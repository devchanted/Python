
# insert string in a specific section 

print("This is a string {}".format("INSERTED"))

#Insert in sequence

print("This is a string with sequential insert of {} {} {}".format("Insert1", "insert2", "insert3"))

#insert based on position
print("This is a string with sequential insert of {2} {1} {0}".format("Insert1", "insert2", "insert3"))

# insert based on variable declaration

print("This is a string with sequential insert of {a} {b} {c}".format(a="Insert1", b =  "insert2", c = "insert3"))

#insert directly from format

result = 77/100

print("The Result is {}".format(result))

#without format method

print(f'The result is {result}')