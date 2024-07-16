# T-O(N) | S-O(D) , D is the depth of the nested list
nums = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def product_sum(nums, multiplier):
    cur_sum = 0
    for num in nums:
        if type(num) == int:
            cur_sum += num
        else:
            value = product_sum(num, multiplier + 1)
            cur_sum += value
    return cur_sum * multiplier


print(product_sum(nums, 1))
