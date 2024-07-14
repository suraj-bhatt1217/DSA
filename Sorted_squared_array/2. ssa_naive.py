# T-O(nlog(n)) | S-O(n)
def sorted_squared_array(nums):
    sorted_nums = [val * val for val in nums]
    sorted_nums.sort()
    return sorted_nums
