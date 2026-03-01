import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from typing import Dict
from google.adk.tools.agent_tool import AgentTool
#importing another agent
from investment_plan_agent.agent import investment_plan_agent

load_dotenv()

# Optional: Check if API key is loaded
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY not found in .env file")

def get_user_finance_details() -> Dict:
    # This function can be expanded to get personal finance details like salary, 
    # expense and savings caacity from the user
    return {
        "income": 50000,
        "expenses": {
            "rent": 15000,
            "utilities": 5000,
            "groceries": 8000,
            "entertainment": 2000,
            "emi": 10000
        },
        "savings_goal": 10000
    }   

finance_assistance_agent = LlmAgent(
    name="Finance_Assistance_Agent",  #FinanceAssistanceAgent - Agent name must be a valid Python identifier. no space is allowed.
    model ="gemini-2.5-flash",    
    description="An agent that provides financial assistance and advice to users.",
    instruction="You are a friendly, helpful and knowledgeable financial assistant. " \
    "You can provide advice on generic questions, budgeting, saving, investing, and other financial topics. " \
    "Always provide accurate and up-to-date information. "\
    "You have two tools to complete your tasks: 1) investment_plan_agent - use google_search tooland 2) get_user_finance_details -"
    "this tool will give you user's financial details. " \
     "Always use google_search tool when asked about:" \
    "- stock prices (ex: Tesla stock price, TSLA latest price)" \
    "- Market data, financial news or company information" \
    "- Any question containing words like latest, current, today, news, update, etc. " \
    "After searching Always provide the factual data from the search results with specific numbers and up-to-date information."\
    "Use these tools when appropriate to provide better assistance to users.",
    tools = [AgentTool(investment_plan_agent),get_user_finance_details]
)

root_agent=finance_assistance_agent