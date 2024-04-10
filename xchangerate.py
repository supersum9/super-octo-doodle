"""Exchange Rate Generator"""
import requests
from datetime import datetime, timedelta

def fetch_exchange_rates(api_endpoint, api_key, base_currency, target_currency, start_date, end_date):
    """
    Fetches historical exchange rates for the given currency pair and date range

    Args:
        api_endpoint: API endpoint for exchange rate service
        api_key: API Key for exchange rate service
        base_currency: Base Currency Code AUD
        target_currency: Target Currency Code NZD
        start_date: start date in YYYY-MM-DD format
        end_date: End Date in YYYY-MM-DD format
    """

    api_url = f"{api_endpoint}/timeseries?access_key={api_key}&start_date={start_date}&end_date={end_date}&base={base_currency}&symbols={target_currency}"

    try:
        response = requests.get(api_url, timeout=120)
        response.raise_for_status()
        data = response.json()
        rates = data.get('rates', {})
        return rates
    except requests.RequestException as e:
        print(f"Failed to fetch exchange rates : {e}")
        return None


def analyze_rates(rates, target_currency):
    """
    Finds the maximum, minimum, and average rates for the time period

    Args:
        rates: Dictionary of rates
        target_currency: Target Currency code NZD
    """
    max_rate = None
    min_rate = None
    max_date = ''
    min_date = ''
    total_rate = 0
    rate_count = 0

    for date, rate_info in rates.items():
        rate = rate_info.get(target_currency)
        if rate is not None:
            total_rate += rate
            rate_count += 1
            if max_rate is None or rate > max_rate:
                max_rate = rate
                max_date = date
            if min_rate is None or rate < min_rate:
                min_rate = rate
                min_date = date

    average_rate = total_rate / rate_count if rate_count else 0
    return max_rate, min_rate, max_date, min_date, average_rate


if __name__ == "__main__":

    api_endpoint = 'http://api.exchangeratesapi.io/v1'
    api_key = 'ENTER_API_KEY'  # Replace with actual API key
    base_currency = 'AUD'
    target_currency = 'NZD'

    # Define the 30-day period

    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    exchange_rates = fetch_exchange_rates(api_endpoint, api_key, base_currency, target_currency, start_date, end_date)

    if exchange_rates is not None:
        max_rate, min_rate, max_date, min_date, avg_rate = analyze_rates(exchange_rates, target_currency)
        print(f'Maximum exchange rate for {base_currency} to {target_currency} was {max_rate} on {max_date}.')
        print(f'Maximum exchange rate for {base_currency} to {target_currency} was {min_rate} on {min_date}.')
        print(f'Average rate for {base_currency} to {target_currency} over the last 30 days was {avg_rate}.')

    else:
        print('Failed to process the exchange rates.')
