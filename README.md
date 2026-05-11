# Crypto Price Monitor (Binance API Tracker)

A lightweight Python script that monitors cryptocurrency prices in real time using the Binance public API. It tracks price movement and triggers alerts when a defined percentage drop occurs.

---

# Overview

This project demonstrates:
- API integration using REST requests
- Real-time data monitoring
- Basic financial data analysis
- Loop-based automation
- Error handling for network stability

It continuously tracks the price of a selected crypto pair and calculates percentage changes over time.

---

# Features

- Live price tracking via Binance API
- Customizable trading pair (e.g., BTCUSDT)
- Percentage drop alert system
- Continuous monitoring loop
- Built-in error handling for API failures
- Simple and lightweight Python script

---

# Tech Stack

- Python 3
- Requests library
- Binance Public API

---

# How It Works

1. Fetches the current price from Binance API  
2. Stores it as a baseline price  
3. Waits for a defined interval  
4. Fetches a new price  
5. Calculates percentage change  
6. Triggers an alert if the drop exceeds the threshold  

---

# Configuration

You can customize the behavior using these variables:

```python
SYMBOL = "BTCUSDT"   # Trading pair (e.g. ETHUSDT, BTCUSDT)
THRESHOLD = -1.0     # Alert trigger percentage drop
INTERVAL = 60        # Time between checks (in seconds)
```

---

# Installation

## 1. Install Python Dependencies

```bash
pip install requests
```

---

## 2. Run the Script

```bash
python main.py
```

---

# Code Explanation

## Fetch Price Function

This function connects to Binance API and retrieves the latest price:

```python
def fetch_price():
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={SYMBOL}"
    response = requests.get(url).json()
    return float(response['price'])
```

---

## Monitoring Logic

This function continuously checks price changes and prints alerts:

```python
def monitor():
    last_price = fetch_price()
    print(f"Monitoring started for {SYMBOL}. Baseline: ${last_price}")

    while True:
        try:
            time.sleep(INTERVAL)

            current_price = fetch_price()
            price_change = ((current_price - last_price) / last_price) * 100

            if price_change <= THRESHOLD:
                print(f"⚠️ ALERT: {SYMBOL} dropped {price_change:.2f}%! New Price: ${current_price}")
            else:
                print(f"Stable: {SYMBOL} is at ${current_price} ({price_change:+.2f}%)")

            last_price = current_price

        except Exception as e:
            print(f"Error connecting to API: {e}")
```

---

## Entry Point

Ensures the script runs only when executed directly:

```python
if __name__ == "__main__":
    monitor()
```

---

# Possible Improvements

- Add Telegram or Discord alerts
- Store price history in a database
- Add multiple coin tracking
- Visual dashboard (charts with matplotlib or web UI)
- Use WebSockets instead of polling for real-time updates

---

# Disclaimer

This project is for educational purposes only and is not financial advice. Cryptocurrency trading involves risk.
```
