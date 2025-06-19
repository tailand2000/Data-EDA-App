import openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import matplotlib.font_manager as fm
from datetime import datetime
import streamlit as st
import os
from config import load_openai_api_key
import pandas as pd

# OpenAIの設定
load_openai_api_key()
llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=600)
count = 0

def generate_code(requests, column_info):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "あなたはプログラマーのアシスタントです。ユーザーがしたいことをpythonコード化してコードのみ返答してください。"),
            ("user", "実行したいこと:すでに用意されているdfがあります。そのdfのカラム情報は「{column_info}」です。このdfに対して「{requests}」を実行するためのコードを実装してください。また、その時に可視化する際にはstreamlitで実行できる形にしてください。また、各ラベルが重ならないように考慮してください。そして、データフレームの例とコメントはコードには必要ありません。")
        ]
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"requests": requests, "column_info":column_info})
    # コードブロックのMarkdown記法を削除
    clean_answer = answer.replace("```python", "").replace("```", "")
    st.write(f"実行コード：\n{answer}")
    return clean_answer

def execute_generated_code(df, generated_code):
    global count
    if count <= 2:
        try:
            exec(generated_code)
        except Exception as e:
            count += 1
            print(f"コード修正：{count}回目")
            prompt = ChatPromptTemplate.from_messages(
                    [
                        ("system", "あなたはプログラマーのアシスタントです。エラー内容に従って修正したコードのみを返答してください。データの確認作業は必要なく、可視化するためのコードのみにしてください。"),
                        ("user", "修正前のコード:「{generated_code}, エラー内容：{e}")
                    ]
            )
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser
            answer = chain.invoke({"generated_code": generated_code, "e":e})
            # コードブロックのMarkdown記法を削除
            clean_answer = answer.replace("```python", "").replace("```", "")
            st.write(f"エラーが発生しました。エラー内容はこちらです。\n{e}")
            st.write("コードを修正します。")
            st.write(f"修正後コード：\n{answer}")
            execute_generated_code(df, clean_answer)
    else: 
        st.write("エラーが修正できませんでした、プロンプトを記載し直してください。")