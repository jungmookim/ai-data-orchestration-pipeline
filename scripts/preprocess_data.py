import pandas as pd
import os

def preprocess_bitcoin_data():
    # Find the latest raw data file
    data_files = [f for f in os.listdir('.') if f.startswith('bitcoin_prices') and f.endswith('.csv')]
    if not data_files:
        print("No bitcoin_prices CSV file found!")
        return
    
    latest_file = max(data_files, key=os.path.getctime)
    print(f"Loading {latest_file}...")

    # Load data
    df = pd.read_csv(latest_file)
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Create new features
    df['day_of_week'] = df['timestamp'].dt.dayofweek  # Monday=0, Sunday=6
    df['day'] = df['timestamp'].dt.day
    df['month'] = df['timestamp'].dt.month
    
    # Create label: 1 if price goes up compared to previous day, 0 if goes down
    df['price_shifted'] = df['price'].shift(1)
    df['price_movement'] = (df['price'] > df['price_shifted']).astype(int)
    
    # Drop any rows with NaN values created by shift()
    df = df.dropna()

    # Save cleaned data
    cleaned_filename = 'cleaned_bitcoin_prices.csv'
    df.to_csv(cleaned_filename, index=False)
    print(f"Saved cleaned dataset to {cleaned_filename}")

if __name__ == "__main__":
    preprocess_bitcoin_data()