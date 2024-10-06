import os
from dotenv import load_dotenv
import openai

def load_config():
    load_dotenv()
    # lang_chainの設定
    os.environ["LANGCHAIN_API_KEY"] = os.environ.get("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = os.environ.get("LANGCHAIN_TRACING_V2")
    os.environ["LANGCHAIN_PROJECT"] = os.environ.get("LANGCHAIN_PROJECT")

def load_openai_api_key():
    load_dotenv()
    openai.api_key = os.environ.get("OPENAI_API_KEY")