def hcf(n1, n2):
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            hcf = i
    return hcf


n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the first number : "))
print("HCF of {} and {} is {}.".format(n1, n2, hcf(n1, n2)))
