start = int(input("Enter the start range"))
stop = int(input("Enter the stop range"))
sum = 0
for i in range(start,stop):
    if i%2!=0:
        sum+=i
print(sum)