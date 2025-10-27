def main():
    n, m = map(int, input().split())

    matrix = [input() for _ in range(n)]
    diagonals_right = {}
    horizontals = {}
    diagonals_invert = {}

    for i in range(n):
        for j in range(m):
            key = i - j
            if key not in diagonals_right:
                diagonals_right[key] = []
            diagonals_right[key].append(matrix[i][j])

            if j not in horizontals:
                horizontals[j] = []
            horizontals[j].append(matrix[i][j])

            key = i + j
            if key not in diagonals_invert:
                diagonals_invert[key] = []
            diagonals_invert[key].append(matrix[i][j])

    def checker(matrix):
        for lst in matrix:
            result = 1
            for i in range(len(lst) - 1):
                if lst[i] == lst[i + 1] and lst[i] != ".":
                    result += 1
                    if result >= 5:
                        return True
                else:
                    result = 1
        return False

    return (
        "Yes"
        if checker(matrix)
        or checker(list(horizontals.values()))
        or checker(list(diagonals_right.values()))
        or checker(list(diagonals_invert.values()))
        else "No"
    )


if __name__ == "__main__":
    print(main())
