import streamlit as st
import pandas as pd
from config import load_config
from data_processing import load_data, describe_columns
from code_generation import generate_code, execute_generated_code

def main():
    
    st.title("データ分析 EDAアプリ")
    st.write("可視化したcsvファイルを選択してください。")
    csv_file = st.file_uploader("カラムが1行目に存在するcsvファイルを選択してください。", type="csv")

    if csv_file:
        df = pd.read_csv(csv_file)
        st.write(df.head(5))
        column_info = describe_columns(df)

        requests = st.text_area("可視化したいことを記載してください", height=5, placeholder="例：〇〇カラムごとの平均年齢を棒グラフで可視化してください。")

        if st.button("可視化", key="submit"):
            if requests:
                generated_code = generate_code(requests, column_info)
                execute_generated_code(df, generated_code)


if __name__ == "__main__":
    # APIキー等の設定
    load_config()
    # 処理を実行
    main()