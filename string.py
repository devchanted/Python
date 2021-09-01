print("Harry Potter") #Double Quotes

got = "Game of Thrones" #Double Quotes
print(got)

bbt = 'Bing Bang Theory' #Single Quotes
print(bbt)

print("$") #Single Character

print("") #Empty String

random_string = "Iam Batman"

print(len(random_string)) #Length of the String

#String Indexing
batman = "Bruce Wayne"
first_letter = batman[0]
print("First Letter is " +first_letter)
last_letter = batman[-1]
print('Last Letter is ' +last_letter)

#String Slicing
my_string = "This is my String"
print("First 4 letters of my string is " +my_string[0:4])
print("from 8 to last " +my_string[8:len(my_string)])

print("------Slice with Step-----")

#String[start:end:Step]
print(my_string[0:7])
print(my_string[0:7:2])
print(my_string[0:7:5])

print("------Reverse Slicing-----")
print(my_string[13:2:-1])
print(my_string[17:0:-2])

print("------Partial Slicing-----")
print(my_string[:8])
print(my_string[8:])
print(my_string[:])
print(my_string[::-1])
