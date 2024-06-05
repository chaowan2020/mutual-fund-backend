import requests
from bs4 import BeautifulSoup

def scrape_mutual_fund_data(id):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={id}&apikey=BLNLMLH5L5Z25HT7"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    if "Time Series (Daily)" not in data:
        return None

    time_series = data["Time Series (Daily)"]
    parsed_data = []

    for date, metrics in time_series.items():
        parsed_data.append({
            "date": date,
            "open": metrics["1. open"],
            "high": metrics["2. high"],
            "low": metrics["3. low"],
            "close": metrics["4. close"],
            "volume": metrics["5. volume"]
        })

    return parsed_data

def analyze_mutual_fund(id):
    data = scrape_mutual_fund_data(id)
    if not data:
        return None

    # Example analysis: calculating the average closing price
    total_close = sum(float(day["close"]) for day in data)
    average_close = total_close / len(data)

    analysis = {
        "average_close": average_close,
        "data_points": len(data)
    }

    return analysis
