import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://testuser:testpass@db:3306/testdb")

engine = create_engine(DATABASE_URL)

st.set_page_config(page_title="SQL Data Viewer", layout="wide")

st.title("📊 SQL Data Viewer")

query = "SELECT * FROM users"
df = pd.read_sql(query, engine)

st.write("### User Data from Database")
st.dataframe(df, use_container_width=True)

# Sidebar Filters
st.sidebar.header("Filters")
name_filter = st.sidebar.text_input("Search by Name")

if name_filter:
    filtered_df = df[df["name"].str.contains(name_filter, case=False)]
    st.write("# Data")
    st.dataframe(filtered_df, use_container_width=True)
