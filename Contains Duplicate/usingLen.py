def containsDuplicate(nums):
    return len(nums) != len(set(nums))

print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8]))
print(containsDuplicate([1, 2, 3, 1, 5, 6, 7, 8]))
print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 7]))