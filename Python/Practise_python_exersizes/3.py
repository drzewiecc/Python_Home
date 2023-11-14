A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B=[]
C=[]

#!!!wazna skladnia!!!
for i in A:
    if i<5:
        print(i)

for i in A:
    if i<5:
        B.append(i)

print("B = ", B)

entered = int(input("Enter a number: "))
for i in A:
    if i<entered:
        C.append(i)
print("Numbers smaller than", entered, "in A are", C)