import streamlit as st
import pandas as pd

st.set_page_config(page_title="数据分析", page_icon="📊")

st.title("数据分析与可视化")

st.subheader("数据加载")
data = pd.DataFrame(
    {
        "产品": ["A", "B", "C", "D"],
        "销量": [120, 230, 180, 90],
        "区域": ["北区", "南区", "西区", "东区"],
    }
)
st.dataframe(data, use_container_width=True)

st.subheader("简单筛选")
region = st.selectbox("按区域筛选", ["全部"] + sorted(data["区域"].unique().tolist()))
filtered = data if region == "全部" else data[data["区域"] == region]
st.bar_chart(filtered.set_index("产品")["销量"])

st.subheader("数据统计")
st.write(filtered.describe(include="all"))
