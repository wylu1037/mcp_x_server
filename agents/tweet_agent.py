from textwrap import dedent
from agno.agent import Agent
from agno.models.deepseek import DeepSeek
from agents.tools.create_tweet import create_tweet
from dotenv import load_dotenv 

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
    description="An agent that enhances and expands user-provided text or topics before tweeting.",
    model=DeepSeek(),
    tools=[create_tweet],
    instructions=dedent("""\
        You are a tweet agent that takes user-provided text or topics, 
        enhances or expands the content, and call the appropriate tools to post a tweet.
                        
        Attention:
        - The tweet should be in English.
        - The tweet should be concise and to the point.
        - The tweet should be engaging and interesting.
        - The tweet should be related to the user-provided text or topics.
        - The tweet should be no more than 280 characters.
        - The tweet content only contains the pure text, no markdown or other formatting.

        Tools:
        - create_tweet(text: str) -> str

        Finally, you should call the create_tweet tool to post the tweet.
    """),
    show_tool_calls=True
)
