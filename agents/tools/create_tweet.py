from pytwitter import Api
from pytwitter.models.tweet import Tweet
from dotenv import load_dotenv
from os import getenv

load_dotenv()

api = Api(
    consumer_key=getenv("CONSUMER_KEY"),
    consumer_secret=getenv("CONSUMER_SECRET"),
    access_token=getenv("ACCESS_TOKEN"),
    access_secret=getenv("ACCESS_SECRET")
)

def create_tweet(text: str) -> str:
    """
    Use this tool to create a tweet

    Args:
        text (str): The text of the tweet

    Returns:
        str: Data for tweet created(JSON format).
    """
    response = api.create_tweet(text=text)
    if response is None:
        return "Error: Failed to create tweet"
    elif isinstance(response, Tweet):
        return f"Tweet created successfully: id is {response.id}"
    else:
        return "Error: Failed to create tweet"