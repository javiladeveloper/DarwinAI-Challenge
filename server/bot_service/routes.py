from dotenv import load_dotenv  # type: ignore # Para cargar variables de entorno desde .env
from flask import jsonify, request  # type: ignore # Para manejar respuestas y solicitudes HTTP en Flask
from langchain_community.llms import OpenAI  # type: ignore # Para utilizar LangChain con el modelo de lenguaje OpenAI
from .models import db, Expense, User  # Importa los modelos de la base de datos y SQLAlchemy
from .utils import type_condition, isNumeric, condition_promp  # Funciones y constantes auxiliares

# Carga las variables de entorno del archivo .env
load_dotenv()

# Inicializa el modelo de lenguaje con un parámetro de temperatura específico
llm = OpenAI(temperature=0.2)

# Función para configurar las rutas de la aplicación Flask
def configure_routes(app):
    @app.post('/api/add_expense')  # Define una ruta POST para añadir gastos
    def add_expense():
        # Obtiene los datos enviados en formato JSON
        data = request.get_json()
        telegram_id = data['telegram_id']  # Extrae el ID de Telegram del usuario

        # Verifica si el usuario está en la lista blanca
        check_whiteList = is_user_whitelisted(telegram_id)

        message = data['message']  # Extrae el mensaje enviado por el usuario

        # Analiza el mensaje para obtener la categoría y el monto del gasto
        category = custom_message(message, type_condition.categorize)
        expense = custom_message(message, type_condition.expense)

        # Procesa y guarda el gasto si el usuario está en la lista blanca y los datos son válidos
        if check_whiteList and isNumeric(expense) and category:
            amount = int(expense)
            response = Expense(user_id=check_whiteList.id, category=category, amount=amount, description=message)
            db.session.add(response)
            db.session.commit()
            return jsonify({'message': f'{category} expense added ✅'})
        
        # Retorna un mensaje de error si los datos no son válidos
        return jsonify({"error": "Invalid message"}), 400

# Función para obtener un mensaje personalizado utilizando LangChain y OpenAI
def custom_message(message, type):
    # Crea un prompt basado en el mensaje y el tipo de información requerida
    prompts = [condition_promp(message, type)]
    
    # Genera una respuesta utilizando LangChain con el modelo de lenguaje OpenAI
    response = llm.generate(prompts=prompts)
    return response.generations[0][0].text.strip()

# Función para verificar si un usuario de Telegram está en la lista blanca
def is_user_whitelisted(telegram_id):
    # Busca al usuario por su ID de Telegram en la base de datos
    user = User.query.filter_by(telegram_id=telegram_id).first()
    return user
