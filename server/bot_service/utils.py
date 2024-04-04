from .enums import type_condition
def isNumeric(response):
    try:
        if int(response)>0:
            return True
    except ValueError:
        return False



def condition_promp(message, type):
    if type == type_condition.categorize:
        return f"Categorize the following expense: '{message}'. The possible categories are: Housing, Transportation, Food, Utilities, Insurance, Medical/Healthcare, Savings, Debt, Education, Entertainment, and Other."
    elif type == type_condition.expense:
        return f"Analyze the following message: '{message}'. If it is a message where a real number appears, respond only with the number without decimals, otherwise it returns, 'It is not an expense.'"
