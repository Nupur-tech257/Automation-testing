import os
import streamlit as st
import pandas as pd
import mysql.connector as conn

mydb=conn.connect(host="db",user="testuser",password="testpass")
cursor=mydb.cursor()

st.title(" SQL Data Viewer")
cursor.execute('use testdb')
query = "SELECT * FROM users"
df = pd.read_sql(query,mydb)

st.write("User Data ")
st.dataframe(df, use_container_width=True)

# Sidebar Filters
st.sidebar.header("hey")
name_filter = st.sidebar.text_input("Search by Name")

if name_filter:
    filtered_df = df[df["name"].str.contains(name_filter, case=False)]
    st.write("#  Data")
    st.dataframe(filtered_df, use_container_width=True)
