NON_VALID = 3


def solve():
    n = int(input())

    seive = [True] * (n + 1)
    seive[0] = seive[1] = False
    for i in range(2, int(n**0.5) + 1):
        if seive[i]:
            seive[i * i :: i] = [False] * len(seive[i * i :: i])

    dp = [False] * (n + 1)

    for i in range(1, n + 1):
        if i - 1 >= 0 and not seive[i - 1]:
            if not dp[i - 1]:
                dp[i] = True
                continue

        if i - 2 >= 0 and not seive[i - 2]:
            if not dp[i - 2]:
                dp[i] = True
                continue

        if i - 3 >= 0 and not seive[i - 3]:
            if not dp[i - 3]:
                dp[i] = True
                continue
    if dp[n]:
        return 1
    else:
        return 2


print(solve())
