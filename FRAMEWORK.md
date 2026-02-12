# 🧠 X Article Generation Framework (SOP)

This document outlines the standard operating procedure (SOP) for generating X Articles (text and images). **All future article generation tasks should follow this 4-phase framework.**

---

## Phase 1: Discovery 🔍
**Goal: Understand the true intent and scope.**

Before writing a single line of code or text:
1.  **Ask Clarifying Questions**: Do not just execute the request. Dig deeper to understand what the user *actually* needs, which might differ from what they initially asked.
2.  **Challenge Assumptions**: If a request seems illogical, contradictory, or suboptimal, politely challenge it. Offer a better perspective.
3.  **Scope Reality Check**:
    *   Is the idea too big?
    *   Is it too vague?
    *   **Action**: Suggest a "smarter starting point" or a Minimum Viable Article (MVA) if the scope is too broad.

---

## Phase 2: Planning 📋
**Goal: Align on the blueprint before execution.**

Once the scope is defined, propose a concrete plan:
1.  **Version 1 Proposal**: State exactly what will be built in this iteration.
2.  **Complexity Estimation**: Rate the task difficulty:
    *   🟢 **Simple**: Quick edit or basic post.
    *   🟡 **Medium**: Requires research or custom graphics.
    *   🔴 **Ambitious**: Deep dive, complex data viz, or series.
3.  **Requirements Checklist**: Identify missing inputs (e.g., "I need a specific headline," "What are the 3 key stats?").
4.  **Rough Outline**: Provide a skeleton of the final article (Section headers, key takeaways) for approval.

---

## Phase 3: Writing & Execution ✍️
**Goal: Transparent creation and learning.**

During the actual generation process:
1.  **Follow the Writing Style Guide**: All articles MUST follow `WRITING_STYLE_GUIDE.md`. Key checkpoints:
    *   **Hook**: Does the first paragraph make people want to keep reading? (Scene/Data/Question hook)
    *   **Metaphor System**: Does the article have a coherent metaphor thread?
    *   **Emotional Rhythm**: Does it alternate between humor/sharp insight/warmth every 2-3 paragraphs?
    *   **Colloquial Tone**: Does it include 語氣詞, 括號碎碎念, and everyday language?
    *   **Concrete Examples**: Does every point have a real story/data to back it up?
2.  **Image Planning** (see `WRITING_STYLE_GUIDE.md` §圖片插入策略):
    *   **Mandatory**: Topic thumbnail at article start (1000×400px)
    *   **Data points**: Insert screenshot/data viz when stats are mentioned
    *   **Complex concepts**: Insert concept/flow chart for multi-step explanations
    *   **Section breaks**: Consider visual rest images between major sections
    *   **Quote cards**: Create image cards for "screenshot-worthy" golden sentences
3.  **Explain "The Why"**: Don't just show the result. Explain the reasoning behind design choices, word selection, or code changes. (The user wants to learn!).
4.  **Problem Solving Protocol**:
    *   **STOP** if you hit a snag (e.g., tool error, missing data).
    *   **Do NOT** silently fix it with a default assumption.
    *   **Present Options**: "I hit problem X. We can do A (fast) or B (thorough). Which do you prefer?"

---

## Phase 4: Polishing ✨
**Goal: Humanize and Maximize Engagement.**

After the draft is generated, refine it against the **「人味兒」五字訣** (see `WRITING_STYLE_GUIDE.md`):

1.  **「真」Check — Authenticity**:
    *   Does it start with a personal "I" experience? (Not "在當今社會…")
    *   Are there admissions of failure/embarrassment? (踩坑、翻車)
    *   Is there at least 1 self-deprecating moment?

2.  **「辣」Check — Sharpness**:
    *   Is there at least 1 "倒吸涼氣" bold judgment?
    *   Are there colloquial rough edges? (口語粗話, 網絡俚語)
    *   Does it dare to say "扎心的話"?

3.  **「暖」Check — Warmth**:
    *   Is the closing paragraph "具體到可以立刻做"? (Not just "記得休息")
    *   Are there moments of撒嬌/示弱? (呀~ 🙈)
    *   Does it use "我們" to create togetherness?

4.  **「活」Check — Vivid Metaphors**:
    *   Is there a coherent metaphor thread throughout?
    *   Are abstract concepts grounded in日常生活 imagery?
    *   每篇至少 3-5 個原創比喻

5.  **「節」Check — Emotional Rhythm**:
    *   Does the tone shift every 2-3 paragraphs?
    *   Is there contrast (humor↔serious, sharp↔warm)?
    *   Does the ending land with a different emotion than the opening?

6.  **Engagement Hooks**:
    *   **"Open Loop" Details**: Drop hints or questions that make readers curious about the next piece of content.
    *   **Value-Add for Saving**: Ensure there is at least one "Cheat Sheet", "Checklist", or "Framework" that makes the user want to hit the **Save/Bookmark** button.
    *   **Shareability**: Include at least 1-2 golden sentences worth screenshotting and sharing.
    *   **CTA**: End with a specific question to drive comments (「評論區聊聊…👇」)

7.  **Anti-Pattern Scan** (see `WRITING_STYLE_GUIDE.md` §絕對禁止):
    *   ❌ No 「您」throughout — use 「你」
    *   ❌ No AI-sounding openings (「在當今…」「隨著…的發展」)
    *   ❌ No excessive exclamation marks (max 3-5 per article)
    *   ❌ No points without supporting stories/data
    *   ❌ No ending with just 「總結」— use warm scene or philosophical quote

---

## Design System: Visual Style 🎨

### **"YouTube Influence" (High Contrast)**
*   **Best for**: Deep dives, controversial opinions, warnings, analysis.
*   **Colors**: Black Background (#000000), white text, **Orange highlights** (#FF9900).
*   **Vibe**: Bold, clear, expert-level.
*   **Image specs**: 1000x400px (5:2 ratio), PNG format.

---

## Output Standards 📁

**所有生成的檔案與圖片一律存進 `crypto-x-articles/`，不要放在 `articles/`。**

- **Output folder**: 專案內使用 `crypto-x-articles/`（或對應絕對路徑）。
- **禁止**: 勿將生成的文章、縮圖、圖片存到 `articles/`。`articles/` 僅供草稿或暫存用途，非正式輸出目錄。

**All generated content MUST be saved to:**
```
/Users/iruka/Downloads/claucowork/crypto-x-articles/
```
（或專案內的 `crypto-x-articles/`）

**Naming Convention:**
- Article: `{article_name}.md`
- Image: `{article_name}.png`
- Keep names consistent and descriptive (use underscores, lowercase)

**Example:**
- `x_blue_follow_strategy_analysis.md`
- `x_blue_follow_strategy_analysis.png`

---

## Quick Generation Tools 🛠️

### Method 1: Python Helper (Recommended)
```bash
# Generate image for existing article
python3 generate_article_image.py article_name "文字1" "文字2" --highlight 0

# Example
python3 generate_article_image.py x_blue_strategy "X藍V" "互關" "真的" "有用？" --highlight 0 3
```

### Method 2: Interactive Script
```bash
./generate_x_article_complete.sh
```

### Method 3: Direct Python Code
```python
from generate_image import ThumbnailGenerator

gen = ThumbnailGenerator()
blocks = [
    {'text': '不要用', 'highlight': False, 'row': 0},
    {'text': 'AI代理', 'highlight': True, 'row': 0},
]
path = gen.create_thumbnail(
    blocks,
    output_path='/Users/iruka/Downloads/claucowork/crypto-x-articles/article_name.png'
)
```

---

## Related Documents 📚

- **`WRITING_STYLE_GUIDE.md`** — 人性化寫作風格指南（核心！所有文章必讀）
- **`X_ARTICLE_WORKFLOW.md`** — 完整工作流程和圖片生成指南
- **`content box/`** — 6 篇範本文章原文（風格學習素材）

---

## Example Interaction

**User**: "Write an article about DeFi."

**Agent (Phase 1)**: "DeFi is huge. Are you targeting beginners or degens? Are we talking about yields, security, or a specific protocol? If you want engagement, I suggest we focus on 'DeFi Risk Management for 2026' as that's trending."

**Agent (Phase 2)**: "Okay, focusing on Risk.
*   **Plan**: 5-point checklist for safety.
*   **Complexity**: 🟢 Simple.
*   **Outline**:
    *   Hook: 'You will get rug pulled.'
    *   Point 1: Revoke permissions.
    *   ...
    *   CTA: What's your safety score?
*   **Need**: Do you have a specific tool you want to mention?"

**Agent (Phase 3)**: "I'm generating the image now using a 'Warning' color scheme (Red/Black) to match the risk theme. I encountered an issue: The API for the chart is down. Option A: Use a generic icon. Option B: Wait for you to provide a screenshot. What do you think?"

**Agent (Phase 4)**: "Article and image generated! Both saved to `/Users/iruka/Downloads/claucowork/crypto-x-articles/` as `defi_risk_2026.md` and `defi_risk_2026.png`"

---

## Conversation Archiving Workflow 📋

**Purpose**: Preserve important conversations for future reference.

### Process (Manual)

**At the end of each conversation:**
1. User says: "請幫我總結這次對話，生成存檔文檔"
2. Agent generates a summary document with format: `YYYY-MM-DD_描述.md`
3. File is saved to `對話存檔/` folder

### Naming Convention

**Format**: `YYYY-MM-DD_Brief_Description.md`

**Examples**:
- `2026-02-12_Framework_Update.md`
- `2026-02-12_Image_Generation_Workflow.md`
- `2026-02-13_Theme_Restrictions_Removal.md`

### Archive Content Should Include

- **Task objective**: What was the goal?
- **Work completed**: Files created/modified
- **Key decisions**: Why certain choices were made
- **Important findings**: Lessons learned
- **Outstanding issues**: What's left to do (if any)

### Example Archive Document

```markdown
# 任務名稱 - 對話存檔

**日期**: 2026-XX-XX
**目標**: [簡述任務]

## 已完成
- [列出完成項目]

## 新增/修改檔案
- file1.py - [做了什麼]
- file2.md - [做了什麼]

## 關鍵決策
- [決策 1 及原因]
- [決策 2 及原因]

## 遺留問題
- [如果有未完成事項]
```

This ensures continuity across conversation contexts and helps new agents quickly understand project history.
