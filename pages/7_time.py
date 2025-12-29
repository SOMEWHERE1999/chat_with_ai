import time
import streamlit as st

st.set_page_config(page_title="进度控制", page_icon="⏱️")

st.title("进度控制与状态反馈")

with st.spinner("模拟长耗时任务中..."):
    time.sleep(0.5)
st.success("初始化完成")

st.subheader("进度条示例")
progress = st.progress(0)
status_text = st.empty()
for i in range(0, 101, 10):
    progress.progress(i)
    status_text.write(f"当前进度：{i}%")
    time.sleep(0.05)

st.subheader("状态提示")
st.error("错误提示样例")
st.warning("警告提示样例")
st.info("信息提示样例")
