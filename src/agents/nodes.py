import os
import sys

from langchain_core.messages import ChatMessage

sys.path.append(os.path.join(os.path.dirname(__file__), ''))
from models.llm import get_llm_model


def agent_search(state, tools):
        """
        Invokes the agent model to generate a response based on the current state. 

        Args:
            state (messages): The current state
            tools: The tools to be used by the agent

        Returns:
            dict: The updated state with the agent response appended to messages
        """
        print("---CALL AGENT RETRIEVER---")
    
        messages = state["messages"]
  
        model = get_llm_model()

        # system_message= """Você é um assistente virtual. A partir de agora responda apenas em português do Brasil."""

        
        # if not any(msg.type == "system" for msg in messages):
        #     messages = [ChatMessage(role="system", content=system_message)] + messages
        model = model.bind_tools(tools)
    
        response = model.invoke(messages)
       
        return {"messages": [response]}
