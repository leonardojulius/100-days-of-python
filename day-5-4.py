#Write your code below this row 👇

#Write your code below this row 👇
a = 1
b = 101

for n in range(a,b):
   if n%3==0 and n%5==0:    
    print("FizzBuzz")
   elif n%5==0:
    print("Buzz")
   elif n%3==0:
      print("Fizz")
   else:
      print(n)    

