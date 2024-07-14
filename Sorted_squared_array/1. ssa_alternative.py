# T-O(nlogn) | S-O(N)
def sorted_squared_array(nums):
    sorted_nums = [0 for _ in range(len(nums))]
    i, j = 0, len(nums) - 1
    for idx in reversed(range(len(nums))):
        if abs(nums[i]) > abs(nums[j]):
            sorted_nums[idx] = nums[i] * nums[i]
            i += 1
        else:
            sorted_nums[idx] = nums[j] * nums[j]
            j -= 1
    return sorted_nums

