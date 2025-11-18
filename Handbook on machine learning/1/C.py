import pandas as pd

base = '/home/avalur/autohw/'
data = pd.read_csv(base + 'organisations.csv')

def filter_restaurants(df):
    filtered_df = df[
        df['average_bill'].notna() & 
        (df['average_bill'] <= 2500)
    ]
    return filtered_df

filtered_data = filter_restaurants(data)

print(len(filtered_data))