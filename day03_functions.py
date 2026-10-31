def greet():
    print("Hello Ibrahim")

greet()
greet()

#with parameters
def greet(name, age):
    print(f"Hello {name}, you are {age} years old ")

greet("Ibrahim", 19)
greet("Jojo", 24)

#using return
def add(a, b):
    return a + b
result = add(5, 6)
print(result)
print(add(10, 4) * 6)

#Default values make parameter optional
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
print(greet("Ibrahim"))
print(greet("Ibrahim", "Habari"))

#word counter function
def count_words(text):
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    return counts   

print(count_words("the cat sat on the mat at the end"))         
print(count_words("a b a c b a"))