# 🚀 Crypto X Article Generator

自动生成高质量币圈 X Article 内容，包含专业图片和优化文案。

## 📋 功能特点

- ✅ **5:2 比例图片生成** - 数据可视化风格，专业美观
- ✅ **X Article 格式优化** - 专为增加 impression、likes 和 saves 设计
- ✅ **多种输入方式** - 支持主题、URL、文件上传、自动搜索
- ✅ **完全可定制** - 通过 config.json 调整所有设置
- ✅ **无需 Claude Project** - 使用本地配置文件系统

## 🧠 生成框架 (New!)

本项目遵循一套标准化的生成框架，以确保质量和沟通效率：
- **Phase 1: Discovery** - 深入理解需求，挑战假设
- **Phase 2: Planning** - 明确版本计划，预估复杂度，列出大纲
- **Phase 3: Writing** - 透明化执行过程，遇到问题提供选项
- **Phase 4: Polishing** - 人性化口吻优化，增加互动诱因选项

👉 详见 [FRAMEWORK.md](FRAMEWORK.md)

## 🎯 快速开始

### 方法 1: 直接用 Claude（推荐）

最简单的方式是直接告诉 Claude 你想要什么：

```
请帮我生成一篇关于"Bitcoin ETFs"的 X Article
```

或者：

```
请基于这个链接生成 X Article: [URL]
```

### 方法 2: 命令行使用

```bash
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator

# 从主题生成
python crypto_article_generator.py --topic "DeFi Yields" --points "Current Trends" "Risk Analysis" "Opportunities"

# 从 URL 生成（需要 Claude 协助）
python crypto_article_generator.py --url "https://example.com/crypto-report"

# 自动生成今日热点（需要 Claude 协助）
python crypto_article_generator.py --auto
```

## 📁 项目结构

```
crypto-x-generator/
├── config.json                    # 配置文件（风格、模板等）
├── generate_image.py              # 图片生成器
├── generate_content.py            # 内容生成器
├── crypto_article_generator.py   # 主执行脚本
├── README.md                      # 本文件
└── quick_generate.sh              # 快捷脚本
```

输出目录：`/sessions/funny-trusting-cori/mnt/claucowork/crypto-x-articles/`

## ⚙️ 配置说明

编辑 `config.json` 来自定义：

### 图片设置
```json
"image": {
  "ratio": "5:2",
  "width": 1000,
  "height": 400,
  "style": "data_visualization",
  "color_scheme": {
    "primary": ["#1e3a8a", "#3b82f6", "#60a5fa"],
    "accent": ["#8b5cf6", "#a78bfa"]
  }
}
```

### 内容设置
```json
"content": {
  "target_length": [800, 1500],
  "tone": "professional_conversational",
  "optimization_goals": ["impressions", "likes", "saves"]
}
```

## 💡 使用场景

### 场景 1: 每日自动生成
每天早上 9 点自动生成当日币圈热点文章（需要配置 cron）

### 场景 2: 快速响应热点
看到重要新闻后，立即生成深度分析文章

### 场景 3: 报告转文章
将复杂的研究报告转换为易懂的 X Article

### 场景 4: 系列内容
针对特定叙事（如 DeFi、NFT、L2）创建系列文章

## 🎨 图片风格示例

**数据可视化风格** (当前配置):
- 清晰的渐变背景
- 突出的关键指标
- 简洁的图表元素
- 专业的字体排版

## 📝 内容优化技巧

生成的内容已经优化了以下方面：

1. **标题吸引力** - 使用数字、emoji、制造好奇心
2. **开头钩子** - 2-3 句话抓住注意力
3. **结构清晰** - 小标题、短段落、列表
4. **可扫描性** - 方便快速浏览的格式
5. **行动号召** - 结尾的思考问题

## 🔧 高级用法

### 自定义标题风格

编辑 `config.json` 中的 `content_templates.title_styles`：

```json
"title_styles": [
  "🚨 {topic}: What You Need to Know Right Now",
  "💡 The {topic} Narrative: A Complete Breakdown"
]
```

### 自定义开场白

编辑 `config.json` 中的 `content_templates.hooks`：

```json
"hooks": [
  "Let's talk about something that's been flying under the radar...",
  "If you've been confused about {topic}, you're not alone."
]
```

## 🤖 与 Claude 配合使用

### 推荐工作流程：

1. **告诉 Claude 主题**
   ```
   请帮我生成关于 "Solana Restaking" 的 X Article
   ```

2. **Claude 会：**
   - 搜索最新资讯
   - 分析关键要点
   - 生成图片和内容
   - 提供可下载链接

3. **你的工作：**
   - 审阅内容
   - 根据需要微调
   - 发布到 X！

### 高级请求示例：

```
基于这篇文章生成 X Article，重点突出数据部分：
[粘贴 URL]

风格要更技术一些，目标读者是 DeFi 用户
```

```
生成一篇关于 EigenLayer 的文章，包含：
1. TVL 增长分析
2. 风险评估
3. 与竞品对比

图片要展示 TVL 增长趋势
```

## 📊 优化指标

生成的内容针对以下指标优化：

- **Impressions** - 吸引人的标题和图片
- **Likes** - 有价值的见解和数据
- **Saves** - 可参考的深度分析
- **Engagement** - 结尾的思考问题

## 🎓 最佳实践

1. **保持时效性** - 关注当天热点
2. **数据驱动** - 包含具体数字和图表
3. **简化复杂** - "长话短说"原则
4. **视觉优先** - 图片必须吸引眼球
5. **行动导向** - 给读者可执行的建议

## 🔄 更新和维护

### 更新配置
直接编辑 `config.json` 文件即可，无需重启

### 添加新模板
在 `config.json` 的 `content_templates` 中添加新的标题或开场白

### 调整图片风格
修改 `config.json` 中的 `color_scheme` 来更改配色方案

## 📞 使用帮助

### 常见问题

**Q: 图片尺寸可以调整吗？**
A: 可以！编辑 `config.json` 中的 `width` 和 `height`，但保持 5:2 比例

**Q: 如何添加自己的模板？**
A: 编辑 `config.json` 的 `content_templates` 部分

**Q: 能否同时生成多篇文章？**
A: 可以通过循环调用脚本，或直接让 Claude 帮你批量生成

**Q: 如何定时自动生成？**
A: 使用系统 cron job 或让 Claude 帮你设置定时任务

## 🎉 开始创作！

现在你已经了解了所有功能，可以开始创作高质量的 X Article 了！

记住：**内容为王，但展现形式同样重要。**

祝你的文章获得大量 impressions 和 engagement！🚀
