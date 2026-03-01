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




