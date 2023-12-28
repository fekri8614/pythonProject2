# zoom tracker
import requests


def get_zoom_csv(api_key, api_secret):
    url = "https://api.zoom.us/v2/report/meetings"
    params = {
        "type": "past",
        "page_size": 300,
    }

    auth = (api_key, api_secret)

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        csv_file = response.json()
        return csv_file

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error occurred: {err}')

    return None


def main():
    api_key = ""
    api_secret = ""

    csv_file = get_zoom_csv(api_key, api_secret)

    if csv_file:
        print("Successfully downloaded the Zoom CSV report.")
    else:
        print("Failed to download the Zoom CSV report.")


if __name__ == '__main__':
    main()
