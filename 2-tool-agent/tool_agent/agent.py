from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description = "Tool agent",
    instruction= """
    You are a helpful and friendly agent that assists the user very eficiently and effectively by using the tool - google_search.""",
    tools=[google_search],
)