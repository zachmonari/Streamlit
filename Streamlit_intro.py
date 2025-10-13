import streamlit as st
import pandas as pd

st.write("Hello World!")

movie=st.text_input("What is your favourite movie? ")
click=st.button("Click here")
if click:
    st.write("Your favourite movies is ", movie)

st.write("## This is a H2 heading")

data=pd.read_csv("mnist_test.csv")
st.write(data)