# Chat with AI - Streamlit 多页面示例

本示例展示如何基于 Streamlit 搭建多页面的 AI 交互与组件演示应用。用户可自行准备 API 密钥，切换侧边栏的页面体验不同组件。

## 目录结构
```
├── start.py                        # 主页 - AI 聊天界面
├── README.md                       # 项目说明文档
└── pages/                          # 多页面应用目录
    ├── 1_OpenAi.py                 # OpenAI API 配置
    ├── 2_Pinecone.py               # Pinecone 配置
    ├── 3_text_view.py              # 文本和表单
    ├── 4_chart_page.py             # 基础图表
    ├── 5_layout.py                 # 布局组件
    ├── 6_reaction.py               # 交互组件
    ├── 7_time.py                   # 进度控制
    ├── 8_media_display.py          # 媒体展示
    ├── 9_advanced_widgets.py       # 高级组件
    ├── 10_data_analysis.py         # 数据分析
    └── 11_session_state.py         # 状态管理
```

## 快速开始
1. 安装依赖：
   ```bash
   pip install streamlit pandas numpy
   ```
2. 启动应用：
   ```bash
   streamlit run start.py
   ```
3. 在侧边栏切换到 **OpenAI API 配置** 或 **Pinecone 配置** 页填写密钥，即可在首页体验聊天界面或在其他页面试用组件。

## 功能概览
- **start.py**：示例聊天界面，演示 `st.chat_input` / `st.chat_message` 的会话流，并使用 Session State 存储消息。
- **配置页**：OpenAI 与 Pinecone 页面提供表单收集密钥和基础参数，保存在 Session State 中，便于后续调用。
- **组件演示**：文本、布局、交互、媒体、进度、地图、数据编辑器等常用组件均有独立页面示例。
- **数据分析页**：展示数据表、筛选与简单可视化。
- **状态管理页**：集中查看与编辑 `st.session_state`，便于理解跨页状态共享。

> 提示：本仓库仅包含前端演示逻辑，真实的 API 请求请按需补充或替换示例代码。
