from textwrap import dedent
from dotenv import load_dotenv 
from pytwitter import Api
from pytwitter.models.tweet import Tweet
from dotenv import load_dotenv
from os import getenv
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.deepseek import DeepSeekProvider

load_dotenv()

"""
    This is a tweet agent.
    You can specify other models, like OpenAI or SiliconFlow.

    ```python
    from agno.models.deepseek import DeepSeek
    from agno.models.openai import OpenAILike
    from os import getenv

    model=OpenAILike(
        id="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B", 
        api_key=getenv("SILICONFLOW_API_KEY"), 
        base_url="https://api.siliconflow.cn/v1",
    ),
    
    # model=DeepSeek(),
    ```
"""
agent = Agent(
    name="Tweet Agent",
    model=OpenAIModel(
        model_name="deepseek-chat",
        provider=DeepSeekProvider(api_key=getenv("DEEPSEEK_API_KEY"))
    ),
    system_prompt="An agent that enhances and expands user-provided text or topics before posting on X.",
    instructions=dedent("""\
        You are a tweet agent that takes user-provided text or topics, 
        enhances or expands the content, and call the appropriate tools to post a tweet.

        Attention:
        - The tweet should be in English.
        - The tweet should be concise and to the point.
        - The tweet should be engaging and interesting.
        - The tweet should be related to the user-provided text or topics.
        - The tweet content only contains the pure text, no markdown or other formatting.

        Tools:
        - create_tweet(text: str) -> str

        Finally, you should call the create_tweet tool to post the tweet.
    """),
)

api = Api(
    consumer_key=getenv("CONSUMER_KEY"),
    consumer_secret=getenv("CONSUMER_SECRET"),
    access_token=getenv("ACCESS_TOKEN"),
    access_secret=getenv("ACCESS_SECRET")
)

@agent.tool
def create_tweet(_: RunContext[None], text: str) -> str:
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
    