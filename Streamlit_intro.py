import numpy as np
import pandas as pd
import streamlit as st

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

df=pd.read_csv("mnist_test.csv")
st.write(df)
#st.dataframe(data)
chart_data=pd.DataFrame(
    np.random.randn(30, 3),
    columns=['red', 'green', 'blue']
)
st.bar_chart(chart_data)
st.line_chart(chart_data)
st.area_chart(chart_data)
st.scatter_chart(chart_data)
#st.map(chart_data)
#st.pyplot(chart_data)
st.altair_chart(chart_data)
#st.vega_lite_chart(chart_data)
#st.plotly_chart(chart_data)
st.bokeh_chart(chart_data)
st.pydeck_chart(chart_data)
st.graphviz_chart(chart_data)

#edited=st.data_editor(DataFrame,num_rows="dynamic")

st.text("Dividers")
st.divider()
#st.help(st.write)
st.html("<p>Foo bar.</p>")
st.metric("Metrics", 43,5)



