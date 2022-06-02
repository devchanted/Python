def is_leap(year):
    leap = False
    
    if year%100 != 0 or year%400 == 0:
        return False   
    else:
        return True

    return leap

year = int(raw_input())
print is_leap(year)