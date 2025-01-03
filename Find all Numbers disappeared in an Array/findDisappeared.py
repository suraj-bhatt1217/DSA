def findDisappeared(nums):
    
    mySet = set(nums)
    res = list()
    n = len(nums)
    
    for i in range(1, n + 1):
        if i not in mySet:
            res.append(i)
    
    return res
        

nums = []

print(findDisappeared(nums))