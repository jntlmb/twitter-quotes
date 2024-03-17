from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_quote():
    category = "computers"
    request_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    header = {'X-Api-Key': os.getenv('API_KEY_QUOTES')}

    quote_data = requests.get(request_url, header).json()
    return quote_data


def post_quote(author="foo", quote="bar"):
    pass


if __name__ == "__main__":
    quote_raw = get_quote()
    author = quote_raw[0]['author']
    quote = quote_raw[0]['quote']
    print(f"Author: {author}\nQuote: {quote}")
