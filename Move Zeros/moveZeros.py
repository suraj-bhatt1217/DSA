def moveZeros(nums: list[int]) -> list[int]:
    l = r = 0 
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums

print(moveZeros([1,2,0,3,4,0,0,5,6,7]))