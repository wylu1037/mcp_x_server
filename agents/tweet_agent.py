from agno.agent import Agent
from agno.models.openai import OpenAILike
import os
from dotenv import load_dotenv
from agents.tools.create_tweet import create_tweet

load_dotenv()

agent = Agent(
    name="Tweet Agent",
    description="An agent that enhances and expands user-provided text or topics before tweeting.",
    model=OpenAILike(
        id="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B", 
        api_key=os.getenv("SILICONFLOW_API_KEY"), 
        base_url="https://api.siliconflow.cn/v1",
    ),
    tools=[create_tweet],
    instructions="You are a tweet agent that takes user-provided text or topics, enhances or expands the content, and call the appropriate tools to post a tweet.",
    show_tool_calls=True,
)
