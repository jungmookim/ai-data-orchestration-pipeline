import requests
import pandas as pd
import time

def fetch_bitcoin_prices():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': '1',
        'interval': 'daily'
    }
    response = requests.get(url, params=params)
    # print(response.status_code)  # <--- Add this
    # print(response.json())        # <--- Add this
    data = response.json()
    
    # Extract prices
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    filename = f"bitcoin_prices_{int(time.time())}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")

if __name__ == "__main__":
    fetch_bitcoin_prices()