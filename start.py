import streamlit as st

st.set_page_config(page_title="AI Chat Playground", page_icon="🤖", layout="wide")

st.title("AI Chat Playground")
st.caption("体验多页 Streamlit 应用，右侧导航可切换组件示例。API 凭证请在相关页面自行配置。")

with st.sidebar:
    st.header("使用说明")
    st.markdown(
        """
        1. 在 “OpenAI API 配置” 或其他数据源配置页填写密钥。
        2. 返回本页即可与模型对话，消息会存入 Session State。
        3. 参考其他页面了解常用 UI 组件与布局写法。
        """
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("输入你的问题或指令…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    reply = "这里是示例回复。接入真实接口后即可返回模型输出。"
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

st.info("欢迎体验，所有 API 调用请在对应配置页填入密钥或自定义逻辑。", icon="ℹ️")
