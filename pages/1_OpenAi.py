import streamlit as st

st.set_page_config(page_title="OpenAI API 配置", page_icon="🤖")

st.title("OpenAI API 配置")
st.write("在此录入 OpenAI API 相关信息。")

with st.form("openai_form"):
    api_key = st.text_input("API Key", type="password", value=st.session_state.get("openai_api_key", ""))
    model = st.text_input("模型名称", value=st.session_state.get("openai_model", "gpt-4o-mini"))
    base_url = st.text_input("Base URL", value=st.session_state.get("openai_base_url", "https://api.openai.com/v1"))
    submitted = st.form_submit_button("保存配置")

if submitted:
    st.session_state.openai_api_key = api_key
    st.session_state.openai_model = model
    st.session_state.openai_base_url = base_url
    st.success("OpenAI 配置已保存到 Session State。")

st.code(
    """
    import openai

    client = openai.OpenAI(api_key=st.session_state.get("openai_api_key"))
    response = client.chat.completions.create(
        model=st.session_state.get("openai_model", "gpt-4o-mini"),
        messages=[{"role": "user", "content": "Hello"}],
    )
    """,
    language="python",
)
