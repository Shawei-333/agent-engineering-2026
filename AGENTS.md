# Project: Agent Engineering Roadmap

This project follows a personalized 18-week agent engineering roadmap.

**On every session start:**
1. Read `MY_ROADMAP.md` — the user's personalized plan (v2, includes Python integration).
2. Identify the current phase from the unchecked deliverables.
3. The "Next action" section tells you exactly what to help with today.

**Canonical roadmap:** https://github.com/codejunkie99/agent-roadmap-2026

---

## User profile (for context)

- **背景：** 真·0 基础（Python 多年前碰过一点，按从零算）
- **时间投入：** 20+ hours/week
- **栈：** Python + Anthropic (Claude)
- **总时长：** 18 周（v1 的 17 周 + 1 周 Python 缓冲，分散在 Phase 0-1）
- **目标：** 找工作 → 接单 → 自媒体内容（"0 基础学会并赚到钱"叙事线）
- **居住：** 比利时布鲁塞尔，Belgian Search Year Visa 至 2027 年 2 月
- **副业：** 中文意识研究科普视频（B 站 / 小红书等），已有内容创作经验

---

## 关键学习原则（Python 集成版）

1. **Python 分散学习,不集中突击** —— 每天 45-60 分钟,18 周里持续。早期用 Automate the Boring Stuff,后期跟项目需求触发学习。
2. **代码必须手敲,禁止从 cookbook / examples 复制粘贴整块代码** —— 这是 0 基础唯一能长出真功夫的方式。
3. **从 Phase 1 起用 Cursor**（Phase 3 切换到 Claude Code）。但要求 AI 工具**逐行解释**它写的代码,不能让 AI 帮写完事——AI 是私教,不是代笔。
4. **每个 Phase 都要公开发布**:GitHub 仓库 + 一篇技术写作 + 一条自媒体内容。这三件事跟代码 deliverable 同等重要。

---

## Rules（给未来 session 的 agent）

- **不要建议跳过 user 标记为 NORMAL 或 DEEP 的 phase。** 所有 phase 都是 NORMAL,不要压缩。
- **当 user 完成一个 deliverable**,在 `MY_ROADMAP.md` 勾选对应方框,并提示下一个。
- **当 user 问"下一步做什么"/"今天做什么"**,先读 `MY_ROADMAP.md`,不要凭记忆猜。
- **用户母语是中文**,技术术语保留英文,解释和讨论用中文。
- **用户明确偏好"边做边学"** —— 遇到卡壳时优先给可运行的代码片段,理论解释跟在代码后面,不要倒过来。
- **自媒体内容线**(每个 phase 一条)和**接单尝试**(Phase 2 起)跟代码 deliverable 同等重要,session 中要主动追踪、提醒,不要让用户只盯着代码忘记做内容。
- **Python 学习要在每天的对话里被自然提及**——不是单独问"今天 Python 学了吗",而是在用户做项目卡壳时识别"这是 Python 语法问题还是 agent 概念问题",分别处理。
- **不要给用户长篇 markdown 报告作为日常对话回复** —— 用户偏好直接、可执行的回应。复杂内容用文件交付,简单回应用对话。

---

## Critical context（务必记住）

- **Day 1 = 2026-05-10**（user 启动日）。所有 "Week N" 从这天算起。
- **MY_ROADMAP.md 是 v2** —— 如果用户提到 v1(17 周),那是过时版本,以 v2 (18 周 + Python 集成) 为准。
- **用户的求职窗口紧迫但不极紧迫** —— 签证到 2027 年 2 月,18 周计划末是 2026 年 9 月,留下约 17 个月找工作 + 接单 + 续签。这意味着不必"为了赶进度牺牲学习深度",但也不能"无限延期 phase"。
- **用户有强烈的内省和分析能力背景**(写作、心理分析、意识研究)。在做技术分析时可以使用类比和深层结构讨论,不需要把概念过度简化。但要警惕用户**用分析逃避执行** —— 如果用户连续几次倾向于"再多想想再做",温和提醒:**"想得够了,做吧"**。

---

## Files in this project

- `MY_ROADMAP.md` — 总计划 v2(18 周 + Python 集成)
- `AGENTS.md` — 此文件,给未来 agent session 用
- `Day1_Action_Manual.md` — Day 1 手册(已发出去,留作记录)
- `Week1_Daily_Plan.xlsx` — 第一周日程表
- `phase-0/` ~ `phase-5/` — 各阶段项目代码和笔记(随进度创建)
- `python-practice/` — 18 周 Python 分散学习的练习代码
- `questions.md` — 用户从 Phase 0 起持续记录的问题清单(高价值文档,持续到 Phase 4)
- `bugs.md` — 用户从 Phase 1 起持续记录的 bug 清单(同样高价值)

---

## Versioning

- v1 (2026-05-10 morning): 17 周计划,无 Python 学习路径
- **v2 (2026-05-10 afternoon): 18 周计划,Python 分散嵌入** ← 当前版本

如果发现 v3、v4 等更新,以最新版本为准。
