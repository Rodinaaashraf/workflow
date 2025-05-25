import requests
import logging

logging.basicConfig(level=logging.INFO)

def extract():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    logging.info(f"Fetching data from {url}")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = extract()
    print(data[:2])

