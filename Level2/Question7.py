def median(nums):
    l= len(nums)
    if l%2 == 1:
        return nums[l//2]
    else:
        middle1 = nums[l//2-1]
        middle2 = nums[l//2]
        return (middle1+middle2) //2



number_list = [7, 2, 5, 1, 9, 3]
print(median(number_list))