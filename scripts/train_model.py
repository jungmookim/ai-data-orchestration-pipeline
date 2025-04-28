import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

def train_bitcoin_model():
    # Load the cleaned data
    if not os.path.exists('cleaned_bitcoin_prices.csv'):
        print("Cleaned data not found. Run preprocess_data.py first.")
        return

    df = pd.read_csv('cleaned_bitcoin_prices.csv')

    # Define features and target
    X = df[['day_of_week', 'day', 'month']]
    y = df['price_movement']

    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    # Save model
    model_filename = 'bitcoin_price_movement_model.pkl'
    joblib.dump(model, model_filename)
    print(f"Model trained and saved as {model_filename}")

if __name__ == "__main__":
    train_bitcoin_model()