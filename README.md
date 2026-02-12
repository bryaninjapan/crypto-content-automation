# 🚀 X Article Generator

自動生成高質量 X (Twitter) Article 內容，包含專業圖片和優化文案。適用於任何主題。

## ⚡ 快速生成圖片（最常用）

```bash
# 為現有文章生成配圖
python3 generate_article_image.py 文章名 "文字1" "文字2" --highlight 0

# 範例
python3 generate_article_image.py x_strategy "X藍V" "互關" "有用嗎" --highlight 0
```

**📁 自動存到:** `/Users/iruka/Downloads/claucowork/crypto-x-articles/`

**📖 詳細文檔:**
- [X Article 完整工作流程](X_ARTICLE_WORKFLOW.md) ← 必讀
- [圖片生成快速參考](QUICK_REFERENCE_圖片生成.md)
- [設計規格與框架](FRAMEWORK.md)

---

## 📋 功能特點

- ✅ **5:2 比例圖片生成** - YouTube Influence 風格，黑底橘色高亮
- ✅ **X Article 格式優化** - 專為增加 impressions、likes 和 saves 設計
- ✅ **通用主題支援** - 不限制特定領域，適用任何主題
- ✅ **完全可定製** - 通過 config.json 調整所有設置
- ✅ **簡單易用** - 一行命令生成專業封面圖

## 🧠 生成框架

本項目遵循標準化的 4 階段生成框架：
- **Phase 1: Discovery** - 深入理解需求，挑戰假設
- **Phase 2: Planning** - 明確版本計劃，預估複雜度
- **Phase 3: Writing** - 透明化執行過程，問題導向
- **Phase 4: Polishing** - 人性化口吻優化，提升互動

👉 詳見 [FRAMEWORK.md](FRAMEWORK.md)

---

## 🎯 使用方式

### 圖片生成（主要功能）

```bash
# 基本用法
python3 generate_article_image.py 文章名 "文字1" "文字2" --highlight 0

# 範例：策略分析
python3 generate_article_image.py strategy_guide "策略" "指南" "2026" --highlight 0

# 範例：警告文章
python3 generate_article_image.py ai_warning "不要用" "AI工具" "的原因" --highlight 1

# 範例：數據報告
python3 generate_article_image.py market_report "市場" "分析" "報告" --highlight 0 2
```

**輸出位置:** 自動存到 `/Users/iruka/Downloads/claucowork/crypto-x-articles/`

## 📁 專案結構

```
crypto-x-generator/
├── config.json                    # 配置文件
├── generate_image.py              # 核心圖片生成引擎
├── generate_article_image.py      # CLI 包裝工具
├── FRAMEWORK.md                   # 設計規範與框架
├── X_ARTICLE_WORKFLOW.md          # 完整工作流程
├── QUICK_REFERENCE_圖片生成.md    # 快速參考
├── README.md                      # 本文件
└── 對話存檔/                      # 對話歷史存檔
```

**輸出目錄:** `/Users/iruka/Downloads/claucowork/crypto-x-articles/`

## ⚙️ 配置說明

編輯 `config.json` 自定義設置：

### 圖片設置（YouTube Influence 風格）
```json
"image": {
  "ratio": "5:2",
  "width": 1000,
  "height": 400,
  "style": "bold_text_thumbnail",
  "color_scheme": {
    "background": "#000000",      // 黑色背景
    "text": "#FFFFFF",            // 白色文字
    "highlight_bg": "#FF8C00",    // 橘色高亮框
    "highlight_text": "#FFFFFF"  // 高亮文字顏色
  }
}
```

### 內容設置
```json
"content": {
  "language": "zh-CN",
  "target_length": [800, 1500],
  "tone": "professional_conversational",
  "optimization_goals": ["impressions", "likes", "saves"]
}
```

## 💡 使用場景

### 場景 1: 文章封面圖生成
為已撰寫的 X Article 快速生成專業封面圖

### 場景 2: 系列內容視覺統一
為系列文章創建風格一致的封面圖

### 場景 3: 主題分析報告
為深度分析、數據報告生成醒目的封面

### 場景 4: 警告/提醒內容
為重要提醒、風險警告生成高對比度封面

## 🎨 圖片風格

**YouTube Influence 風格**（當前實作）:
- ⬛ 黑色背景 - 高對比度
- ⬜ 白色文字 - 清晰易讀
- 🟧 橘色高亮 - 突出關鍵詞
- 📐 自動排版 - 最佳化字體大小

## 🔧 進階用法

### 自定義顏色

編輯 `config.json` 中的 `color_scheme`：

```json
"color_scheme": {
  "background": "#000000",      // 背景色
  "text": "#FFFFFF",            // 文字顏色
  "highlight_bg": "#FF8C00",    // 高亮框顏色
  "highlight_text": "#FFFFFF"  // 高亮文字顏色
}
```

### 文字排版技巧

**單行排列（2-3個詞組）:**
```bash
python3 generate_article_image.py article "主標題" "副標題"
```

**雙行排列（4-6個詞組）:**
```bash
python3 generate_article_image.py article "第一行" "文字" "第二行" "文字"
```

**高亮策略:**
- 關鍵詞：核心概念、品牌名稱
- 數據：百分比、數字、統計
- 動作：行動呼籲、警告詞

## 📚 相關文檔

- **[FRAMEWORK.md](FRAMEWORK.md)** - 設計規範與 4 階段生成框架
- **[X_ARTICLE_WORKFLOW.md](X_ARTICLE_WORKFLOW.md)** - 完整工作流程與故障排除
- **[QUICK_REFERENCE_圖片生成.md](QUICK_REFERENCE_圖片生成.md)** - 快速參考速查表

## 📋 對話存檔

每次對話結束時，可以請求生成對話存檔：

```
請幫我總結這次對話，生成存檔文檔
```

存檔會自動保存到 `對話存檔/` 資料夾，格式：`YYYY-MM-DD_描述.md`

**詳見 FRAMEWORK.md 中的「Conversation Archiving Workflow」章節。**

## 🎯 快速開始（新 Agent）

如果你是新的 AI Agent，只需：

1. **閱讀 2 個文檔**（5 分鐘）:
   - `FRAMEWORK.md` - 理解設計哲學
   - `generate_article_image.py` 的 docstring - 看懂工具用法

2. **執行一個命令**:
   ```bash
   python3 generate_article_image.py test "測試" "圖片" --highlight 0
   ```

3. **完成！** 你已經可以開始生成圖片了。

---

## 💡 設計原則

生成的圖片針對以下目標優化：

- **可讀性** - 在手機和桌面都清晰
- **吸引力** - 高對比度黑橘配色
- **專業度** - 自動字體大小調整
- **一致性** - 統一的視覺風格

## 🎓 最佳實踐

### 文字設計
1. **簡潔為王** - 每行 2-3 個詞組
2. **善用高亮** - 只高亮關鍵詞（1-2 個）
3. **雙行排版** - 較長標題分成兩行

### 高亮策略
- 核心概念、品牌名稱
- 數據、百分比、統計
- 警告詞、行動呼籲

## ❓ 常見問題

**Q: 圖片尺寸可以調整嗎？**  
A: 可以！編輯 `config.json` 中的 `width` 和 `height`

**Q: 可以改變顏色嗎？**  
A: 可以！編輯 `config.json` 中的 `color_scheme`

**Q: 支援其他語言嗎？**  
A: 支援！只要系統有對應的中文字型

**Q: 如何批量生成？**  
A: 使用 Shell 腳本循環調用命令

---

## 🎉 開始創作！

現在你已經了解了所有功能，可以開始為你的 X Article 生成專業封面圖了！

**記住：好的視覺設計能讓你的內容脫穎而出。** 🚀
