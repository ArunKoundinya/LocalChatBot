# File: chatbot_engine.py
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.prompts import PromptTemplate
import configparser

config = configparser.ConfigParser()
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
config.read('src/myagent/models_prompts.ini')

ollama_model = config.get('model', 'ollama')
context_text = config.get('botcontext', 'context')
botname = config.get('names', 'name')
username = config.get('names', 'username')

#stripspace
context_text = context_text.strip()


model = OllamaLLM(model=ollama_model)
search = DuckDuckGoSearchResults(k=3)

default_prompt = """You are my personal guide. based our chat history, you will answer my questions.
chat history: {chat_history}
user: {query}
"""
summarize_search_promt = """ Summarize your understanding {query} using these search results:
{search_results}
and 
chat_history : {chat_history}
user: {user_input}
"""

searchintent_template = PromptTemplate.from_template(
    """You are an assistant that generates concise search queries for a search engine.
Only return the actual search query string. No explanations or formatting.

User input: {user_input}

Search Query:"""
)

default_prompt_template = ChatPromptTemplate.from_template(default_prompt)
search_prompt_template = ChatPromptTemplate.from_template(summarize_search_promt)

searchintent = searchintent_template | model
search_prompt = search_prompt_template | model
no_search_prompt = default_prompt_template | model

class ChatBotEngine:
    def __init__(self):
        self.chat_history = f"{botname}:\n{context_text}\n"

    def ask(self, user_input):
        if "search" in user_input.lower():
            raw_query = searchintent.invoke({"user_input": user_input})
            query = raw_query.strip().splitlines()[-1].strip().strip('"')
            print(f"🔍 Searching for: {query}...")
            response = search_prompt.invoke({
                "query": query,
                "search_results": search.run(query),
                "chat_history": self.chat_history,
                "user_input": user_input
            })
        else:
            response = no_search_prompt.invoke({
                "chat_history": self.chat_history,
                "query": user_input
            })
        self.chat_history += f"{username}: {user_input}\n{botname}: {response}\n"
        chat_lines = self.chat_history.strip().split("\n")
        if len(chat_lines) > 10:
            self.chat_history = "\n".join(chat_lines[-10:])
        return response