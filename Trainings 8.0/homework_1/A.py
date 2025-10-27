def main():
    n = int(input())
    data = list(map(int, input().split()))

    vasya = []
    maria = []

    for i in range(0, n, 2):
        vasya.append(data[i])
    for i in range(1, n, 2):
        maria.append(data[i])

    vasya.sort()
    maria.sort()

    result_with_swap = (sum(vasya) - vasya[0] + maria[-1]) - (
        sum(maria) - maria[-1] + vasya[0]
    )
    result_without_swap = sum(vasya) - sum(maria)
    print(max(result_without_swap, result_with_swap))


if __name__ == "__main__":
    main()
