import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = [0] * n

stack = deque()
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        stack.pop()

    if not stack:
        result[i] = i
    else:
        result[i] = i - stack[-1] - 1

    stack.append(i)

sys.stdout.write(" ".join(map(str, result)) + "\n")
