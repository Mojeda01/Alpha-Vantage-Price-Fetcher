# AlphaVantage Stock Data Fetcher

This python script works as a simple tool for AlphaVantage, it eases the process for fetching stock market data using the API. For now, you can retrieve daily, weekly, or monthly stock prices, historical options data, quote endpoint, news and sentiment, and insider transactions.

## Features

- Fetch daily, weekly, or monthly stock prices.
- Retrieve historical options data.
- Get Quote Endpoint information.
- Fetch news and sentiment data for a stock.
- Retrieve insider transactions.

## Requirements

Install necessary dependencies by running:
    - `pip3 install -r requirements.txt`

## Command-line arguments

You can run the script with the following command-line arguments:

- `-symbol`: **(Required)** the stock symbol (e.g., AAPL,IBM, TSLA).
- `-sDaily`: Fetch daily stock prices.
- `-sWeekly`: Fetch weekly stock prices.
- `-sMonthly`: Fetch monthly stock prices.
- `-QE`: Quote Endpoint data.
- `-histOptions`: Fetch historical options data.
- `-news`: Fetch news and sentiment data.
- `insiderTrans`: Fetch insider transactions.
- `apikey`: **(Required)** the path to a file containing your AlphaVantage API key.

## Example Usages
1. **Fetch daily stock prices and global quote for Apple (AAPL):**
    ```
    python3 priceExec.py -symbol AAPL -sDaily -QE -apikey apikey.txt
    ```
2. **Fetch insider transactions for IBM:**
    ```
    python3 priceExec.py -symbol IBM -insiderTrans -apikey apikey.txt
    ```

3. **Fetch weekly stock prices and historical options for Tesla (TSLA):**
    ```
    python3 priceExec.py -symbol TSLA -sWeekly -histOptions -apikey apikey.txt
    ```

4. **Fetch monthly stock prices, news, and sentiment for Microsoft (MSFT):**
    ```
    python3 priceExec.py -symbol MSFT -sMonthly -news -apikey apikey.txt
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
