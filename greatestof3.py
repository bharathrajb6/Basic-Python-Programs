a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if a>b and a>c:
    print("{} is greater.".format(a))
elif b>a and b>c:
    print("{} is greater.".format(b))
else:
    print("{} is greater.".format(c))