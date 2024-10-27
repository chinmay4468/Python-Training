def cal_sum(num):
    nums = [int(digit) for digit in str(num)]
    s = sum(nums)
    return s

n = int(input("Enter the Number"))
while(n>10):
    n= cal_sum(n)
print(f"Single Digit sum: {n}")