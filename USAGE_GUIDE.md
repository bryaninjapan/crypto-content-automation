# 💎 Crypto X Article Generator - 完整使用指南

## 🎯 系统已经为你准备好了！

你现在拥有一个完整的币圈 X Article 自动生成系统，**无需使用 Claude Project 的 memory 功能**。所有配置都保存在本地文件中。

---

## 🚀 三种使用方式

### 方式 1️⃣: 最简单 - 直接问 Claude（强烈推荐！）

这是最轻松的方式，Claude 会自动帮你完成一切：

#### 基础用法：
```
请帮我生成一篇关于 "Solana Restaking" 的 X Article
```

#### 进阶用法：
```
帮我生成一篇 Bitcoin L2 的文章，要包含：
1. 技术对比
2. TVL 数据
3. 投资机会

图片要突出 TVL 增长数据
```

#### 从 URL 生成：
```
基于这篇文章生成 X Article：
https://example.com/defi-report

请简化技术术语，重点放在普通投资者能理解的部分
```

#### 自动生成今日热点：
```
帮我生成今天币圈最值得关注的话题的 X Article
```

---

### 方式 2️⃣: 使用快捷脚本

进入项目目录后运行交互式脚本：

```bash
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator
./quick_generate.sh
```

然后根据提示选择：
1. 主题生成
2. URL 生成
3. 自动热点生成

或者直接命令行：
```bash
./quick_generate.sh "DeFi Yields" "Current Trends" "Risk Analysis"
```

---

### 方式 3️⃣: Python 命令行

```bash
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator

# 基础生成
python3 crypto_article_generator.py --topic "Bitcoin ETFs"

# 指定要点
python3 crypto_article_generator.py --topic "DeFi Yields" \
  --points "Current Trends" "Risk Analysis" "Best Practices"

# 从 URL（需要 Claude）
python3 crypto_article_generator.py --url "https://..."

# 自动生成（需要 Claude）
python3 crypto_article_generator.py --auto
```

---

## 📁 文件位置

### 项目文件：
```
/sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator/
├── config.json                    # 所有配置（颜色、模板、风格等）
├── generate_image.py              # 图片生成器
├── generate_content.py            # 内容生成器
├── crypto_article_generator.py   # 主程序
├── quick_generate.sh              # 快捷脚本
├── README.md                      # 详细文档
└── USAGE_GUIDE.md                 # 本文件
```

### 输出文件：
```
/sessions/funny-trusting-cori/mnt/claucowork/crypto-x-articles/
├── crypto_article_2026-02-05.png  # 图片
└── crypto_article_2026-02-05.md   # 文章
```

---

## ⚙️ 自定义配置

所有设置都在 `config.json` 文件中，无需 Claude Project！

### 修改图片配色

编辑 `config.json` 的 `color_scheme` 部分：

```json
"color_scheme": {
  "primary": ["#1e3a8a", "#3b82f6", "#60a5fa"],    // 主色调（蓝色系）
  "accent": ["#8b5cf6", "#a78bfa"],                // 强调色（紫色系）
  "background": ["#0f172a", "#1e293b"],            // 背景色（深色系）
  "text": "#f8fafc"                                 // 文字颜色
}
```

**预设配色方案：**

蓝紫科技风（当前）：
```json
"primary": ["#1e3a8a", "#3b82f6", "#60a5fa"],
"accent": ["#8b5cf6", "#a78bfa"]
```

绿金专业风：
```json
"primary": ["#065f46", "#059669", "#10b981"],
"accent": ["#d97706", "#f59e0b"]
```

红橙警示风：
```json
"primary": ["#991b1b", "#dc2626", "#f87171"],
"accent": ["#ea580c", "#fb923c"]
```

### 修改标题模板

编辑 `config.json` 的 `title_styles`：

```json
"title_styles": [
  "🚨 {topic}: What You Need to Know Right Now",
  "💡 {topic} 完全解析：从复杂到清晰",
  "📊 {topic} 数据深度分析",
  "⚡ 为什么 {topic} 比你想象的更重要"
]
```

### 修改内容风格

编辑 `config.json` 的 `content` 部分：

```json
"content": {
  "target_length": [800, 1500],              // 文章长度范围
  "tone": "professional_conversational",      // 语气风格
  "optimization_goals": [
    "impressions",                            // 优化目标
    "likes",
    "saves"
  ]
}
```

---

## 🎨 图片定制

### 修改尺寸
虽然默认是 5:2 比例，但你可以调整：

```json
"image": {
  "width": 1200,   // 改为 1200x480
  "height": 480
}
```

### 单独生成图片
```bash
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator
python3 generate_image.py simple
```

或自定义：
```python
from generate_image import CryptoImageGenerator

gen = CryptoImageGenerator()
gen.create_image(
    title="Your Title Here",
    subtitle="Subtitle",
    key_metric="+150%",
    metric_label="24H Growth"
)
```

---

## 📝 内容定制

### 单独生成内容
```bash
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator
python3 generate_content.py "Bitcoin L2" "Scaling Solutions" "Security Tradeoffs" "Future Outlook"
```

### 在 Python 中使用
```python
from generate_content import create_article_from_template

topic = "DeFi Safety"
points = ["Smart Contract Risks", "Audit Importance", "Best Practices"]

content, filepath = create_article_from_template(topic, points)
print(f"Saved to: {filepath}")
```

---

## 🤖 与 Claude 协同工作流程

### 标准工作流：

1. **你:** "帮我生成关于 EigenLayer 的 X Article"

2. **Claude 会:**
   - 🔍 搜索最新 EigenLayer 资讯
   - 📊 分析 TVL、技术特点等关键数据
   - 🖼️ 生成 5:2 比例的专业图片
   - 📝 撰写优化的文章内容
   - 🔗 提供下载链接

3. **你的工作:**
   - ✅ 审阅内容
   - ✏️ 根据需要微调
   - 🚀 发布到 X!

### 高级工作流：

**场景 1: 快速响应热点**
```
我看到 Solana 突破 $150，帮我生成一篇分析文章，
重点分析：价格驱动因素、链上数据、短期展望
```

**场景 2: 深度研究报告**
```
这是一份关于 L2 竞争格局的报告 [上传 PDF]
请帮我转换成易懂的 X Article，目标读者是
普通投资者，不要太多技术细节
```

**场景 3: 系列内容**
```
我想做一个 DeFi 安全系列，帮我生成第一篇：
"DeFi 安全基础 - 你必须知道的 5 个风险"
```

---

## 🎯 优化技巧

### 标题优化
- ✅ 使用数字："5 个关键指标"
- ✅ 制造好奇："大家都忽略的..."
- ✅ 用 emoji（1-2 个）
- ❌ 避免超过 70 字符

### 内容优化
- ✅ 短段落（2-3 句）
- ✅ 每 200-300 字一个小标题
- ✅ 包含数据和图表
- ✅ 使用列表
- ✅ 结尾提问引导互动

### 图片优化
- ✅ 一个清晰的焦点
- ✅ 高对比度文字
- ✅ 突出关键数字
- ✅ 保持简洁专业

---

## 🔄 每日自动化（可选）

如果想要每天自动生成，可以设置 cron job：

```bash
# 编辑 crontab
crontab -e

# 添加（每天早上 9 点运行）
0 9 * * * cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator && python3 crypto_article_generator.py --auto > /tmp/crypto-gen.log 2>&1
```

或者直接让 Claude 帮你设置：
```
请帮我设置每天早上 9 点自动生成币圈热点文章
```

---

## 📊 查看生成的内容

### 方式 1: 通过 Claude
```
显示我刚才生成的文章
```

### 方式 2: 命令行
```bash
# 查看最新文章
cat /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-articles/crypto_article_*.md | tail -50

# 查看所有生成的文件
ls -lh /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-articles/
```

### 方式 3: 在 Finder/文件管理器中打开
直接导航到输出文件夹查看图片和文件

---

## 🆘 常见问题

### Q: 图片中文显示乱码怎么办？
A: 编辑 `generate_image.py`，添加中文字体支持：
```python
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
```

### Q: 生成的内容太通用，如何个性化？
A: 使用更具体的提示，例如：
```
生成 Solana 文章，风格要更技术，包含：
- Firedancer 进展
- MEV 解决方案
- 生态系统对比

目标读者：有经验的 DeFi 用户
```

### Q: 如何批量生成多篇文章？
A: 让 Claude 帮你：
```
请帮我生成 5 篇文章，主题分别是：
1. Bitcoin L2
2. Ethereum Staking
3. DeFi Yields
4. NFT Market
5. AI + Crypto
```

### Q: 可以修改输出目录吗？
A: 编辑 `config.json` 的 `output.directory`

### Q: 生成速度慢怎么办？
A:
- 图片生成较快（1-2 秒）
- 内容生成取决于 Claude 的分析深度
- 如果是从 URL 生成，需要等待网页抓取

---

## 🎉 开始使用

现在你已经完全了解这个系统了！最简单的开始方式：

```
Claude，帮我生成一篇关于今天币圈最热话题的 X Article
```

就这么简单！🚀

---

## 📞 需要帮助？

随时问 Claude：
- "如何修改图片颜色？"
- "帮我生成一篇 XXX 的文章"
- "如何设置自动生成？"
- "展示配置文件的位置"

祝你创作愉快，获得大量 engagement！💎
