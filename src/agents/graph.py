from langgraph.graph import END, StateGraph, START
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition


def create_workflow():

    from .nodes import agent_search as agent
    from .state import AgentState
    from .retriever import retriever_tool
    
    tools = [retriever_tool()]
    memory = MemorySaver()
    workflow = StateGraph(AgentState)
   
    workflow.add_node("agente", lambda state: agent(state, tools))  
    retriever = ToolNode(tools)
    workflow.add_node("retriever", retriever)  
    workflow.add_edge(START, "agente")

    workflow.add_conditional_edges(
        "agente",
        tools_condition,
        {
           "tools": "retriever",
            END: END,
        },
    )

    workflow.add_edge("retriever", "agente")

    graph = workflow.compile(checkpointer=memory)

    return graph
