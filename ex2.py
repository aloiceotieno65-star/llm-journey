tools = ["python", "c", "claude", "java", "gemini"]
print(tools[0]) #accessing first element of list
print(tools[-1]) #accessing last element of list
print(len(tools)) #how many items
tools.append("msql") #adding new item to list
tools.remove("c") #removing item from list
print(sorted(tools)) #alphabetically sorted list
alombotura={
    "name": "Ibrahim",
    "age": 19,
    "course": "Computer Science",
    "city": "Nairobi",
    "goal": "Become a data scientist"
}
alombotura["game"] = "call of duty" #adding new key-value pair to dictionary
alombotura["age"] = 20 #changing value of key "age"
models = [
    {"name": "llama3.2:3b", "size_gb": 2.0},
    {"name": "llama3.2:7b", "size_gb": 7.0},
    {"name": "llama3.2:13b", "size_gb": 13.0}
]
print(models[1]["name"]) #accessing value of key "name" in second dictionary of list
print(f"Total size of models: {sum(model['size_gb'] for model in models)} GB") #calculating total size of models