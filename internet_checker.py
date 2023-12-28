import requests
from requests.exceptions import ConnectionError


def is_internet_connected() -> bool:
    url = 'https://google.com'
    print(f'Attempting to connect to {url} to determine internet connection status.')

    try:
        print(url)
        resp = requests.get(url=url, timeout=10)
        resp.text
        resp.status_code
        print(f'Connection to {url} was successful.')
        return True
    except ConnectionError as e:
        requests.ConnectionError
        print(f'Failed to connect to {url}.')
        return False
    except:
        print(f'Failed with unparsed reason.')
        return False
