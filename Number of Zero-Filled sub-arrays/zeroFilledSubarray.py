def zeroFilledSubarray(nums):
    count = 0
    res = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            count = 0
        res += count
    
    return res

print(zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 2, 9, 0]))