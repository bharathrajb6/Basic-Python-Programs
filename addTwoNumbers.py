#normal way
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

result=num1+num2
print("Addition of {} and {} is {}.".format(num1,num2,result))


#using fucntions
def add(n1,n2):
    return n1+n2
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
result=add(n1,n2)
print("Addition of {} and {} is {}.".format(n1,n2,result))



