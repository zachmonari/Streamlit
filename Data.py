import numpy as np
import pandas as pd
import streamlit as st
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
data=pd.read_csv("mnist_test.csv")
st.download_button("Download Data",data)