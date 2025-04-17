from pytwitter import Api
import os
from dotenv import load_dotenv

load_dotenv()

api = Api(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_secret=os.getenv("ACCESS_SECRET")
)

def create_tweet(text: str) -> str:
    """
    Use this tool to create a tweet

    Args:
        text (str): The text of the tweet

    Returns:
        str: The response from the create tweet
    """
    #return api.create_tweet(text=text)
    return "Tweet created"