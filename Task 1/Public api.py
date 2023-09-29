import requests
import pandas as pd

api_url = "https://data.binance.com/api/v3/ticker/24hr"

response = requests.get(api_url)

if response.status_code == 200:

    data = response.json()
    

    df = pd.DataFrame(data)
    

    columns_to_include = ["symbol", "priceChange", "priceChangePercent", "lastPrice", "volume"]
    

    df = df[columns_to_include]
    

    df.to_csv("binance_data.csv", index=False)
    
    print("Data has been successfully saved to binance_data.csv")
else:
    print("Failed to fetch data from the API. Status code:", response.status_code)
