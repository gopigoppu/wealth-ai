from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# Create the root agent
market_intelligence_agent = LlmAgent(
    name="market_intelligence_agent",
    model="gemini-2.5-pro",
    instruction=(
        "Fetch and summarize real-time market data using google_search_tool. "
        "Highlight actionable trends and cite all sources."
        "For any additonal info, real-time market, or external info, use google_search to retrieve web updates."
        "If no relevant content is found, Delegate to Root Agent for further assistance."
    ),
    tools=[google_search]
)
