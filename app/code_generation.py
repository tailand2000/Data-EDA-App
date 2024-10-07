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
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=1000)

def generate_code(requests, column_info):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
             "あなたは非常に優秀なプログラマーのアシスタントです。ユーザーが指定した要件を正確にPythonコードとして生成してください。"
             "dfはすでに用意されているので、新しくdfを作成する必要はありません。"
             "コードはstreamlitで実行可能な形にしてください。"
             "可視化の際には、ラベルが重ならないように最適化し、必要に応じて `matplotlib` などのライブラリを使用してください。"
             "コードにはデータフレームの例や不要なコメントを含めないでください。"
             "コードの効率性や読みやすさを重視し、冗長な部分は避けてください。"),
            ("user", 
             "実行したいこと: 用意されているデータフレーム(df)のカラム情報は次の通りです: {column_info}。"
             "このデータフレームに対して次の操作を行いたい: {requests}。"
             "結果を可視化する際は、streamlitで実行可能なコードにしてください。"
             "また、プロットのラベルが重ならないように注意してください。"
             "必要に応じて、適切なフォントサイズやスタイルを設定してください。")
        ]
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"requests": requests, "column_info":column_info})
    # コードブロックのMarkdown記法を削除
    clean_answer = answer.replace("```python", "").replace("```", "")
    st.write(f"実行コード：\n{answer}")
    return clean_answer

def execute_generated_code(df, generated_code, count=0):
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
            code_with_font_setting = (
                answer.replace("```python", "").replace("```", "")
            )
            st.write(f"エラーが発生しました。エラー内容はこちらです。\n{e}")
            st.write("コードを修正します。")
            st.write(f"修正後コード：\n{answer}")
            execute_generated_code(df, code_with_font_setting, count)
    else: 
        st.write("エラーが修正できませんでした、プロンプトを記載し直してください。")