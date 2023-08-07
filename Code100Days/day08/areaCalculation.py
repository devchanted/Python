#calculate number of cans of paint needed to cover a wall area
import math
def num_of_cans(height,width,coverage):
    area = int(height) * int(width)
    cans = area/int(coverage)
    return math.ceil(cans)

total_cans = num_of_cans(height=input("height: "), width= input("Weight: "), coverage= input("Coverage: ") )
print (f"Total number of Cans: {total_cans}")
