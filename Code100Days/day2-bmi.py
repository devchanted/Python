#PEMDAS with M&D with similar priority but goes from left ot right

from cgi import print_directory


print (3 * 3 + 3 /3 - 3 )

height = input("Enter your height in meter: ")
weight = input("Enter your weight in kg: ")

BMI = float(weight) / (float(height) ** 2)

print(round(BMI))
print(int(BMI))