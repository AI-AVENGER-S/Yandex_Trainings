from requests import get


def main():
    print(get("http://127.0.0.1:5000").text)


if __name__ == "__main__":
    main()
