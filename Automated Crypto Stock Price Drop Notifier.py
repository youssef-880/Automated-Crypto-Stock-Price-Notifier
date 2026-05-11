import requests  # Import the library that allows us to send HTTP requests to websites/APIs
import time      # Import the library that lets us control timing and delays (pausing the code)

# --- CONFIGURATION ---
# These are 'Constants'—values that don't change while the script is running
SYMBOL = "BTCUSDT"  # The trading pair we want to watch (Bitcoin vs US Dollar Tether)
THRESHOLD = -1.0    # The percentage drop that triggers an alert (e.g., -1.0 is a 1% drop)
INTERVAL = 60       # The amount of time (in seconds) to wait before checking the price again

def fetch_price():
    """Fetches the current price from a public API (Binance Example)."""
    # Create the specific URL needed to get data for our SYMBOL from Binance's API
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={SYMBOL}"
    
    # Send a GET request to the URL and convert the raw web response into a Python Dictionary (JSON)
    response = requests.get(url).json()
    
    # Extract the 'price' value from the dictionary and convert it from a String to a Float (decimal number)
    return float(response['price'])

def monitor():
    # Call our function to get the current price and store it as our starting point (baseline)
    last_price = fetch_price()
    
    # Print a message to the console so we know the script is actually working
    print(f"Monitoring started for {SYMBOL}. Baseline: ${last_price}")

    # Start an infinite loop so the script runs forever until you manually stop it
    while True:
        try:
            # Tell the script to "sleep" for the number of seconds defined in INTERVAL
            time.sleep(INTERVAL)
            
            # Fetch the new price after the waiting period is over
            current_price = fetch_price()
            
            # Calculate the difference: ((New - Old) / Old) * 100 gives us the percentage change
            price_change = ((current_price - last_price) / last_price) * 100
            
            # Check if the calculated change is less than or equal to our negative THRESHOLD
            if price_change <= THRESHOLD:
                # If the drop is big enough, print a warning message with the stats
                print(f"⚠️ ALERT: {SYMBOL} dropped {price_change:.2f}%! New Price: ${current_price}")
            else:
                # If the drop isn't big enough, just print a standard status update
                # The :+.2f format makes it show a '+' for gains and a '-' for losses
                print(f"Stable: {SYMBOL} is at ${current_price} ({price_change:+.2f}%)")

            # Crucial: Update 'last_price' to the 'current_price' so the NEXT loop compares against this new value
            last_price = current_price

        except Exception as e:
            # If the internet cuts out or the API is down, this prevents the script from crashing
            print(f"Error connecting to API: {e}")

# This line ensures the monitor() function only runs if this specific file is executed directly
if __name__ == "__main__":
    monitor()