import heapq

q = int(input())
heap = []
for _ in range(q):
    data = input().split()
    if len(data) > 1:
        request, x = map(int, data)
    else:
        request = int(data[0])

    match request:
        case 1:
            heapq.heappush(heap, -x)
            if heap:
                print(-heap[0])
            else:
                print(-1)
        case 2:
            if heap:
                heapq.heappop(heap)
            
            if heap:
                print(-heap[0])
            else:
                print(-1)



