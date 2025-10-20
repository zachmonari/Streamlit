import numpy as np
#import pandas as pd
import streamlit as st
from PIL import Image
import time
from numpy.random import default_rng as rng

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

@st.fragment
def release_the_balloons():
    st.button("Release the balloons", help="Fragment rerun")
    st.balloons()

with st.spinner("Inflating balloons..."):
    time.sleep(5)
release_the_balloons()
st.button("Inflate more balloons", help="Full rerun")
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

# vertical alignment bottom
left, middle, right=st.columns(3, vertical_alignment="bottom")
left.text_input("Write something")
click2=middle.button("Click me")
if click2:
    st.balloons()
right.checkbox("Check me")

#modal dialog
@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
#Creating forms
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")

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

# Use commands as container methods
df=rng(0).standard_normal((10,1))
col1,col2=st.columns([3,1])

col1.subheader("Column 1 with a chart")
col1.line_chart(df)

col2.subheader("Column 2 with data")
col2.write(df)

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")

left, middle,right=st.columns(3,border=True)
left.markdown("I love tech"*10)
middle.markdown("I love engineering"*8)
right.markdown("I love rice"*4)

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

flex = st.container(horizontal=True, horizontal_alignment="right")

for card in range(3):
    flex.button(f"Button {card + 1}")