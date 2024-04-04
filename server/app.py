# Importa las clases y funciones necesarias de los módulos Flask y dotenv
from flask import Flask
from dotenv import load_dotenv
import os
# Importa la función para configurar rutas y el objeto de la base de datos desde el módulo bot_service
from bot_service import configure_routes
from bot_service.models import db

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Define la función create_app para inicializar y configurar la aplicación Flask
def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)

    # Configura la URI de la base de datos SQLAlchemy a partir de las variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

    # Inicializa la extensión de SQLAlchemy con la aplicación Flask configurada
    db.init_app(app)

    # Configura las rutas de la aplicación usando la función configure_routes
    configure_routes(app)
    
    # Retorna la instancia de la aplicación Flask configurada
    return app

# Verifica si el script se ejecuta directamente (no importado)
if __name__ == '__main__':
    # Crea una instancia de la aplicación Flask
    app = create_app()

    # Ejecuta la aplicación Flask en modo debug, utilizando el host y puerto definidos en las variables de entorno
    app.run(debug=True, host=os.getenv("HOST"), port=int(os.getenv("PORT")))
