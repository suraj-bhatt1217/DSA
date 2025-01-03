def findDisappeared(nums):
    n = len(nums)
    freq = [0] * n
    
    for num in nums:
        idx = num - 1
        freq[idx] += 1
        
    return [i + 1 for i in range(len(nums)) if freq[i] == 0]

print(findDisappeared([1,1,3,1,5]))