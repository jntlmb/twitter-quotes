from dotenv import load_dotenv
from pprint import pprint
import requests
import tweepy
import os

load_dotenv()


def get_quote():
    category = "computers"
    request_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    header = {'X-Api-Key': os.getenv('API_KEY_QUOTES')}

    quote_data = requests.get(request_url, header).json()
    return quote_data


def post_quote(author="foo", quote="bar"):
    api_key = os.getenv('API_KEY')
    api_key_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(
        api_key,
        api_key_secret
    )

    auth.set_access_token(
        access_token,
        access_token_secret
    )

    api = tweepy.API(auth)

    tweet_text = f"{quote}\n{author}"
    api.update_status(tweet_text)

if __name__ == "__main__":
    quote_raw = get_quote()
    author = quote_raw[0]['author']
    quote = quote_raw[0]['quote']
    print(f"Author: {author}\nQuote: {quote}")

    post_quote(author, quote)