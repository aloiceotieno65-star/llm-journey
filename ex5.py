def square(n):
    return n  * n
print(square(5))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))    
print(is_even(7))

def grade(score):
    if score >= 80:
       return "Distinction"
    elif score >= 70 :
       return "Merit"
    elif score >= 50:
       return "Pass"
    else :
       return "Fail"

for s in [78, 16, 88, 69, 82] :
 print(f"{s} : {grade(s)}")

def average(numbers):
   total = 0
   for number in numbers:
    total = total + number
   return total/len(numbers)

numbers = [72, 88, 95]
print(average(numbers))   

def fizzbuzz(n):
   if n % 3 == 0 and n % 5 == 0 :
      return "FizzBuzz"
   elif n % 3 == 0:
      return "Fizz"
   elif n % 5 == 0:
      return "Buzz"
   else:
      return n

for i in range(1,31):
     print(fizzbuzz(i))