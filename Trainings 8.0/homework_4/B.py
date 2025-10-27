n = int(input())

data = [0] * n
for i in range(n):
    st, price = map(int, input().split())
    data[i] = (st, price)


def search(q):
    global data, n

    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        st = data[mid][0]
        if st == q:
            return mid
        elif st < q:
            l = mid + 1
        elif q < st:
            r = mid - 1
    return l


m = int(input())
for _ in range(m):
    q = int(input())
    index = search(q)
    print(q * data[index - 1][1])
