def main():
    a, b, c, v0, v1, v2 = map(int, input().split())
    cases = []
    cases.append(a / v0 + c / v1 + b / v2)
    cases.append(b / v0 + c / v1 + a / v2)

    cases.append(a / v0 + c / v0 + c / v1 + a / v2)
    cases.append(b / v0 + c / v0 + c / v1 + b / v2)

    cases.append(a / v0 + a / v1 + b / v0 + b / v1)

    cases.append(a / v0 + c / v0 + c / v1 + a / v1 + a / v0 + a / v1)
    cases.append(b / v0 + c / v0 + c / v1 + b / v1 + b / v0 + b / v1)

    print(min(cases))


if __name__ == "__main__":
    main()
