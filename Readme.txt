 🤖 AI 全能工作助手 (AI Productivity Assistant)

> 一款基於 Python 與 Google Gemini API 打造的輕量化、高效能 AI 個人工作流程自動化工具。專門解決文本摘要、會議紀錄整理與商務信件潤飾等日常辦公痛點。

![專案主視覺/Demo畫面](docs/demo_screenshot.png) *(註：請將你的軟體截圖放至 docs 資料夾並替換此連結)*

---

 ✨ 核心功能 (Key Features)

- **📌 核心摘要與行動清單**：輸入長文章、新聞或報告，AI 自動提煉出 3 大核心重點與具體行動清單 (Action Items)。
- **📝 會議紀錄結構化整理**：將雜亂的會議逐字稿或筆記，快速轉化為包含「主題」、「決議事項」與「待辦 To-Do List」的標準化紀錄。
- **✉️ 商務 Email 潤飾與生成**：輸入簡短草稿，自動生成專業、禮貌且條理分明的商務郵件主旨與正文。
- **📂 本地檔案上傳**：支援拖曳或上傳 `.txt` 文字檔案，自動讀取內容並進行 AI 處理。
- **💾 一鍵匯出成果**：處理完成後，可一鍵將 AI 回應匯出為格式規範的 Markdown (`.md`) 檔案。

---

 🛠️ 使用技術 (Tech Stack)

- **主語言**：Python 3.11 / 3.12
- **前端介面 (UI)**：[Streamlit](https://streamlit.io/) (快速渲染與互動式網頁框架)
- **AI 核心 API**：[Google GenAI SDK](https://ai.google.dev/) (`gemini-3.6-flash` 模型)
- **開發工具**：PyCharm IDE

---

 🚀 快速開始 (Quick Start)

 1. 複製專案 (Clone Repository)

```bash
git clone [https://github.com/你的帳號/你的專案名稱.git](https://github.com/你的帳號/你的專案名稱.git)
cd 你的專案名稱