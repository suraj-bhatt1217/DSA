def findDisappeared(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))

print(findDisappeared([1, 1, 1, 1]))