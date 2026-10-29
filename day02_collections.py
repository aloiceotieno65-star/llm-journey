tools = ["python", "git", "ollama"]
print(tools)
print(tools[0]) #accessing first element of list
print(tools[-1]) #accessing last element of list
print(len(tools)) #how many items
tools.append("vscode") #adding new item to list
tools.remove("git") #removing item from list
print(tools)
print("python" in tools) #checking if item is in list
print(sorted(tools)) #alaphabetically sorted list
print(tools[0:2]) #accessing first two items of list
scores = [72, 88, 95]
scores[0] = 75 #changing first item of list
print(scores)
print(sum(scores), min(scores), max(scores)) #sum, min, max of list
# Dictionaries
person = {
    "name": "Ibrahim",
    "age": 19,
    "course": "Computer Science"
}
print(person["name"]) #accessing value of key "name"
person["gpu"] = "RTX A2000" #adding new key-value pair to dictionary
person["age"] = 20 #changing value of key "age"
print(person) #printing entire dictionary

print(person.keys()) #getting all keys of dictionary
print(person.values()) #getting all values of dictionary
print(person.items()) #getting all key-value pairs of dictionary
print("course" in person) #checking if key is in dictionary
print(person.get("email", "Not set")) #getting value of key "email" with default value if key doesn't exist