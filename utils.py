import os 
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(
                "Please enter a whole number"
            )
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid data")
def get_grade(score):
    if score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    else:
        return "Grade F"
def format_currency(amount):
    return f"{amount:,.0f},MMK"
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")