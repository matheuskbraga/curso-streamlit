import streamlit as st
import pandas as pd

st.title("Olá Streamlit!!!")
st.markdown(
    """
    Este é um teste para ver as widget do streamlit!
    """
)

if st.button("Send ballons!"):
    st.balloons()