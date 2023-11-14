a = int(input("Enter a number: "))
x = range(1, a+1)
for i in x:
    if a%i==0:
        print(i)