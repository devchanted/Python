def format_name(f_name,l_name):

    formatted_fname = f_name.title()
    formatted_lname= l_name.title()
    return f"{formatted_fname} {formatted_lname}" 



output = format_name(input("Enter First Name: "), input("Enter LastName: "))

print(output)