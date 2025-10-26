from math import comb


def main():
    n, m = map(int, input().split())
    print(comb(n, m) * m // n, comb(n, m))


if __name__ == "__main__":
    main()
