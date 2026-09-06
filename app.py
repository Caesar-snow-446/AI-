import streamlit as st
from google import genai

# 頁面標題與設定
st.set_page_config(page_title="AI 多功能工作助手", page_icon="🤖", layout="wide")
st.title("🤖 AI 全能工作助手")
st.caption("結合文字摘要、會議紀錄整理與信件潤飾，支援檔案上傳與成果下載！")

# 1. 側邊欄：設定 API Key 與模式選擇
with st.sidebar:
    st.header("🔑 設定與選單")
    api_key = st.text_input("輸入你的 Gemini API Key", type="password")

    st.markdown("---")
    st.header("⚙️ 工作模式設定")

    # 【擴充功能 1】：多種功能模式選擇
    mode = st.selectbox(
        "選擇 AI 處理模式：",
        ["📌 核心摘要與行動清單", "📝 會議紀錄整理", "✉️ Email 信件潤飾與生成"]
    )

    st.markdown("---")
    st.markdown("💡 **提示**：免費 API Key 可至 [Google AI Studio](https://aistudio.google.com/) 申請。")

# 2. 主介面：輸入區與檔案上傳
col1, col2 = st.columns([1, 1])

# 【擴充功能 2】：支援檔案上傳 (.txt)
uploaded_file = st.file_uploader("📂 可選：上傳 .txt 文字檔案（優先讀取檔案內容）", type=["txt"])

file_text = ""
if uploaded_file is not None:
    try:
        file_text = uploaded_file.read().decode("utf-8")
        st.success(f"已成功載入檔案：{uploaded_file.name}")
    except Exception as e:
        st.error(f"檔案讀取失敗：{e}")

# 文字輸入框（若有上傳檔案則顯示檔案內容）
user_input = st.text_area(
    "請輸入或貼上要處理的內容：",
    value=file_text if file_text else "",
    height=250,
    placeholder="在這邊貼上文字，或使用上方上傳 .txt 檔案..."
)


# 根據模式設定 Prompt 指令
def get_prompt(mode_choice, text):
    if mode_choice == "📌 核心摘要與行動清單":
        return f"""你是一個專業的高階行政助理。請分析以下文本，並以繁體中文提供：
1. 📌 **核心摘要** (3 個重點，條列式)
2. 🎯 **關鍵行動清單 (Action Items)** (如有，請寫出具體任務與執行對象)

待處理內容：
{text}"""
    elif mode_choice == "📝 會議紀錄整理":
        return f"""你是一個專業的會議紀錄整理師。請將以下會議逐字稿或雜亂筆記，整理成結構化的繁體中文會議紀錄：
1. 📅 **會議主題與重點**
2. 💡 **關鍵決議事項**
3. 📝 **待辦事項與負責人 (To-Do List)**

待處理內容：
{text}"""
    elif mode_choice == "✉️ Email 信件潤飾與生成":
        return f"""你是一個商務溝通專家。請根據以下草稿或需求，將其重寫/潤飾為一篇專業、禮貌且條理分明的繁體中文商務 Email。請包含「郵件主旨」與「正文」：

待處理內容：
{text}"""


# 3. 執行按鈕與結果顯示
if st.button("🚀 開始處理"):
    if not api_key:
        st.error("請先在左側欄位輸入你的 Gemini API Key！")
    elif not user_input.strip():
        st.warning("請先輸入內容或上傳檔案！")
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = get_prompt(mode, user_input)

            with st.spinner("AI 正在處理中，請稍候..."):
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=prompt,
                )

                # 儲存結果至 session_state，供下載按鈕使用
                st.session_state["ai_result"] = response.text
                st.success("處理完成！")

        except Exception as e:
            st.error(f"發生錯誤：{e}")

# 4. 顯示結果區與【擴充功能 3：一鍵複製 / 下載】
if "ai_result" in st.session_state:
    st.markdown("---")
    st.markdown("### 📊 AI 處理結果")

    # 顯示產出結果
    result_text = st.session_state["ai_result"]
    st.markdown(result_text)

    st.markdown("---")
    # 下載成果按鈕 (.md 檔案格式，通用且好閱讀)
    st.download_button(
        label="💾 下載結果為 Markdown (.md) 檔案",
        data=result_text,
        file_name="AI_Assistant_Result.md",
        mime="text/markdown"
    )