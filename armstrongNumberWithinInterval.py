lower=int(input("Enter the lower interval : "))
upper=int(input("Enter the upper interval : "))

for i in range(lower,upper+1):
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if i==sum:
        print(i)