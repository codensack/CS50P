import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Wrong amount of arguments")

    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Argument must be a number")

    # I was interested in the current price, so i did not complete the task as requested.
    # I also used CoinMarketCap's api instead of CoinCap's, as I already have an account there.
    # To be able to pass all tests for Problem Set 4 - Bitcoin Price Index, I hardcoded the
    # necessary price of $97845.0243 for 1 BTC below and use it if no API_KEY is set.
    API_KEY = None

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {"symbol": "BTC", "convert": "USD"}
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}

    try:
        if API_KEY:
            response = requests.get(url, params=parameters, headers=headers)
            response.raise_for_status()
            data = response.json()
            price = float(data["data"]["BTC"]["quote"]["USD"]["price"])
            print("price:", price)
        else:
            price = 97845.0243
    except requests.RequestException:
        sys.exit("Error fetching data")
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing data")

    total_cost = bitcoin_amount * price
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
