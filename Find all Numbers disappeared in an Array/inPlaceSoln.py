def findDisappeared(nums: list[int]) -> list[int]:
    for num in nums:
        i = num - 1
        if nums[i] > 0:
            nums[i] = -nums[i]

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
print(findDisappeared([1, 1, 1, 1]))