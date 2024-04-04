# Importa SQLAlchemy para manejar la base de datos
from flask_sqlalchemy import SQLAlchemy

# Crea una instancia de SQLAlchemy para usar en la definición de modelos
db = SQLAlchemy()

# Define el modelo User para la tabla 'users' en la base de datos
class User(db.Model):
    # Especifica el nombre de la tabla en la base de datos
    __tablename__ = 'users'

    # Define las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Columna de ID como clave primaria
    telegram_id = db.Column(db.String(100), unique=True, nullable=False)  # ID de Telegram único para cada usuario
    is_whitelisted = db.Column(db.Boolean, default=False)  # Indica si el usuario está en la lista blanca

    # Establece una relación entre User y Expense (un usuario puede tener muchos gastos)
    expenses = db.relationship('Expense', backref='user', lazy=True)

    # Representación en cadena del objeto, útil para depuración y registro
    def __repr__(self):
        return f'<User {self.telegram_id}>'
    
# Define el modelo Expense para la tabla 'expenses' en la base de datos
class Expense(db.Model):
    # Especifica el nombre de la tabla en la base de datos
    __tablename__ = 'expenses'

    # Define las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # Columna de ID como clave primaria
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Clave foránea que enlaza con el ID del usuario
    category = db.Column(db.String(50), nullable=False)  # Categoría del gasto
    amount = db.Column(db.Float, nullable=False)  # Monto del gasto
    description = db.Column(db.String(255), nullable=True)  # Descripción opcional del gasto
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())  # Fecha y hora de creación del gasto, establecido automáticamente

    # Representación en cadena del objeto, útil para depuración y registro
    def __repr__(self):
        return f'<Expense {self.category} - {self.amount}>'
