# Prime number - Divisible by 1 and that number 

def prime_checker(number):
    is_prime = True

    for i in range(2,number):
        if number%i == 0:
            is_prime = False
    if is_prime:
        print(" Prime")
    else:
        print("Not Prime")

prime_checker(int(input("Enter a Number: ")))