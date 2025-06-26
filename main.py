import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.run import RunConfig

load_dotenv()

set_tracing_disabled(disabled=True)

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

# Client
external_client = AsyncOpenAI(
    api_key= OPEN_ROUTER_API_KEY,
    # Use the OpenRouter API base URL
    # This is necessary to ensure the client communicates with OpenRouter's API
    base_url="https://openrouter.ai/api/v1"
)

# Model
model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-chat-v3-0324:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
)

# Agent
Translater_Agent = Agent(
    name = "Translater_Agent",
    instructions="you are a Translater Agent. your task is Urdu language translate to English , others Languages",  # Fixed typo: Instructer → instructor
)

# Runner
result = Runner.run_sync(
    starting_agent=Translater_Agent,
    input="mara naam Uzair ghori hai or mari umar 24 saal hai or mai Pakistan se hun tanslate into german language",
    run_config=config
)

print(result.final_output)