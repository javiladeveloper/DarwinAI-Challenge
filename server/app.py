from flask import Flask
from dotenv import load_dotenv
import os
from bot_service import configure_routes
from bot_service.models import db
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    configure_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host=os.getenv("HOST"), port=os.getenv("PORT"))
    

