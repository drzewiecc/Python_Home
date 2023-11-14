a = int(input("Enter a number: "))
if a%2==0:
    print(a, " is an even number.")
else:
    print(a, "is an odd number.")

if a%4==0:
    print(a, "is a multiply of 4.")

b = int(input("Enter a number: "))
c = int(input("Enter another number: "))
if b%c==0:
    print(b, "is divisible by", c, ".")
else:
    print(b, "isn't divisible by", c, ".")