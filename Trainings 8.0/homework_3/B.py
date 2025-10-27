from collections import deque


def solution():

    n = int(input())

    graph = [[] for _ in range(n)]
    power = [0] * n
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        power[u] += 1
        power[v] += 1

    q = deque()
    distances = [-1] * n
    sources = [-1] * n
    for i in range(n):
        if power[i] == 1:
            q.append(i)
            distances[i] = 0
            sources[i] = i

    while q:
        u = q.popleft()

        for v in graph[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                sources[v] = sources[u]
                q.append(v)
            elif sources[u] != sources[v]:
                return distances[u] + distances[v] + 1


print(solution())
