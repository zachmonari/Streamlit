import streamlit as st
import pandas as pd
import numpy as np

st.title("My Streamlit App")
st.write("Hello World!:sunglasses:")
#markdown
st.markdown("My first **App**!")
st.header("My header")
st.subheader("My subheader")
st.badge("My badge")
st.caption("My caption")
st.code("My code")
with st.echo():
    st.write("My code is this")
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.latex("\int a x^2 \,dx")
movie=st.text_input("What is your favourite movie? ")
click=st.button("Click here")
if click:
    st.write("Your favourite movies is ", movie)

st.write("## This is a H2 heading")

"""data=pd.read_csv("mnist_test.csv")
st.write(data)
chart_data=pd.DataFrame(
    np.random.randn(30, 3),
    columns=['red', 'green', 'blue']
)
st.bar_chart(chart_data)
st.line_chart(chart_data)
"""
st.text("Dividers")
st.divider()
st.help(st.write)
st.html("<p>Foo bar.</p>")


