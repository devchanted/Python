
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

operator = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div

}

def logic():
    x = int(input("Enter Numner 1: "))
    selector = input("Enter the operator [+, - , *, / ]:  ")
    y = int(input("Enter Number 2: "))
    answer = operator[selector](x,y)
    print(f"{x} {selector} {y} = {answer}")
    return answer
answer = logic()
choice = input(f" Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: " )

if choice == "y":
    selector = input("Enter the operator [+, - , *, / ]:  ")
    z = int(input("Enter Number 2: "))
    new_answer = operator[selector](answer,z)
    print(f"{answer} {selector} {z} = {new_answer}")
elif choice == "n":
    logic()

else:
    print("Error")

