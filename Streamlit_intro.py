#import numpy as np
#import pandas as pd
import streamlit as st

st.logo("ZachTechs.jpg")
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
with open("ZachTechs.jpg","rb") as file:
    image = file.read()
st.download_button("Download Image",image,file_name="ZachTechs.jpg")
