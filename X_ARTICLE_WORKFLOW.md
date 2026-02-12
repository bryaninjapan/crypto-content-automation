# 📋 X Article 完整工作流程

## 標準流程：文章 + 圖片一體化

### 🎯 輸出規範（重要！）

**所有產出必須存放在:**
```
/Users/iruka/Downloads/claucowork/crypto-x-articles/
```

**檔案命名規則:**
- 文章: `{article_name}.md`
- 配圖: `{article_name}.png`
- 使用小寫、底線分隔、描述性名稱

**範例:**
```
✓ x_blue_follow_strategy_analysis.md
✓ x_blue_follow_strategy_analysis.png
✓ x_automation_warning_article.md
✓ x_automation_warning_article.png
```

---

## 🚀 快速生成指南

### 方法 1: Python 輔助工具（推薦）

**適用場景:** 文章已寫好，只需生成配圖

```bash
cd /Users/iruka/Downloads/claucowork/crypto-x-generator

python3 generate_article_image.py <文章名> "文字1" "文字2" "文字3" --highlight 0 2
```

**實際範例:**
```bash
# 範例 1: 藍V策略文章
python3 generate_article_image.py x_blue_strategy "X藍V" "互關" "真的" "有用？" --highlight 0 3

# 範例 2: 警告文章
python3 generate_article_image.py x_warning "不要用" "AI代理" "經營" "X帳號" --highlight 1 3

# 範例 3: 單行標題
python3 generate_article_image.py crypto_defi "DeFi" "風險管理" --highlight 1
```

**參數說明:**
- 第1個參數: 文章檔名（不含 .md）
- 後續參數: 要顯示的文字區塊
- `--highlight`: 後接要高亮的文字索引（從0開始）

---

### 方法 2: 互動式腳本（可選）

**適用場景:** 需要一步步設定選項

```bash
./generate_x_article_complete.sh
```

**注意:** 大多數情況下，方法 1（CLI）更快更簡單

---

### 方法 3: 直接呼叫 Python（進階）

**適用場景:** 需要完全自訂或自動化

```python
from generate_image import ThumbnailGenerator

generator = ThumbnailGenerator()

# 定義文字區塊
blocks = [
    {'text': 'X藍V', 'highlight': True, 'row': 0},
    {'text': '互關', 'highlight': False, 'row': 0},
    {'text': '真的', 'highlight': False, 'row': 1},
    {'text': '有用？', 'highlight': True, 'row': 1},
]

# 生成圖片
output_path = '/Users/iruka/Downloads/claucowork/crypto-x-articles/article_name.png'
path = generator.create_thumbnail(blocks, output_path=output_path)
print(f'✓ 已生成: {path}')
```

---

## 🎨 設計風格（YouTube Influence）

**視覺特徵:**
- 黑色背景 (#000000)
- 白色文字 (#FFFFFF)
- 橘色高亮框 (#FF8C00)

**適合主題:**
- 深度分析文章
- 警告/提醒內容
- 爭議性話題
- 數據洞察
- 策略指南

**範例應用:**
- ❌ 為什麼不該用 AI 代理
- ⚠️ 風險警告系列
- 📊 數據分析報告
- 🔥 爭議性觀點
- 💡 策略深度解析

**實作工具:** `generate_image.py` + `generate_article_image.py`

---

## 📐 圖片規格

**尺寸:** 1000 x 400 px (5:2 比例)
**格式:** PNG
**用途:** X (Twitter) 文章封面圖
**優化目標:** 在手機和桌面都清晰可讀

---

## ✅ 檢查清單

**生成文章配圖前:**
- [ ] 文章已寫好並存在 `crypto-x-articles/` 資料夾
- [ ] 檔名使用小寫和底線（如 `x_article_name.md`）
- [ ] 已確定圖片風格（YouTube / Data Viz）
- [ ] 準備好要顯示的文字（2-6個詞組，最多2行）

**生成後檢查:**
- [ ] 圖片已存在 `crypto-x-articles/` 資料夾
- [ ] 檔名與文章一致（article_name.md + article_name.png）
- [ ] 文字清晰可讀（在小尺寸下測試）
- [ ] 高亮區塊正確（關鍵詞有橘色背景）
- [ ] 整體視覺符合文章主題

---

## 🔧 故障排除

### 問題 1: 權限錯誤 (Permission Denied)

**症狀:**
```
PermissionError: [Errno 1] Operation not permitted
```

**解決方案:**
確保 Python 腳本使用完整權限執行，或手動建立輸出目錄：
```bash
mkdir -p /Users/iruka/Downloads/claucowork/crypto-x-articles
```

---

### 問題 2: 中文字型找不到

**症狀:**
```
FileNotFoundError: No Chinese font found
```

**解決方案:**
檢查 macOS 中文字型是否存在：
```bash
ls /System/Library/Fonts/*eiti*
```

如需要，安裝思源黑體或其他中文字型。

---

### 問題 3: 文字排版不理想

**症狀:** 文字太擠或太小

**解決方案:**
- 減少文字區塊數量（建議每行 2-3 個）
- 使用更短的詞組
- 調整 `row` 分配（將文字分散到兩行）

**範例調整:**

❌ 不好:
```
"為什麼" "你" "不該" "用" "AI" "代理"  # 太多區塊
```

✓ 更好:
```
"為什麼不該用" "AI代理"  # 合併為較少區塊
```

---

## 📚 相關文件

- `FRAMEWORK.md` - 完整框架和設計系統規格
- `generate_image.py` - 圖片生成核心程式
- `generate_article_image.py` - 快速輔助工具
- `generate_x_article_complete.sh` - 互動式生成腳本

---

## 🎓 最佳實踐

### 文字區塊設計

**單行佈局:** 適合短標題
```
"比特幣" "暴漲"
```

**雙行佈局:** 適合較長標題
```
Row 0: "X藍V" "互關"
Row 1: "真的" "有用？"
```

### 高亮使用原則

**高亮關鍵詞:**
- 爭議性詞彙（如 "不要用"、"警告"）
- 數據/數字（如 "90%"、"400"）
- 核心概念（如 "AI代理"、"藍V"）

**避免全高亮:** 會失去視覺重點

✓ 好的範例:
```
"不要用" [高亮:"AI代理"] "經營X帳號"
```

❌ 不好的範例:
```
[高亮:"不要用"] [高亮:"AI代理"] [高亮:"經營X帳號"]  # 太多高亮
```

---

## 📊 效果追蹤

**建議記錄:**
- 文章發布日期
- Impressions（曝光數）
- Likes（按讚數）
- Saves（收藏數）
- 圖片風格（YouTube / Data Viz）

**目標:** 根據數據優化未來的圖片設計

---

**最後更新:** 2026-02-12
**維護者:** @iruka
