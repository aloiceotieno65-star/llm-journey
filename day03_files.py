#Writing a file
with open ("notes.txt", "w") as f:
 #w means write - creates file
 #a means append - adding to the end without erasing
 f.write("first line\n")    
 f.write("second line\n")
 #\n - new line dummy 
 #with- closses the file automatically when the block ends
 
#Reading a filie
with open("notes.txt", "r") as f:
     content = f.read() # Dispalying the whole file as one string
print(content)    

with open("notes.txt", "r") as f:
    for line in f:   #One line at a time
        print(line.strip()) #strip() removes the \n and extra spaces
      #without strip() -you get blank lines btwn everything  

#appending
with open("notes.txt", "a") as f:
    f.write("third line\n")
    
#Error handling with try/except
try:
    with open("missing.txt", "r") as f:
        print(f.read())    
except FileNotFoundError:
    print("That file doesn't exist")        
    
try:
    number = int("abc")
except ValueError:
    print("That is not a number")        