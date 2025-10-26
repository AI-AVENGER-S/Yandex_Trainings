import csv


def process_cities(L):
    with open("city.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        cities = []
        for row in reader:
            try:
                geo_lat = float(row["geo_lat"])
                capital_marker = int(row["capital_marker"])
                if capital_marker == 2 and geo_lat < L:
                    city_name = row["city"]
                    population = row["population"]
                    foundation_year = row["foundation_year"]
                    cities.append((city_name, population, foundation_year))
            except (ValueError, KeyError):
                continue

    cities.sort(key=lambda x: x[0])

    for city in cities:
        print(f"{city[0]} {city[1]} {city[2]}")


L = float(input().strip())
process_cities(L)
