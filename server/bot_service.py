from aiohttp import web
import asyncpg
import os
from dotenv import load_dotenv
import json

load_dotenv()

async def init_db():
    return await asyncpg.connect(dsn=os.environ['DATABASE_URL'])

async def handle_expense(request):
    data = await request.json()
    db = await init_db()

    # Aquí iría la lógica para procesar el mensaje
    # Esta es una simplificación

    await db.close()
    return web.json_response({"message": "Expense processed"})

app = web.Application()
app.add_routes([web.post('/process', handle_expense)])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)