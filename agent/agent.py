from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit 
from llm import get_llm


def create_agent(database):
    tool_kit=SQLDatabaseToolkit(db=database)
    llm=get_llm()
    
    agent_executor=create_sql_agent(
        llm=llm,
        toolkit=tool_kit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    return agent_executor


def invoke_agent(user_input,database):
    agent_executor=create_agent(database)
    
    return agent_executor.run(user_input)