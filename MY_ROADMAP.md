# My Agent Engineering Roadmap (v2 — Python 集成版)

*Personalized from https://github.com/codejunkie99/agent-roadmap-2026 on 2026-05-10. v2 generated 2026-05-10 after Python skill recalibration.*

## Profile
- Level: 真·0基础（Python 多年前碰过一点，按从头算）
- Time: 20+ 小时/周
- Stack: Python + Anthropic (Claude)
- Goal: 从0基础到用该技术赚到第一桶金
- Total estimated duration: **18 周**（Phase 5 持续进行）

---

## v2 关键变化

v1 漏掉了 Python 学习。v2 把 Python 作为**底色式持续学习**嵌进每个阶段，而不是单独留出 2-3 周集中突击。

**Python 学习的 3 条原则：**

1. **每天最多 45-60 分钟 Python 时间，分散在 18 周里**——不集中，因为集中学语法会忘，分散学才能跟项目场景挂钩
2. **每个 Phase 的项目代码都强制手敲**，不复制粘贴 anthropic-cookbook 或者 LangGraph examples——这是真正的练习场
3. **从 Phase 1 开始用 Cursor**，但要求 Cursor 逐行解释它写的代码——不能变成"AI 帮我写"，要变成"AI 当我私教"

---

## Before you start（Day 1 之前 / Day 1 当天）

- 注册 HuggingFace + GitHub + Anthropic Console（详见 Day 1 手册）
- 发第一条自媒体内容
- **额外加：** 在 GitHub 仓库里建一个 `python-practice/` 目录，作为整个 18 周 Python 练习的家

---

## Phase 0 — Foundations + Python 启蒙（NORMAL, 2 周 = Week 1-2）

**双重目标：**
1. 建立 agent 工程心智模型
2. 启动 Python 学习——目标是 Week 2 末能读懂、跑通、稍微改一改 anthropic-cookbook 的 notebook

### 每天的时间分配

| 时段 | 内容 | 时长 |
|---|---|---|
| 上午 | Anthropic / LangChain 博客精读 + 笔记 | 90-120 min |
| 下午 | 跑 anthropic-cookbook notebook + Python 实操 | 90-120 min |
| 晚上 | Python 基础学习 | 45-60 min |

### Python 学习路径（Phase 0 期间）

**用 [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) 第 1-6 章作为主线**——免费在线，章节短，例子实用：

- Week 1 Day 2-7：第 1-3 章（基础语法、控制流、函数）
- Week 2 Day 1-4：第 4-6 章（list、dict、字符串、文件）
- Week 2 Day 5-7：开始读懂 anthropic-cookbook 的 notebook，能解释每一行在干什么

**辅助资源：**
- [Real Python](https://realpython.com) — 遇到具体语法点查这里
- ChatGPT / Claude.ai 网页版 — 不懂的代码贴进去问"这一行在干什么，逐行解释"

### Phase 0 项目修改

原 deliverable：2 页心智模型文档。**v2 新增：**

- [ ] **`python-practice/week1-basics.py`**：用 Python 写一个简单脚本——读 questions.md 这个文件，统计行数、字符数、含有问号的行数。≤ 30 行
- [ ] **`python-practice/week2-cookbook-annotated.ipynb`**：把 anthropic-cookbook 里 prompt-chaining 的 notebook 拷一份过来，**每行加中文注释**，证明你看懂了

### Phase 0 Milestone（v2）

加一条：能用 Python 读取一个 .md 文件、做基本字符串处理、写个 for 循环，**不查文档**。

---

## Phase 1 — 第一个 agent + Python 巩固（NORMAL, 4 周 = Week 3-6）

**v2 把这里从 3 周延长到 4 周**——多出来的 1 周分散在整个 phase 里，给 Python 调试和 debug 留时间。

### 每天的时间分配

| 时段 | 内容 | 时长 |
|---|---|---|
| 上午 | 读官方文档、写代码主线 | 120 min |
| 下午 | 继续写代码 + debug | 120 min |
| 晚上 | Python 学习 + 复盘 | 45-60 min |

### Python 学习路径（Phase 1 期间）

- Week 3：Automate the Boring Stuff 第 7-9 章（正则、文件路径、组织文件）
- Week 4：第 11-12 章（web scraping、Excel——Phase 2 用得上）
- Week 5：环境管理（venv、pip、requirements.txt、.env）+ HTTP 请求（requests 库）
- Week 6：调试技巧（print debugging、断点、读 traceback）+ 用 Cursor 写代码的最佳实践

### Phase 1 工具切换：Day 1 用浏览器和文本编辑器，Phase 1 起换成 Cursor

**Phase 1 第 1 天（Week 3 Day 1）专门用 1 天装环境：**
- 装 Python 3.11+
- 装 [Cursor](https://cursor.sh)（推荐起步工具）
- 装 Git（命令行）
- 创建第一个 venv，跑通 `pip install anthropic` + 调用一次 `messages.create`
- 把 GitHub 仓库 clone 到本地

**这 1 天值得专门花**——0 基础卡在环境配置上的时间会比写代码还多，集中处理比每天卡 10 分钟好。

### Phase 1 项目修改

原 deliverable 不变（100 行 from-scratch agent + Claude SDK 重写 + daily-briefing），但**加严要求**：

- [ ] **每个项目必须自己手敲，禁止复制粘贴 cookbook 完整代码块**
- [ ] **每个文件顶部加一段 docstring**，用中文解释这个文件在干什么——逼你说人话
- [ ] **遇到 bug 必须在 `bugs.md` 里记录**：bug 现象、你怎么 debug、最终原因。这个文档比代码本身更值钱（Phase 4 做 eval 时会回头用）

### 自媒体内容方向（Phase 1）

第 3 条内容：**"0 基础学 Python 第一个月，我写出了什么"** —— 截图 daily-briefing agent 跑起来的样子 + 你的 bugs.md 节选。**真实失败比假装顺利的内容更值钱**。

---

## Phase 2 — LangGraph + Deep Agents（NORMAL, 4 周 = Week 7-10）

跟 v1 相同。Python 这时候应该已经不是瓶颈了。

### Python 学习路径（Phase 2 期间）

- Week 7-8：异步编程（async/await）—— LangGraph 大量用
- Week 9：类型注解（type hints、Pydantic）—— Phase 3 写 harness 时核心
- Week 10：装饰器（decorator）—— LangGraph 的 `@tool` 等

**学习方式从"读教程"切换到"读 LangGraph 源码 + 查需要的 Python 概念"** —— 这是更接近真实工作的学习方式。

### Phase 2 项目（v1 相同）

research-analyst Deep Agent + LangSmith trace URL + README + 第一次试水接单。

---

## Phase 3 — 自己写 mini-harness（NORMAL, 4 周 = Week 11-14）

### Python 学习路径（Phase 3 期间）

不再有"专门的 Python 学习时段"。Python 已经融入项目代码本身。

但有一个例外：**Week 11 花一个半天读 [Anthropic Python SDK 源码](https://github.com/anthropics/anthropic-sdk-python)** —— 你要自己写 harness，必须能读懂底层 SDK 在干什么。这本身是 Python 进阶最有效的方式。

### Phase 3 工具升级

**从 Cursor 切换到 Claude Code**（如果你还想继续用 Cursor 也可以，二选一）。理由：
- Phase 3 是"理解 agent 工程内部"，Claude Code 的 harness 本身就是你的研究对象
- 用 agent 工具写 agent 代码，元层认知会突然清晰

### Phase 3 项目（v1 相同）

1500 行 mini-harness + 1000 字 post-mortem。

---

## Phase 4 — Eval + regression（NORMAL+加权, 4 周 = Week 15-18）

跟 v1 相同。

### Python 学习路径（Phase 4 期间）

不再单独学 Python。但会接触：pytest（写测试）、GitHub Actions YAML（CI 配置）、pandas / matplotlib（看 eval 结果）。这些都属于"用到时学"，不需要预习。

### Phase 4 项目（v1 相同）

golden dataset + CI gate + Inspect benchmark + `make eval` 一键产出。

**Phase 4 末（Week 18）= 简历正式开投。**

---

## Phase 5 — 生产硬化（持续，从 Week 19 起）

跟 v1 相同。

---

## 公开发布要求（每个 Phase 都要做）

1. 公开 GitHub 仓库 + README 写清楚
2. 一篇技术写作（中文 / 英文）
3. 一条自媒体内容

---

## Project deliverables（v2 更新版）

### Phase 0（Week 1-2）
- [ ] 2 页中文心智模型文档
- [ ] questions.md（持续更新到 Phase 4）
- [ ] Python: week1-basics.py + week2-cookbook-annotated.ipynb
- [ ] 自媒体第 1 条：17 周计划开始（Day 1 发）
- [ ] 自媒体第 2 条：第一周笔记 + 心智模型（Day 7 发）

### Phase 1（Week 3-6）
- [ ] 100 行 from-scratch agent
- [ ] Claude Agent SDK 重写版
- [ ] daily-briefing agent（自己每天用）
- [ ] bugs.md（Phase 1 起持续记录）
- [ ] Python: 能解释自己写的每一行代码
- [ ] 自媒体第 3 条："0 基础写出第一个 agent"

### Phase 2（Week 7-10）
- [ ] research-analyst Deep Agent
- [ ] PostgresSaver + human-in-the-loop budget
- [ ] LangSmith trace URL
- [ ] 自媒体第 4 条：研究 agent demo
- [ ] 首次接单尝试

### Phase 3（Week 11-14）
- [ ] 1500 行 mini-harness
- [ ] 1000 字 post-mortem
- [ ] 自媒体第 5 条：mini-harness 系列
- [ ] 接单升级：诊断服务

### Phase 4（Week 15-18）
- [ ] golden dataset + grader
- [ ] CI gate
- [ ] Inspect benchmark run
- [ ] `make eval` 一键产出
- [ ] 自媒体第 6 条："为什么 90% 的 AI agent 都在 vibes 上改进"
- [ ] 简历正式投递开始

---

## Math（duration v2）

Phase 0 (2 周) + Phase 1 (4 周) + Phase 2 (4 周) + Phase 3 (4 周) + Phase 4 (4 周) = **18 周** + Phase 5 永久。

v1 是 17 周（Phase 1 是 3 周），v2 把 Phase 1 加到 4 周，多出来的 1 周分摊给 Python 上手 + 环境配置 + 第一次写真实代码的卡顿。

---

## Next action

**Day 1（今天）任务不变** —— 详见 Day1_Action_Manual.md。
Python 学习从 **Day 2** 正式开始（每晚 45-60 min）。
