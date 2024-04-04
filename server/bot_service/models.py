from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(100), unique=True, nullable=False)
    is_whitelisted = db.Column(db.Boolean, default=False)

    # Relación con la tabla de gastos (expenses)
    expenses = db.relationship('Expense', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.telegram_id}>'
    
class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Expense {self.category} - {self.amount}>'