def is_leap_year(year):
    if year % 4 ==0 and (year %100 !=0 or year % 400 == 0):
       print("True")
    else:
        print("False")

is_leap_year(int(input("Enter a Year: ")))
