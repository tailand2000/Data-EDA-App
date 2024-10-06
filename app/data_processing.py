import pandas as pd
import streamlit as st

def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

def describe_columns(df: pd.DataFrame) -> str:
    descriptions = []
    for column in df.columns:
        col_type = df[column].dtype
        descriptions.append(f"column_name:{column},column_type:{col_type}")
    
    column_info = "-".join(descriptions)
    return column_info
