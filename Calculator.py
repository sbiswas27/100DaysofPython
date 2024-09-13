def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    should_accumulate = True
    first_number = float(input("Enter the first number: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_chosen = input("Pick an operation: ")
        second_number = float(input("Enter the second number: "))
        result = round(operations[operation_chosen](n1=first_number,n2=second_number),2)
        print(f"{first_number} {operation_chosen} {second_number} = {result}")

        choice = input(f"Do you want to continue with {result} press 'y' or enter a new calculation, press 'n'? ").lower()
        if choice=='y':
            first_number = result
        else:
            should_accumulate = False
            print('\n' * 20)
            calculator()

calculator()
