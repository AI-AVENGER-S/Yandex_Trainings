def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = {}
    for key in a:
        freq[key] = freq.get(key, 0) + 1

    elements = list(freq.keys())

    if len(elements) >= k:
        print(*elements[:k])

    else:
        answer = elements[:]
        k -= len(answer)

        for char in a:
            if not k:
                break
            if freq[char] > 1:
                answer.append(char)
                k -= 1
                freq[char] -= 1

        print(*answer)


if __name__ == "__main__":
    main()
