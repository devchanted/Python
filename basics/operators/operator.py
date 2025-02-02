#Arithmetic Operators

print("---Addition---")
print(10 + 5)

float1 = 13.65
float2 = 33.33
print(float1+float2)

num = 10
flt = 2.22
print(num + flt)

print("---Subtraction---")
print(33-3)
print(float2-float1)
print(num-flt)

print("---Divison---")
print( 40/10)
print(float2/float1)

print("----Floor Division---")
print(43//10)
print(float2//float1)
print(5.5//4.4)
print(12.4//2)

print("---Modulo---")
print(10%2)
print(10%3)
twenty_eight = 28
print(twenty_eight % 10)
print(-28 % 10)
print(28 % -10)
print(34.4 % 2.5)

print("---Precedence---")
# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication


print("---Parantheses---")
print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))

print("---Assignment Operators---")

year = 2010
print(year)

year = 2021
print(year)

year = year+1
print( year)

first = 20
second = first
first = 35  # Updating 'first'

print(first, second)  # 'second' remains unchanged

print("---Assign---")
num = 10
print(num)

print("---Add&Assign---")
num += 5
print(num)

print("---Subtract&Assign---")
num -= 5
print(num)

print("---Multiply&Assign---")
num *= 2
print(num)

print("---Divide&Assign---")
num /= 2
print(num)

print("---RaisePower&Assign---")
num **= 2
print(num)


print("Divide, Floor, and Assign")
num //= 2
print(num)

print("Take Modulo and Assign")
num %= 7
print(num)



