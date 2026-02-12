# 🚀 X Article 圖片生成 - 快速參考

## ⚡ 最快速的方法

```bash
cd /Users/iruka/Downloads/claucowork/crypto-x-generator

python3 generate_article_image.py 文章名 "文字1" "文字2" "文字3" --highlight 0 2
```

**範例:**
```bash
# 警告文章
python3 generate_article_image.py x_warning "不要用" "AI代理" "經營X帳號" --highlight 1

# 策略文章
python3 generate_article_image.py x_strategy "X藍V" "互關" "有用嗎" --highlight 0
```

---

## 📁 檔案會自動存到這裡

```
/Users/iruka/Downloads/claucowork/crypto-x-articles/
```

**生成檔案:**
- `{文章名}.png` ← 配圖

**應該已存在:**
- `{文章名}.md` ← 文章本體

---

## 🎨 設計風格（當前）

**YouTube Influence 風格:**
- ⬛ 黑色背景
- ⬜ 白色文字
- 🟧 橘色高亮框

**適合:** 警告、爭議、深度分析

---

## 🎯 高亮技巧

**--highlight 後面接索引（從 0 開始）**

```bash
# "文字1" "文字2" "文字3" "文字4"
#    0       1       2       3

--highlight 0 3   # 高亮第1和第4個文字
--highlight 1     # 只高亮第2個文字
--highlight 0 1 2 # 高亮前3個（不建議太多）
```

---

## ✅ 檢查清單

生成前:
- [ ] 文章已存在 crypto-x-articles 資料夾
- [ ] 準備 2-6 個文字區塊
- [ ] 確定哪些要高亮

生成後:
- [ ] 圖片檔案已產生
- [ ] 檔名與文章一致
- [ ] 文字清晰可讀

---

## 🔧 常見問題

**Q: 文字太小怎麼辦？**
A: 減少文字區塊數量（建議每行 2-3 個）

**Q: 想要兩行排列怎麼辦？**
A: 文字超過 2 個會自動分成兩行

**Q: 生成失敗怎麼辦？**
A: 檢查文章檔案是否存在，輸出目錄權限是否正確

---

## 📚 完整文件

詳細說明請看:
- `X_ARTICLE_WORKFLOW.md` - 完整工作流程
- `FRAMEWORK.md` - 設計規格

---

**快速生成，立即發布！** 🚀
