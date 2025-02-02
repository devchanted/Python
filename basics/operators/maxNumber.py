
a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))


def max(a,b):
    
    if a>b :
        return a
    elif a == b:
        return "Equal"
    else:
        return b
    
print(max(a,b))