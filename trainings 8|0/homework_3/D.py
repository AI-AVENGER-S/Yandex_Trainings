LIMIT = 2 * 10**10


def solve():
    n, p = map(int, input().split())
    c = list(map(int, input().split()))

    data = [(num, index) for index, num in enumerate(c, 1)]
    data = sorted(data, key=lambda item: item[0])
    answer = LIMIT
    valid_pair = None

    j = 1
    for i in range(n - 1):
        while j < n - 1 and data[j][0] < data[i][0] * p:
            j += 1

        if i != j:
            if data[j][0] == data[i][0] * p:
                return str(data[j][1]) + " " + str(data[i][1])

            elif j < n and data[j][0] > data[i][0] * p:
                case01 = abs(data[j][0] / data[i][0] - p)
                case02 = abs(data[j - 1][0] / data[i][0] - p) if i < j - 1 else LIMIT
                if case02 < answer or case01 < answer:
                    answer = min(case01, case02)
                    if answer == case01:
                        valid_pair = (data[i][1], data[j][1])
                    else:
                        valid_pair = (data[i][1], data[j - 1][1])

            elif data[j][0] < data[i][0] * p:
                case01 = abs(data[j][0] / data[i][0] - p)
                if case01 < answer:
                    answer = case01
                    valid_pair = (data[i][1], data[j][1])

    return str(valid_pair[1]) + " " + str(valid_pair[0])


print(solve())
