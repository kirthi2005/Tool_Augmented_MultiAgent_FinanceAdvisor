## LLMAgent
The Finance Assistance Agent is an LLM-powered agent that helps users with personalized investment planning.
It gathers financial data from the user and generates investment recommendations by coordinating with other tools and agents.

## Workflow

The interaction between agents follows this flow:

1. User requests financial planning assistance.

2. The Finance Assistance Agent receives the request.

3. The agent calls get_user_finance_details to retrieve financial data from the database.

4. The financial data is passed to the Investment Plan Agent.

5. The Investment Plan Agent:

    1. Uses google_search to gather relevant investment insights

    2. Generates an investment strategy tailored to the user's profile.

6. The response is returned to the Finance Assistance Agent.

7. The Finance Assistance Agent provides the final investment planning advice to the user.

User Request
      │
      ▼
Finance Assistance Agent
      │
      ├── get_user_finance_details (Database)
      │
      ▼
Investment Plan Agent
      │
      └── google_search (Market insights)
      │
      ▼
Investment Strategy Generated
      │
      ▼
Final Advice Returned to User

## To run the agent
    adk web

## Error and ADK Limitations:
400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Tool use with function calling is unsupported by the model.', 'status': 'INVALID_ARGUMENT'}}

1. In tools tools = [get_user_finance_details,google_search] we cannot pass custom funcion and inbuilt tools 
together. so results in above error.

2. One agent is able to use one inbuilt tool.

## AgentTool
AgentTool class is used to pass another agent in root agent tools[].

tools = [AgentTool(investment_plan_agent),get_user_finance_details]

Give instruction about another agent to use it as tool in root agent.




