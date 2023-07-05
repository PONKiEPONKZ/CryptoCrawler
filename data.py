"""


Returns:
    _type_: _description_
"""
import requests
import pandas as pd
from utils.logger import logger

def collect_and_process_data():
    """
    Retrieves cryptocurrency data from the Coingecko API.
    Returns:
        pandas.DataFrame: Cryptocurrency data
    """
    api_url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',  # or whichever currency you prefer
        'per_page': 250,  # adjust as necessary
        'page': 10,  # adjust as necessary
    }
    try:
        return _extracted_from_collect_and_process_data_14(api_url, params)
    except requests.exceptions.RequestException as e:
        logger.error(f'Error retrieving data from Coingecko API: {str(e)}')
        return None


# TODO Rename this here and in `collect_and_process_data`
def _extracted_from_collect_and_process_data_14(api_url, params):
    logger.info('Sending request to Coingecko API')
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    logger.info('API response received successfully')
    data = response.json()
    logger.info('Converting API response to DataFrame')
    df = pd.DataFrame(
        data,
        columns=['id', 'name', 'symbol', 'current_price', 'high_24h', 'low_24h', 'market_cap', 'total_volume']
    )
    df.rename(
        columns={'id': 'CryptoSymbol', 'name': 'Cryptocurrency', 'current_price': 'Last Price',
                 'high_24h': 'High Price', 'low_24h': 'Low Price', 'total_volume': 'Volume'},
        inplace=True
    )
    df.fillna({'CryptoSymbol': 'N/A', 'Cryptocurrency': 'N/A', 'Last Price': 0, 'High Price': 0,
               'Low Price': 0, 'Volume': 0}, inplace=True)
    logger.info('Data processing completed successfully')
    return df
