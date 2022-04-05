print("Lear year check")

year = int(input("Enter the year you want to check? "))

if year%4 == 0:
    if year%100 ==0:
        if year%400 == 0:
            print('Year is a leap year')
        else:
            print("Its not")
    else:
        print("It's a leap year")
else:
    print("Its not")
