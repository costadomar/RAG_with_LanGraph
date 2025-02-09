from typing import List, TypedDict
from typing import Annotated, Sequence
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """
    Represents the state of the graph.
    Attributes:
        messages: messages
        
    """
    messages: Annotated[Sequence[BaseMessage], add_messages]
    