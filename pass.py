
import random
print("Welcome to the PyPassword Generator")


passowrdLenght=  int(input("How many letters would like in your password?"))
symbolLen = int(input("How many symbols do you want?"))
numsLen = int(input("How many numbers?"))


letters=["a","b","c","e"]
symbols=["@","!","#","$","%","^","&","*","(",")","_","+","="]
nums = ["1" ,"2", "3","4","5,","6","7","8","9","0"]

letterRes = ""
for letter in range(0,(passowrdLenght)):

  ran=random.randint(0,passowrdLenght-1)
  letterRes += letters[ran]
print(letterRes)


symbolRes = ""
for symboll in range(0,(symbolLen)):

  ran=random.randint(0,symbolLen-1)

  symbolRes += symbols[ran]
print(symbolRes)


numsRes = ""
for numss in range(0,(numsLen)):
  ran=random.randint(0,numsLen-1)
  numsRes += nums[ran]
print(numsRes)

combination=letterRes+symbolRes+numsRes



ranIndex = ""
for combine in range(0,len(combination)):
   combine = int(combine)
   x = random.randint(0,combine)
   ranIndex +=combination[x]

print(ranIndex)
#for passowrdLenghts in range(1,passowrdLenght):
#print(passowrdLenghts)
