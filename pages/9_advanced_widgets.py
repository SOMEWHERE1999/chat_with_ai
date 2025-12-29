import streamlit as st

st.set_page_config(page_title="高级组件", page_icon="🎛️")

st.title("高级组件示例")

st.subheader("文件上传与下载")
uploaded_file = st.file_uploader("上传文件", type=["txt", "csv", "json"])
if uploaded_file:
    st.write(f"文件名：{uploaded_file.name}")
    st.download_button("下载原文件", data=uploaded_file.getvalue(), file_name=uploaded_file.name)

st.subheader("表格编辑器")
data = st.experimental_data_editor(
    [{"名称": "任务 A", "状态": "进行中"}, {"名称": "任务 B", "状态": "已完成"}],
    num_rows="dynamic",
    use_container_width=True,
)
st.write("编辑后数据：", data)

st.subheader("地图展示")
st.map(
    data={"lat": [37.7749, 34.0522], "lon": [-122.4194, -118.2437]},
    zoom=3,
)
