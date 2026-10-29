print(5>3) # True
print(5==3) # False
print(5!=3) # True
print(5>=5) # True
print("a" == "a") # True
#testing if/elif/else statements
score = 72
if score>= 80 :
    print ("Distinction")
elif score >= 60:
    print ("Pass")
else:
    print ("Failure")

#Combine conditions with and, or, not
age = 19
has_id = True
if age >= 18 and has_id:
    print("Getting old")    
if age < 18 or not has_id:
    print("Not allowed")    
#using loops
tools = ["python", "c", "claude", "java", "gemini"]
for tool in tools:
    print(f"Learning {tool} is fun!") #using f-string to format output
for i in range(5):
    print(i) #printing numbers from 0 to 4
for i in range(1,6):
    print(i) #printing numbers from 1 to 5
#loop over a dictionary's pairs

person = {
    "name": "Ibrahim",
    "age": 19,
    "course": "Computer Science",
    "city": "Nairobi",
    "goal": "Become a data scientist"
}    
for key, value in person.items():
    print(f"{key}: {value}")

#Putting loops and conditions together
scores = [72, 88, 95, 60, 45]
passed = 0
for score in scores:
    if score >= 60:
        passed = passed + 1

print(f"{passed} out of {len(scores)} students passed the exam.")

# While loops
count = 3
while count > 0:
    print(count)
    count = count - 1

print("Blast off!")
