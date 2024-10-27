def rotate_arr(arr,d):
    d = d % len(arr)
    return arr[d:]+arr[:d]


arr = [1, 2, 3, 4, 5]
D = 2
r = rotate_arr(arr,D)
print(r)
