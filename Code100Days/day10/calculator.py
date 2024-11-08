
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

operation_memory = add

x = int(input("Enter Numner 1: "))
y = int(input("Enter Number 2: "))

operation = input("Enter the Operations [+, - , *, / ]:  ")

if operation == "+":
    operation_memory = add
elif operation == "-":
    operation_memory = sub
elif operation == "*":
    operation_memory = mul
else:
    operation_memory= div

print(operation_memory(x,y))
