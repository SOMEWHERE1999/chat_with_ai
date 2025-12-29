import streamlit as st

st.set_page_config(page_title="布局组件", page_icon="🎨")

st.title("布局组件示例")

st.subheader("两列布局")
col1, col2 = st.columns([1, 1])
with col1:
    st.info("左侧信息框")
with col2:
    st.success("右侧成功提示")

st.subheader("选项卡")
tab1, tab2, tab3 = st.tabs(["输入", "展示", "帮助"])
with tab1:
    st.text_input("在此输入一些内容")
with tab2:
    st.write("此处展示选项卡 2 的内容")
with tab3:
    st.markdown("帮助信息或 FAQ")

st.subheader("侧边栏")
st.sidebar.radio("快捷筛选", ["全部", "进行中", "已完成"])
st.sidebar.slider("置信度", 0.0, 1.0, 0.5, 0.1)
