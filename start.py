import streamlit as st
from openai import OpenAI


def get_client() -> OpenAI | None:
    api_key = st.session_state.get("openai_api_key")
    base_url = st.session_state.get("openai_base_url") or None
    if not api_key:
        return None
    return OpenAI(api_key=api_key, base_url=base_url)


st.set_page_config(page_title="AI Chat Playground", page_icon="🤖", layout="wide")

st.title("AI Chat Playground")
st.caption("体验多页 Streamlit 应用，右侧导航可切换组件示例。API 凭证请在相关页面自行配置。")

with st.sidebar:
    st.header("使用说明")
    st.markdown(
        """
        1. 在 “OpenAI API 配置” 页面填写密钥、模型与 Base URL。
        2. 返回本页即可与模型对话，支持连续对话与温度调节。
        3. 遇到错误会在提示框中展示，便于排查。
        """
    )
    st.divider()
    st.session_state.temperature = st.slider(
        "回答随机性 (temperature)", 0.0, 1.5, st.session_state.get("temperature", 0.7), 0.1
    )
    if st.button("🧹 清空对话"):
        st.session_state.messages = []
        st.toast("已清空对话历史")

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

    client = get_client()
    if not client:
        warning = "请先在左侧导航的 “OpenAI API 配置” 页填写 API Key。"
        st.warning(warning)
        st.session_state.messages.append({"role": "assistant", "content": warning})
    else:
        with st.chat_message("assistant"):
            status = st.status("正在向大模型提问…", expanded=True)
            try:
                completion = client.chat.completions.create(
                    model=st.session_state.get("openai_model", "gpt-4o-mini"),
                    temperature=st.session_state.temperature,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                )
                reply = completion.choices[0].message.content or "(无返回内容)"
                st.write(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
                status.update(label="回答已返回", state="complete", expanded=False)
            except Exception as exc:  # noqa: BLE001
                error_msg = f"调用大模型接口出错：{exc}"
                status.update(label="请求失败", state="error", expanded=True)
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

st.info("欢迎体验，所有 API 调用请在对应配置页填入密钥或自定义逻辑。", icon="ℹ️")
