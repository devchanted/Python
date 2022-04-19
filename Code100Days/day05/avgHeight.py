str_height = input("Enter Student height")
student_heights = str_height.split(" ")
print(student_heights)
sum = 0
count = 0
for height in student_heights:
    sum = sum+ int(height)
    count = count+1
average = sum/count
print(f"Average height is : {round(average)}")

