# Importa el enumerado type_condition para determinar el tipo de condición de procesamiento
from .enums import type_condition

# Define una función para verificar si una respuesta es numérica y positiva
def isNumeric(response):
    try:
        # Intenta convertir la respuesta en un entero y verifica si es mayor que cero
        if int(response) > 0:
            return True
    except ValueError:
        # Si ocurre un ValueError durante la conversión, retorna Falso
        return False

# Define una función para generar un prompt basado en el tipo de análisis requerido
def condition_promp(message, type):
    # Verifica si el tipo es para categorización de gastos
    if type == type_condition.categorize:
        # Retorna un prompt para la categorización de gastos
        return f"Categorize the following expense: '{message}'. The possible categories are: Housing, Transportation, Food, Utilities, Insurance, Medical/Healthcare, Savings, Debt, Education, Entertainment, and Other."
    # Verifica si el tipo es para análisis de monto de gasto
    elif type == type_condition.expense:
        # Retorna un prompt para analizar si el mensaje contiene un monto de gasto
        return f"Analyze the following message: '{message}'. If it is a message where a real number appears, respond only with the number without decimals, otherwise it returns, 'It is not an expense.'"
