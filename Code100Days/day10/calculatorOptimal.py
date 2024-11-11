def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

operation = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div

}


def calculator():
    num1 = float(input("Enter Number 1: "))
    memory_enabled = True

    while memory_enabled:
            for symbol in operation:
                print(symbol)

            operator_selected = input("Select an operator: ")
            num2 = float(input("Enter number 2: "))

            result = operation[operator_selected](num1, num2)
            print(f"{num1} {operator_selected} {num2} = {result}")

            should_continue = input("Should we continue using the result ? Type 'Y' or 'N' ")

            if should_continue == "Y":
                num1 = result
            elif should_continue == "N":
                memory_enabled = False
                print("\n" * 100)

calculator()