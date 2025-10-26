from math import dist, cos, sin


def main():
    deca = list(map(float, input().split()))
    polar = list(map(float, input().split()))
    print(
        dist(
            (deca[0], deca[1]),
            (
                polar[0] * cos(polar[1]),
                polar[0] * sin(polar[1]),
            ),
        )
    )


if __name__ == "__main__":
    main()
