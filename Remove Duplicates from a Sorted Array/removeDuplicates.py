def removeDuplicates(nums):
    left = right = 1
    
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    
    return left 

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))