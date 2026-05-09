import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Parquet Test")

files = list(Path(".").rglob("*.parquet"))

st.write(files)

if files:

    df = pd.read_parquet(files[0])

    st.write(df.head())
