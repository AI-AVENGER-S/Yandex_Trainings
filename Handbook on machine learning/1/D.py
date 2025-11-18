import pandas as pd

data = pd.read_csv('organisations.csv')

data['average_bill'] = pd.to_numeric(data['average_bill'], errors='coerce')

def filter_restaurants(df):
    filtered_df = df[
        df['average_bill'].notna() & 
        (df['average_bill'] <= 2500)
    ]
    return filtered_df

data = filter_restaurants(data)

cafe_data = data[
    data['rubrics_id'].astype(str).str.contains(r'\b30774\b', regex=True) & 
    (data['city'].isin(['msk', 'spb']))
]

city_means = cafe_data.groupby('city')['average_bill'].mean()

result = round(city_means['msk'] - city_means['spb'])

print(result)