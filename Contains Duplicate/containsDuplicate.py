def containsDuplicate(nums):
    mySet = set()
    for num in nums:
        if num not in mySet:
            mySet.add(num)
        else:
            return True
    return False

print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8]))
print(containsDuplicate([1, 2, 3, 1, 5, 6, 7, 8]))
print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 7]))