import streamlit as st
from bbquote850.quotes import get_quote

btn = st.button("Get Quote!")

if btn:
  st.write("# Quote of the day 👇")
  st.write(f"### {get_quote()}")
