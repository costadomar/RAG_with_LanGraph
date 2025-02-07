import os
import sys

from langchain.schema.runnable.config import RunnableConfig
import chainlit as cl

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.rag_agent import create_rag_chain

@cl.on_chat_start
async def on_chat_start():
    
    await cl.Message(content="Olá!! Eu sou seu assistente virtual!").send()
    
    rag_chain = create_rag_chain()
    
    cl.user_session.set("runnable", rag_chain)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)
    await msg.send()
