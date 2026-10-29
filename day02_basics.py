name = "Ibrahim"
age = 19
height = 1.9
is_student = True
print("Name:", name)
print("Age:", age)
print (type(name))
#mathematical operations
print(10*5)
print (10/3)
print(10//3)
#string operations
first_name = "Aloice"
last_name = "Ibrahim"
full_name = first_name + " " + last_name #joining two strings
print("Full name:", full_name)
print("Length of full name:", len(full_name)) #length of string
print("Uppercase full name:",full_name.upper()) #uppercase string   
print("Lowercase full name:",full_name.lower()) #lowercase string
print("First character of full name:",full_name[0]) #accessing first character of string
print("Last character of full name:",full_name[-1]) #accessing last character of string
print("First three characters of full name:",full_name[0:3]) #accessing first three characters of string
#Using f-string to format string
print(f"My name is {full_name} and I am {age} years old.")