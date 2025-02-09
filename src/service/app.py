import os
import sys

from langchain.schema.runnable.config import RunnableConfig
import chainlit as cl

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.graph import create_workflow

@cl.on_chat_start
async def on_chat_start():
    
    agent = create_workflow()
    
    cl.user_session.set("agent", agent)


@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")  

    msg = cl.Message(content="")

    async for chunk in agent.astream(
                                        {"messages": message.content},
                                        stream_mode="values",
                                        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()],
                                                                configurable={"thread_id": cl.context.session.id})
        ):
        msg_content = chunk["messages"][-1].content
    await msg.stream_token(msg_content)
