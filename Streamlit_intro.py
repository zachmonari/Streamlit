#import numpy as np
#import pandas as pd
import streamlit as st
from PIL import Image

logo = Image.open("ZachTechs.jpg")
st.image(logo,width=150)

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

# containers
c=st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")

#columns
col1,col2=st.columns(2)
col1.write("Column 1")
col2.write("Column 2")

#modal dialog
@st.dialog("Sign up")
def reg_form():
    name=st.text_input("Enter your name")
    email=st.text_input("Enter your email")

reg_form()
#Expander
with st.expander("Open to see more"):
    st.write("More content here")

with st.popover("Settings"):
    st.checkbox("Completed")

#sidebar
st.sidebar.write("### Sidebar")
click1=st.sidebar.button("Click here")
if click1:
    st.balloons()

#Tabs
tab1,tab2=st.tabs(["Tab 1","Tab 2"])
tab1.write("This is tab 1")
tab2.write("This is tab 2")

#pages

#from St_pages import Page, show_pages,add_page_title
#show_pages([Page("Streamlit_App.py","Home",""),Page("Streamlit_App.html","Home",":memory:")])
#add_page_title("Streamlit_App.py")

#columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    with open("cat.jpg","rb") as file:
        image = file.read()
    st.image(image, width=300)
    st.download_button("Download Image",image,file_name="cat.jpg")


with col2:
    st.header("A dog")
    with open("dog.jpg","rb") as file:
        image = file.read()
    st.image(image, width=300)
    st.download_button("Download Image", image, file_name="dog.jpg")

with col3:
    st.header("An owl")
    with open("owl.jpg", "rb") as file:
        image = file.read()
    st.image(image,width=300)
    st.download_button("Download Image", image, file_name="owl.jpg")
