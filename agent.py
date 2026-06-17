from agno.agent  import Agent 

from agno.models.openai.responses  import OpenAIResponses
from agno.models.groq import groq

from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.arxiv import ArxivTools

load_dotenv()

def build_agent():
    return Agent(
        model = OpenAIResponses(id = "gpt-4o-mini"),
        tools = [DuckDuckGoTools(), ArxivTools()],
        markdown = True,
        instructions= "You are a helpful and expert travel agant.",
        add_datetime_to_context = True
    )


openai_agent = build_agent()

openai_agent.print_response("Find recent papers on GANs and summarize them")