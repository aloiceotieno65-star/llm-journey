score =[78, 16, 88, 69, 82]
for s in score:
    if s >= 80:
        print(f"Score: {s} - Distinction")
    elif s >= 70:
        print(f"Score: {s} - Merit")
    elif s >= 50:
        print(f"Score: {s} - Pass")
    else:
        print(f"Score: {s} - Fail")
for i in range(1,31):
    if i % 3 ==0 and i %5 == 0:
            print (f"FizzBuzz: {i}")
    elif i %3 == 0:
        print(f"Fizz: {i}")
    elif i % 5 == 0:
        print(f"Buzz: {i}")
    else:
        print(i)

models = [
    {"name": "llama3.2:3b", "size_gb": 2.0},
    {"name": "llama3.2:8b", "size_gb": 8.0},
    {"name": "qwen2.5:7b", "size_gb": 7.0},
]
gpu_limit = 4
for model in models:
    if model["size_gb"] <= gpu_limit:
        print(f"{model['name']}fits on your GPU")

text = "the cat sat on the mat the end"
words = text.split() #splitting string into list of words

counts = {} #empty notebook    
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)            