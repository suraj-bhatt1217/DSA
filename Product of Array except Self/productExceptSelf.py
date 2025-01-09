def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n
    pre = 1
    for i in range(n):
        ans[i] = pre
        pre *= nums[i]

    post = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= post
        post *= nums[i]

    return ans


print(productExceptSelf([-1, 1, 0, -3, 3]))
