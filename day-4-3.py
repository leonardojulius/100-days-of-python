row1 = ["#","#","#"]
row2 = ["#","#","#"]
row3 = ["#","#","#"]

map=[row1, row2, row3] 
print(f"{row1}\n{row2}\n{row3}\n")

tables = input("Where do you want to put the treasure? ")
rows= int(tables[0])-1 #row
column = int(tables[1])-1 #column

result = map[column][rows]="x"

print(f"{row1}\n{row2}\n{row3}\n")
