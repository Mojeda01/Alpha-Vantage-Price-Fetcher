import requests
import json
import csv
import argparse

def API(filename):
    try:
        with open(filename, 'r') as file:
            api_key = file.read().strip() # read and remove any extra whitespace/newlines
        return api_key
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def alpha(sDaily=False, sWeekly=False, sMonthly=False, 
          QE=False, histOptions=False, news=False, insiderTrans=False, symbol='', API_key=''):
    base_url = 'https://www.alphavantage.co/query?'

    # 1. Function to choose Daily, Weekly, or Monthly prices
    if sDaily:
        function_type = 'TIME_SERIES_DAILY'
        filename = f'{symbol}_daily_data.csv'
    elif sWeekly:
        function_type = 'TIME_SERIES_WEEKLY'
        filename = f'{symbol}_weekly_data.csv'
    elif sMonthly:
        function_type = 'TIME_SERIES_MONTHLY'
        filename = f'{symbol}_monthly_data.csv'

    if sDaily or sWeekly or sMonthly:
        params = {
            'function': function_type,
            'symbol': symbol,
            'apikey': API_key
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        # 2. Save price data as CSV
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in data.items():
                writer.writerow([key, value])

    # 3. Historical options
    if histOptions:
        options_url = f'{base_url}function=HISTORICAL_OPTIONS&symbol={symbol}&apikey={API_key}'
        response = requests.get(options_url)
        options_data = response.json()
        with open(f'{symbol}_historical_options.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in options_data.items():
                writer.writerow([key, value])

    # 4. QE (Quote Endpoint)
    if QE:
        QE_url = f'{base_url}function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_key}'
        response = requests.get(QE_url)
        QE_data = response.json()
        with open(f'{symbol}_QE.json', 'w') as json_file:
            json.dump(QE_data, json_file, indent=4)

    # 5. News and Sentiment
    if news:
        news_url = f'{base_url}function=NEWS_SENTIMENT&tickers={symbol}&apikey={API_key}'
        response = requests.get(news_url)
        news_data = response.json()
        with open(f'{symbol}_news.json', 'w') as json_file:
            json.dumps(news_data, json_file, indent=4)

    # 6. Insider Transactions
    if insiderTrans:
        insider_url = f'{base_url}function=INSIDER_TRANSACTIONS&symbol={symbol}&apikey={API_key}'
        response = requests.get(insider_url)
        insider_data = response.json()
        with open(f'{symbol}_insider_transactions.json', 'w') as json_file:
            json.dump(insider_data, json_file, indent=4)

# Command-line argument parsing setup
def main():
    parser = argparse.ArgumentParser(description='Fetch stock data using AlphaVantage API.')

    parser.add_argument('-symbol', type=str, required=True, help='The stock symbol (e.g., AAPL, IBM).')
    parser.add_argument('-sDaily', action='store_true', help='Fetch daily stock prices.')
    parser.add_argument('-sWeekly', action='store_true', help='Fetch weekly stock prices.')
    parser.add_argument('-sMonthly', action='store_true', help='Fetch monthly stock prices.')
    parser.add_argument('-QE', action='store_true', help='Fetch Quote Endpoint (QE) data')
    parser.add_argument('-histOptions', action='store_true', help='Fetch historical options data')
    parser.add_argument('-news', action='store_true', help='Fetch news and sentiment data')
    parser.add_argument('-insiderTrans', action='store_true', help='Fetch insider transactions data')
    parser.add_argument('-apikey', type=str, required=True, help='Path to the file containing the Alphavantage API key')

    args = parser.parse_args()

    # Retrieve the API key from the provided file
    api_key = API(args.apikey)

    # Call the alpha function with parsed command-line arguments
    alpha(sDaily=args.sDaily, sWeekly=args.sWeekly, sMonthly=args.sMonthly, QE=args.QE, 
          histOptions=args.histOptions, news=args.news, insiderTrans=args.insiderTrans, 
          symbol=args.symbol, API_key=api_key)

if __name__ == '__main__':
    main()
