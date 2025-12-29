import streamlit as st

st.set_page_config(page_title="交互组件", page_icon="🔄")

st.title("交互组件示例")

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.button("计数 +1", on_click=lambda: st.session_state.update(counter=st.session_state.counter + 1))
st.metric("当前计数", st.session_state.counter)

choice = st.radio("选择一个选项", ["选项 A", "选项 B", "选项 C"], horizontal=True)
st.write(f"你选择了：{choice}")

slider_value = st.slider("调整阈值", 0, 100, 50)
st.write(f"当前阈值：{slider_value}")

color = st.color_picker("选取颜色", "#FF5733")
st.write(f"选择的颜色：{color}")
