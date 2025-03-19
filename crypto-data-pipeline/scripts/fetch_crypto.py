import requests
import psycopg2
from datetime import datetime

# PostgreSQL Database Connection
conn = psycopg2.connect(
    dbname="crypto_db",
    user="user",
    password="user",
    host="postgres_db",  # Use 'localhost' if running locally without Docker
    port="5432"
)
cursor = conn.cursor()

# CoinGecko API URL
URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

def fetch_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Check for errors

        data = response.json()

        # Extract Bitcoin & Ethereum prices
        btc_price = data.get("bitcoin", {}).get("usd")
        eth_price = data.get("ethereum", {}).get("usd")
        timestamp = datetime.utcnow()

        if btc_price and eth_price:
            cursor.execute(
                "INSERT INTO crypto_prices (symbol, price, timestamp) VALUES (%s, %s, %s), (%s, %s, %s)",
                ("BTC", btc_price, timestamp, "ETH", eth_price, timestamp)
            )
            conn.commit()
            print(f"Data inserted: BTC - ${btc_price}, ETH - ${eth_price}")

        else:
            print("Error: Could not fetch prices!")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    fetch_data()
