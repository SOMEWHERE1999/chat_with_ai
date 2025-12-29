import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="基础图表", page_icon="📈")

st.title("基础图表展示")

np.random.seed(42)
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["系列 A", "系列 B", "系列 C"],
)

st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)

with st.expander("数据预览"):
    st.dataframe(data)
