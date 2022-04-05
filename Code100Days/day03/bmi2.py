height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/(height*2)


if bmi<=18.5:
    print("your bmi is : " + str(bmi) + ". You are underweight")
elif bmi <= 25:
    print(f"your bmi is : {bmi}. You are normal weight")
elif bmi <=30:
    print("your bmi is : " + str(bmi) + ". You are overweight")
elif bmi <=35:
    print("your bmi is : " + str(bmi) + ". You are obese")
else:
    print("your bmi is : " + str(bmi) + ". You are clinically obese")