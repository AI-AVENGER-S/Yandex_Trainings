import requests
import json


def get_unique_strings():
    seen_responses = set()
    all_strings = set()

    while True:
        response = requests.get("http://127.0.0.1:5000/").json()
        json_str = json.dumps(response)

        if json_str in seen_responses:
            break

        seen_responses.add(json_str)

        for item in response:
            all_strings.add(item)

    sorted_strings = sorted(all_strings, key=lambda x: x.lower())
    return sorted_strings


result = get_unique_strings()
for s in result:
    print(s)
