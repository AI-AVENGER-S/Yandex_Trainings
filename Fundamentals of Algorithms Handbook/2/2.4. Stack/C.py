from collections import deque

n = int(input())
k = int(input())
a = list(map(int, input().split()))

result = 0
dq = deque()

for i in range(n):
    while dq and a[dq[-1]] >= a[i]:
        dq.pop()

    dq.append(i)
    if dq[0] <= i - k:
        dq.popleft()
    if i >= k - 1:
        result += a[dq[0]]

print(result)
