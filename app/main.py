import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta
from config import load_config
from data_processing import describe_columns
from code_generation import generate_code, execute_generated_code
from session import clear_session_if_expired, update_last_interaction

SESSION_TIMEOUT_SECONDS = 300  # セッションの有効時間を5分（300秒）に設定

def main():
    # セッションタイムアウトをチェック
    clear_session_if_expired()

    st.title("データ分析 EDAアプリ")
    st.write("可視化したcsvファイルを選択してください。")
    
    # CSVファイルアップロード
    csv_file = st.file_uploader("カラムが1行目に存在するcsvファイルを選択してください。", type="csv")

    # CSVファイルがアップロードされた場合、セッションに保存し、最後の操作時間を更新
    if csv_file:
        st.session_state.csv_file = csv_file
        df = pd.read_csv(csv_file)
        st.session_state.df = df
        column_info = describe_columns(df)
        st.session_state.column_info = column_info
        update_last_interaction()  # 最後の操作時間を更新

    # セッションにCSVファイルとデータフレームがある場合
    if "df" in st.session_state:
        st.write(st.session_state.df.head(5))  # データフレームを表示
        column_info = st.session_state.column_info

        # ユーザーのリクエストを入力
        requests = st.text_area("可視化したいことを記載してください", height=5, placeholder="例：〇〇カラムごとの平均年齢を棒グラフで可視化してください。")

        # ボタンが押されたとき
        if st.button("可視化", key="submit"):
            if requests:
                st.write(f"可視化内容：\n{requests}")
                # 生成されたコードの呼び出しと実行
                generated_code = generate_code(requests, column_info)
                execute_generated_code(st.session_state.df, generated_code)
                update_last_interaction()  # 最後の操作時間を更新

if __name__ == "__main__":
    # APIキー等の設定
    load_config()
    # 処理を実行
    main()
