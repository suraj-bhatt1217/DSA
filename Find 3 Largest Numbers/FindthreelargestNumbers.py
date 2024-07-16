# T-O(N) | S-O(1)

nums = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]


def get_three_largest(nums):
    largest_nums = [None] * 3
    for num in nums:
        if largest_nums[2] is None or num > largest_nums[2]:
            largest_nums[0] = largest_nums[1]
            largest_nums[1] = largest_nums[2]
            largest_nums[2] = num
        elif largest_nums[1] is None or num > largest_nums[1]:
            largest_nums[0] = largest_nums[1]
            largest_nums[1] = num
        elif largest_nums[0] is None or num > largest_nums[0]:
            largest_nums[0] = num
        else:
            continue
    return largest_nums


print(get_three_largest(nums))
