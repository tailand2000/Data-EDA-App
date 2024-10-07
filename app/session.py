import streamlit as st
import datetime

def clear_session_if_expired():
    if "last_interaction" in st.session_state:
        # 現在の時間と最後の操作時間の差を計算
        time_elapsed = datetime.now() - st.session_state.last_interaction
        # 5分以上経過している場合、セッションをクリア
        if time_elapsed.total_seconds() > SESSION_TIMEOUT_SECONDS:
            st.session_state.clear()
            st.write("セッションがタイムアウトしました。再度ファイルをアップロードしてください。")

def update_last_interaction():
    # 現在の時間をセッションに保存
    st.session_state.last_interaction = datetime.now()