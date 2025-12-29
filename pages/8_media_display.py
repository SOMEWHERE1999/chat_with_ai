import streamlit as st

st.set_page_config(page_title="媒体展示", page_icon="🎬")

st.title("媒体展示示例")

st.subheader("图片展示")
st.image(
    "https://images.unsplash.com/photo-1522199755839-a2bacb67c546?auto=format&fit=crop&w=800&q=80",
    caption="示例图片 - 工作空间",
    use_column_width=True,
)

st.subheader("音频播放")
st.audio(
    "https://file-examples.com/storage/fe5ed0c4b44fc743c7f2d6c/2017/11/file_example_MP3_700KB.mp3",
    format="audio/mp3",
)

st.subheader("视频播放")
st.video(
    "https://www.w3schools.com/html/mov_bbb.mp4",
)
