import streamlit as st

st.set_page_config(page_title="Pinecone 配置", page_icon="🗄️")

st.title("Pinecone 配置")
st.write("保存向量库连接信息，便于在其他页面调用。")

with st.expander("基本参数"):
    api_key = st.text_input("API Key", type="password", value=st.session_state.get("pinecone_api_key", ""))
    index_name = st.text_input("Index 名称", value=st.session_state.get("pinecone_index", "demo-index"))
    environment = st.text_input("Environment/Host", value=st.session_state.get("pinecone_env", "gcp-starter"))
    save_btn = st.button("保存配置")

if save_btn:
    st.session_state.pinecone_api_key = api_key
    st.session_state.pinecone_index = index_name
    st.session_state.pinecone_env = environment
    st.success("Pinecone 配置已保存。")

st.code(
    """
    # 使用 session_state 中的配置初始化客户端
    from pinecone import Pinecone

    pc = Pinecone(api_key=st.session_state.get("pinecone_api_key"))
    index = pc.Index(st.session_state.get("pinecone_index", "demo-index"))
    """,
    language="python",
)
