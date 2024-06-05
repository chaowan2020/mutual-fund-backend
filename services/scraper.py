import requests
from bs4 import BeautifulSoup

def scrape_mutual_fund_data(id):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={id}&apikey=79HOWNP77EIUU0RO"
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
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={id}&apikey=79HOWNP77EIUU0RO"
    r = requests.get(url)
    data = r.json()
    return data


def get_market_news_and_sentiment(tickers=None, time_from=None, time_to=None, sort="LATEST", limit=50):
    base_url = "https://www.alphavantage.co/query"
    topics = "financial_markets,finance,economy_fiscal,economy_monetary,economy_macro,real_estate,technology"

    params = {
        "function": "NEWS_SENTIMENT",
        # "topics": topics,
        "apikey": "79HOWNP77EIUU0RO",
        # "sort": sort,
        "limit": "5"
    }

    # if tickers:
    #     params["tickers"] = tickers
    # if time_from:
    #     params["time_from"] = time_from
    # if time_to:
    #     params["time_to"] = time_to

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return None

    return response.json()
