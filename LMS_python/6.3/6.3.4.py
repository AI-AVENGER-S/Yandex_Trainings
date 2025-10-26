from requests import get


def main():
    address, key = f"http://{input()}", input()
    print(get(address).json().get(key, "No data"))


if __name__ == "__main__":
    main()
