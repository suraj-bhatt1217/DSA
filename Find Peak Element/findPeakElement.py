def findPeakElement(nums):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = l + ((r - l) // 2)
        
        if m > 0 and nums[m] < nums[m - 1]:
            r = m - 1
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m
        
print(findPeakElement([1, 2, 3, 1]))