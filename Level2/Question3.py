arr = [1, 2, 3, 4, 5]
k = 6
count = 0

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == k:
            count+=1
print("Number of pairs with sum", k, ":", count)
