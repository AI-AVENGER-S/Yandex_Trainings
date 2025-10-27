import sys

sys.setrecursionlimit(200_000)

n = int(input())
parents = list(map(int, input().split()))

root = None
graph = [[] for _ in range(n)]

for i in range(n):
    v = i
    if not parents[i]:
        root = v
    else:
        graph[parents[i] - 1].append(v)

timer_in = [0] * n
timer_out = [0] * n
timer = 0


def dfs(v):
    global timer

    timer_in[v] = timer
    timer += 1

    for u in graph[v]:
        dfs(u)

    timer_out[v] = timer
    timer += 1


dfs(root)


def is_ansestor(ansestor, child):
    global timer_in, timer_out

    return (
        True
        if timer_in[ansestor] <= timer_in[child]
        and timer_out[ansestor] >= timer_out[child]
        else False
    )


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if is_ansestor(a, b):
        print(1)
    else:
        print(0)
