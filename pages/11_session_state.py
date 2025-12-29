import streamlit as st

st.set_page_config(page_title="状态管理", page_icon="💾")

st.title("Session State 状态管理")

st.write("在多页应用中共享状态，避免重复输入。")

if "notes" not in st.session_state:
    st.session_state.notes = ""

st.text_area("全局笔记", key="notes", height=150)
st.write("当前笔记内容：")
st.code(st.session_state.notes)

st.subheader("跨页变量预览")
st.json({k: v for k, v in st.session_state.items() if not k.startswith("_")})

st.info("Session State 会在页面之间保持，返回首页即可看到最新数据。")
