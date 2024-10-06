import os
from dotenv import load_dotenv
import openai
import streamlit as st

def load_config():
    load_dotenv()
    # lang_chainの設定
    os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
    os.environ["LANGCHAIN_TRACING_V2"] = st.secrets["LANGCHAIN_TRACING_V2"]
    os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]

def load_openai_api_key():
    openai.api_key = st.secrets["OPENAI_API_KEY"]