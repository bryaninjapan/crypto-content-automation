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
1.  **Explain "The Why"**: Don't just show the result. Explain the reasoning behind design choices, word selection, or code changes. (The user wants to learn!).
2.  **Problem Solving Protocol**:
    *   **STOP** if you hit a snag (e.g., tool error, missing data).
    *   **Do NOT** silently fix it with a default assumption.
    *   **Present Options**: "I hit problem X. We can do A (fast) or B (thorough). Which do you prefer?"

---

## Phase 4: Polishing ✨
**Goal: Humanize and Maximize Engagement.**

After the draft is generated, refine it to feel authentic and "sticky":
1.  **Human Tone Check**:
    *   **Anti-Robot Filter**: Remove stiff, corporate, or overly academic language.
    *   **Conversational Flow**: Use "I", "You", "We". Write like you are talking to a friend at a coffee shop.
    *   **Rhythm**: Vary sentence length. Use short, punchy sentences for impact.
2.  **Engagement Hooks**:
    *   **"Open Loop" Details**: Drop hints or questions that make readers curious about the next piece of content.
    *   **Value-Add for Saving**: Ensure there is at least one "Cheat Sheet", "Checklist", or "Framework" that makes the user want to hit the **Save/Bookmark** button.
    *   **Shareability**: Include a quote or a hot take that is easy to **Repost/Quote**.

---

## Design Systems: Visual Styles 🎨
Standardized visual templates to ensure brand consistency:

### 1. **"YouTube Influence" (High Contrast)**
*   **Best for**: Hardcore knowledge, deep dives, controversial opinions.
*   **Colors**: Black Background (#000000), white headers, **Orange highlights** (#FF9900).
*   **Vibe**: Bold, clear, expert-level.

### 2. **"Data Visualization" (Tech Blue)**
*   **Best for**: Market reports, TVL data, technical releases.
*   **Colors**: Deep Blue/Purple gradients, cyan accents.
*   **Vibe**: Future-forward, professional, systematic.

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
