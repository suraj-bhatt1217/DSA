coins = [5, 7, 1, 1, 2, 3, 22]
coins.sort()


def nonConstructibleChange(coins):
    current_change = 0
    for coin in coins:
        if current_change + 1 < coin:
            return current_change + 1
        current_change += coin
    return current_change + 1


print(f"The non-constructible change is {nonConstructibleChange(coins)}")
