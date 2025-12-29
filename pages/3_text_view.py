import streamlit as st

st.set_page_config(page_title="文本和表单", page_icon="📝")

st.title("文本与表单组件")

st.subheader("文本展示")
st.write("可以使用 `st.write`、`st.markdown` 或 `st.caption` 渲染不同层级文本。")
st.markdown(
    """
    **示例 Markdown**

    - 支持粗体、斜体和代码块
    - 支持列表与引用
    > 引用内容
    """
)

st.subheader("输入表单")
with st.form("demo_form"):
    name = st.text_input("姓名")
    age = st.number_input("年龄", min_value=0, max_value=120, value=25)
    agree = st.checkbox("我已阅读条款")
    submitted = st.form_submit_button("提交")

if submitted:
    st.success(f"收到：{name}, {age} 岁, 同意条款：{agree}")
