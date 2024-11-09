
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

x = int(input("Enter Numner 1: "))


operation = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div

}

y = int(input("Enter Number 2: "))
selector = input("Enter the Operations [+, - , *, / ]:  ")

print(operation[selector](x,y))

