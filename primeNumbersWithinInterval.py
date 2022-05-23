# Python program to display all the prime numbers within an interval
lower = int(input("Enter the lower interval : "))
upper = int(input("Enter the upper interval : "))

for i in range(lower, upper + 1):
    if i > 1:
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if not flag:
            print(i)
