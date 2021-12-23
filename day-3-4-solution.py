
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")




====================
My code
#pizza Sizes S=Small, M=medium, L=large
size  = input("What size pizza do you want? S, M, or L M")

#pepperoni ingredients additional Y=Yes, N=No
pepperoni = input("Do you want pepperoni? Y or N")
#chesse ingredients additional Y=Yes, N=No
cheese = input ("Do you want extra chesse? Y or N")

#Pizza sizes price 
smallP = 15 #$
mediumP = 20 #$
largeP = 25 #$

#ingredients pepperoniS size prices
pepperoniS = 2 #$
pepperoniML= 3 #$ /Medium and Large

#Extra Cheese ingredients
cheesePrice = 1 #$
mypizza =""
if size == "s":
  mypizza = smallP
 # print(mypizza)
if size == "m": 
  mypizza = mediumP
 #print(mypizza)
if size == "l":    
  mypizza = largeP
#  print(mypizza)

mypepperoni = "0" 
if pepperoni == "y":
    pepperoniSize = input("What pepperoni size? S=Small, M=Medium, L=Large?")
    if pepperoniSize == "s":
         mypepperoni = pepperoniS
         # print(mypepperoni)
    if pepperoniSize == "m" or pepperoniSize == "l" :     
         mypepperoni = pepperoniML
         # print(mypepperoni)
         
    
mycheese="0"
if cheese == "y" :
    mycheese = cheesePrice
   
    
print (f"Pizza $:{mypizza}\nPepperoni $:{mypepperoni}\ncheese $:{mycheese}")    
total = mypizza+mypepperoni+mycheese
print ("_______\ntotal:$",total)    
    
