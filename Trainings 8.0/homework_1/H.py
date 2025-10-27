def main():
    n, m = map(int, input().split())
    s = input()
    data = []

    for i in range(0, n, n // m):
        data.append(s[i : i + n // m])

    words = {}
    for i in range(m):
        word = input()
        if word not in words:
            words[word] = []
        words[word].append(i + 1)

    for word in data:
        print(words[word][-1], end=" ")
        words[word].pop()


if __name__ == "__main__":
    main()
