freq={}
def freq_count(nums):
    for i in nums:
        if i in freq.keys():
            freq[i] +=1
        else:
            freq[i] = 1

freq_count([1, 2, 3, 2, 4, 1, 2, 4, 5])
print(freq)