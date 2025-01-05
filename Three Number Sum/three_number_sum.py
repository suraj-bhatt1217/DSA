def three_num_sum(a: list, target: int):
    ans = []
    a.sort()
    for idx, ele in enumerate(a):
        temp = ele
        left = idx + 1
        right = len(a) - 1
        while left <= right:
            if temp + a[left] + a[right] == target:
                ans.append([idx, left, right])
                left += 1
                right -= 1
            elif temp + a[left] + a[right] < target:
                left += 1
            else:
                right -= 1
    return ans