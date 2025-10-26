def main():
    s = input()
    answer = 1

    freq = {}
    for key in s:
        freq[key] = freq.get(key, 0) + 1

    values = list(freq.values())
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            answer += values[i] * values[j]

    print(answer)


if __name__ == "__main__":
    main()
