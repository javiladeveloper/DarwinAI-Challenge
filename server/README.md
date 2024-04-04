# Expense Tracker Bot API

Este proyecto es una API construida con Flask para un bot de seguimiento de gastos en Telegram. Permite añadir gastos y categorizarlos automáticamente utilizando LangChain con OpenAI.

## Características

- Verificación de usuarios contra una lista blanca.
- Análisis y categorización de mensajes de gastos utilizando LangChain con OpenAI.
- Registro de gastos en una base de datos PostgreSQL.

## Configuración

### Virtual config

- Create a virtual environment: python3 -m venv venv
- Activate the virtual environment: source venv/bin/activate (Linux/Mac) or .\venv\Scripts\activate (Windows)

### Requisitos

Python 3.8+
Flask
flask[async]
flask_sqlalchemy
SQLAlchemy
dotenv
LangChain
psycopg2
Una base de datos PostgreSQL en este caso usamos una levantada en SUPABASE

### Instalación

1. Clona el repositorio:

```
bash
git clone https://github.com/javiladeveloper/DarwinAI-Challenge.git
cd <DIRECTORIO_DEL_REPOSITORIO>
```

2. Instala las dependencias:

```
Copy code
pip install Flask[async] SQLAlchemy python-dotenv langchain psycopg2 flask_sqlalchemy
```

3. Configura las variables de entorno creando un archivo .env en la raíz del proyecto con los siguientes contenidos:

```
bash
SQLALCHEMY_DATABASE_URI=postgresql://postgres.dscvvvbhxouywazgavtc:Jonimon321jojo@aws-0-us-west-1.pooler.supabase.com:5432/postgres

OPENAI_API_KEY=your_openai_api_key
PORT=8080
HOST=localhost
```

Reemplaza los valores de username, password, hostname, port, y dbname con tus credenciales de la base de datos (dejo las credenciales de supabase), y your_openai_api_key con tu clave de API de OpenAI.

### Ejecución

Para ejecutar la aplicación, usa:

```
arduino
python app.py
```

## Uso de la API

### POST /api/add_expense

Añade un nuevo gasto. Espera un JSON con telegram_id y message.

Ejemplo de cuerpo de solicitud:

```
json
{
"telegram_id": "123456789",
"message": "Cena en restaurante por $30"
}
```

Si el usuario está en la lista blanca y el mensaje es válido, se añadirá el gasto.

## Desarrollo

Para agregar nuevas funcionalidades o modificar el comportamiento existente, edita los archivos correspondientes bajo el directorio de tu proyecto.

## Contribución

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, puedes clonar el repositorio, realizar tus cambios y enviar un pull request.
