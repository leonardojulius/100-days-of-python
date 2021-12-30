# 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights ").split() #split default with space
summ = 0 #as int
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    summ += student_heights[n] #adding loops (student_heights) 
   
#print(summ) # sum of total result

total_height = n+1 #looping from 0, to lenght of input series
div = summ / total_height 
print(round(div))
#print(f"There are a total of 7 heights {n+1}" )

#Write your code below this row 👇
