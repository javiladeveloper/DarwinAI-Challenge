import os
from dotenv import load_dotenv
from flask import jsonify, request
from psycopg2 import connect
from langchain.llms import OpenAI
from .models import db, Expense, User
from .utils import type_condition, isNumeric, condition_promp


load_dotenv()
llm = OpenAI(temperature=0.7)
def configure_routes(app):
    @app.post('/api/add_expense')
    def add_expense():
        data = request.get_json()
        telegram_id = data['telegram_id']
        check_whiteList = is_user_whitelisted(telegram_id)
        message = data['message']
        category = custom_message(message,type_condition.categorize)
        expense = custom_message(message,type_condition.expense)
        if check_whiteList:
            if isNumeric(expense):
                if category:
                    amount = int(expense)
                    response = Expense(user_id=check_whiteList.id, category=category, amount=amount, description= message)
                    db.session.add(response)
                    db.session.commit()
                    return jsonify({'message': f'{category} expense added ✅'}) 
        return jsonify({"error": "Invalid message"}), 400
def custom_message(message, type):
    prompts = [condition_promp(message,type)]
    response = llm.generate(prompts=prompts)
    return response.generations[0][0].text.strip()

def is_user_whitelisted(telegram_id):
    user = User.query.filter_by(telegram_id=telegram_id).first()
    return user