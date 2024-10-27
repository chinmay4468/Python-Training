arr = [1, 2, 3, 4, 5]
index = 5

try:
    print(arr[index])
except IndexError:
    print("Index out of bounds")