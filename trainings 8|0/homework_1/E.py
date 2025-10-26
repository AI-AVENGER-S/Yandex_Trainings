def main():
    n, k = map(int, input().split())

    def short(n, k):
        lst_loop = []

        result = n
        digit = result % 10
        while digit not in lst_loop and k:
            lst_loop.append(digit)
            result += digit
            digit = result % 10
            k -= 1
        if not k:
            return result

        lst_loop.append(digit)
        first_index = lst_loop.index(lst_loop[-1])

        lst_loop = lst_loop[first_index:-1]
        distance = len(lst_loop)
        sum_of_loop = sum(lst_loop)
        result += (k // distance) * sum_of_loop
        k %= distance

        for i in range(len(lst_loop)):
            if not k:
                break
            result += lst_loop[i]
            k -= 1

        return result

    print(short(n, k))


if __name__ == "__main__":
    main()
