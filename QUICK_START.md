# ⚡ 快速开始 - 30 秒上手

## 🎯 最简单的用法（推荐）

直接在 Claude 中说：

```
请帮我生成一篇关于 "[你的主题]" 的 X Article
```

**就这么简单！** Claude 会自动：
- 🔍 研究主题
- 📊 分析数据
- 🖼️ 生成图片（5:2 比例）
- 📝 撰写文章（X Article 格式）
- 🔗 提供下载链接

---

## 📝 示例命令

### 基础用法
```
生成一篇关于 "Solana Restaking" 的文章
```

### 指定要点
```
生成 Bitcoin L2 文章，包含：
1. 技术对比
2. TVL 数据
3. 投资机会
```

### 从 URL 生成
```
基于这篇文章生成 X Article：
https://example.com/crypto-report
```

### 今日热点
```
生成今天币圈最热的话题的文章
```

---

## 📁 文件位置

**项目目录：**
```
/sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator/
```

**输出目录：**
```
/sessions/funny-trusting-cori/mnt/claucowork/crypto-x-articles/
```

**配置文件：**
```
/sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator/config.json
```

---

## ⚙️ 快速定制

### 修改图片颜色
编辑 `config.json`，找到 `color_scheme`：
```json
"primary": ["#颜色1", "#颜色2", "#颜色3"]
```

### 修改标题风格
编辑 `config.json`，找到 `title_styles`：
```json
"title_styles": [
  "🚨 {topic}: 你现在需要知道的",
  "💡 {topic} 完全解析"
]
```

### 修改文章长度
编辑 `config.json`，找到 `target_length`：
```json
"target_length": [800, 1500]  // 改为你想要的范围
```

---

## 🎨 预设配色方案

在 `config.json` 中替换 `color_scheme`：

**蓝紫科技风（当前）：**
```json
"primary": ["#1e3a8a", "#3b82f6", "#60a5fa"],
"accent": ["#8b5cf6", "#a78bfa"]
```

**绿金专业风：**
```json
"primary": ["#065f46", "#059669", "#10b981"],
"accent": ["#d97706", "#f59e0b"]
```

**红橙警示风：**
```json
"primary": ["#991b1b", "#dc2626", "#f87171"],
"accent": ["#ea580c", "#fb923c"]
```

---

## 🚀 命令行使用

```bash
# 进入项目目录
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator

# 使用快捷脚本（交互式）
./quick_generate.sh

# 或直接指定主题
./quick_generate.sh "DeFi Yields" "Current Trends" "Risk Analysis"

# 使用 Python
python3 crypto_article_generator.py --topic "Bitcoin ETFs" \
  --points "Institutional Adoption" "Market Impact"
```

---

## 📊 生成的文件

每次运行会生成两个文件：

1. **图片**：`crypto_article_YYYY-MM-DD.png`
   - 5:2 比例（1000x400px）
   - 数据可视化风格
   - 专业配色

2. **文章**：`crypto_article_YYYY-MM-DD.md`
   - Markdown 格式
   - X Article 优化
   - 800-1500 字

---

## 💡 最佳实践

### 获得最佳效果的技巧：

1. **明确主题** - 越具体越好
   ❌ "写篇加密货币的文章"
   ✅ "分析 Solana 生态的 DeFi TVL 增长"

2. **指定要点** - 告诉 Claude 你想涵盖什么
   ```
   生成 EigenLayer 文章，包含：
   - Restaking 机制
   - 安全风险
   - 收益对比
   ```

3. **指定受众** - 让内容更精准
   ```
   给 DeFi 新手写篇关于 Yield Farming 的文章
   ```

4. **提供数据** - 如果有具体数据更好
   ```
   生成 Bitcoin 文章，突出这些数据：
   - ETF 净流入 $2.5B
   - 24H 交易量 +45%
   ```

---

## 🆘 遇到问题？

直接问 Claude：

- "配置文件在哪里？"
- "如何修改图片颜色？"
- "帮我生成今天的热点文章"
- "文章太长了，如何缩短？"

---

## 🎯 现在就开始

在 Claude 中输入：

```
请帮我生成一篇关于今天币圈最热话题的 X Article
```

就这么简单！🚀

---

**详细文档：**
- 📖 完整使用指南：`USAGE_GUIDE.md`
- 📚 项目说明：`README.md`
- ⚙️ 配置文件：`config.json`
