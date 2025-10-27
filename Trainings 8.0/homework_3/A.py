def solve():
    a, b, s = map(int, input().split())

    l, r = 1, 10**8

    while l <= r:
        L = (l + r) // 2
        if (L - a) * (L - b) == s:
            return L
        elif (L - a) * (L - b) > s:
            r = L - 1
        elif (L - a) * (L - b) < s:
            l = L + 1

    if (l - a) * (l - b) == s:
        return l
    else:
        return -1


print(solve())
