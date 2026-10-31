#Reading a filie
with open("notes.txt", "r") as f:
     content = f.read() # Dispalying the whole file as one string
print(content)    

with open("notes.txt", "r") as f:
    for line in f:   #One line at a time
        print(line.strip()) #strip() removes the \n and extra spaces
      #without strip() -you get blank lines btwn everything  