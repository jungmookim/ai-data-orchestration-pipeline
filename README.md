![Python Version](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

# AI Data Orchestration Pipeline: Bitcoin Price Movement Prediction
Created by Jungmoo Kim (with help from AI)

This project demonstrates an end-to-end data orchestration pipeline:

- Automated data ingestion (Bitcoin price data)
- Data preprocessing
- Model training
- Model deployment via API

---

## 📦 Project Structure

```
ai-data-orchestration-pipeline/
├── scripts/
│   ├── fetch_data.py          # Fetches Bitcoin price data
│   ├── preprocess_data.py     # Cleans and labels the data
│   ├── train_model.py          # Trains a Decision Tree model
│   └── serve_model.py          # Deploys model using FastAPI
├── bitcoin_prices_*.csv        # Raw data files
├── cleaned_bitcoin_prices.csv  # Preprocessed dataset
├── bitcoin_price_movement_model.pkl  # Trained model
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 1. Data Ingestion
- Fetches daily Bitcoin prices from the [CoinGecko API](https://www.coingecko.com/en/api).
- Saves the data as timestamped CSV files.

### 2. Data Preprocessing
- Extracts useful features (`day_of_week`, `day`, `month`).
- Labels each entry: 
  - `1` if price went up compared to previous day,
  - `0` if price went down.

### 3. Model Training
- Trains a **Decision Tree Classifier** to predict price movement.
- Saves the trained model as a `.pkl` file.

### 4. Model Deployment
- Exposes a `/predict` API endpoint using **FastAPI**.
- Accepts JSON input with day, month, day of week.

---

## 🚀 How to Run

### Set up environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Fetch new Bitcoin data
```bash
python scripts/fetch_data.py
```

### Preprocess the data
```bash
python scripts/preprocess_data.py
```

### Train the model
```bash
python scripts/train_model.py
```

### Start the API server
```bash
uvicorn scripts.serve_model:app --reload
```

Then open your browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the `/predict` endpoint.

Example input:
```json
{
  "day_of_week": 2,
  "day": 28,
  "month": 4
}
```

---

## 📈 Example API Response

Request:
```json
{
  "day_of_week": 2,
  "day": 28,
  "month": 4
}
```

Response:
```json
{
  "prediction": 1
}
```
(`1` = price up, `0` = price down)

---

## 🔥 Future Improvements

- Automate pipeline with Prefect or Airflow
- Add model performance evaluation metrics
- Dockerize the API server
- Deploy to a cloud service (AWS/GCP/Azure)

---

## 📄 License

MIT License.