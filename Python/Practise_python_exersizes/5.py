import random
list1=[]
list2=[]
A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def finding(C, D):
    for i in C:
        if i in C and i in D:
            print(i)

if len(A)>len(B):
    finding(A, B)
else:
    finding(B, A)

length = random.randint(1, 20)
while length>=0:
    list1.append(random.randint(1,15))
    length=length-1

length = random.randint(1, 20)
while length>=0:
    list2.append(random.randint(1,20))
    length=length-1

print(list1, list2)

if len(list1)>len(list2):
    finding(list1, list2)
else:
    finding(list2, list1)