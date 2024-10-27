num = int(input("Enter the Number"))
isPerfect = False
sum = 0
if num>0:
    for i in range (1,num):
        if num % i == 0:
            sum+=i
    if sum == num:
        isPerfect = True

print("Yes" if isPerfect else "No")  