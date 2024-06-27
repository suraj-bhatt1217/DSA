# Time-complexity-O(n) time | Space-complexity-O(n) 
def twoNumSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
    if potentialMatch in nums:
        return [potentialMatch, num]
    else:
        nums[num] = True
    return []