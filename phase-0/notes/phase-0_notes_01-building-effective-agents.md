# Building Effective Agents（Anthropic, 2024-12）

**学习日期：** 2026-05-11 (Day 2)
**类型：** Blog
**来源：** https://www.anthropic.com/research/building-effective-agents
**作者：** Anthropic

---

## 我学到的核心概念

### 1. Agentic Systems 的两大分类

Anthropic 把所有"用 LLM 完成多步任务"的系统统称为 **agentic systems**，但内部分两类：

| 类型 | 控制流由谁决定 | 特点 |
|---|---|---|
| **Workflow** | 工程师**预先**写死的代码路径 | LLM 和 tools 按固定路线运行 |
| **Agent** | LLM **动态**自己决定 | LLM 自主指挥流程和工具调用 |

**核心区别：control flow 是写死的（workflow）还是 LLM 自己决定的（agent）。**

这是 Phase 0 最重要的一个区分。它决定了你设计系统时的根本立场——**写死可控但僵硬，让 LLM 决定灵活但不可预测**。

---

### 2. Augmented LLM（增强型 LLM）

**定义：** 能调用外部能力（retrieval、tools、memory）的 LLM。

这是构建 workflow 和 agent 的最小积木——**所有 agentic system 都是用 augmented LLM 拼出来的**。

裸 LLM = 只能聊天的模型。
Augmented LLM = 能"动手"的模型（查资料、用工具、记东西）。

---

### 3. Workflow 的 5 种模式

#### 3.1 Prompt Chaining（串行链式）

**机制：** 多步 LLM 处理，每一步的输出是下一步的输入。中途可以设置 **gate**（检查点）。

**Gate 的作用：** 判断中间结果是否合格——不合格就退回或终止，不是用来选路径。

**类比：** 流水线工人，每个人加工后传给下一个。

**适合场景：** 任务可以拆成清晰的固定步骤（先翻译再润色再校对）。

---

#### 3.2 Routing（路由）

**机制：** 第一个 LLM 根据输入选择走哪条路径，第二个 LLM 用对应专门 prompt 处理。

**跟 Prompt Chaining 的区别：**
- Prompt Chaining 的 gate 是"继续/终止"（检查作用）
- Routing 是"选哪条路"（分诊作用）

**类比：** 医院分诊台——先判断你该挂哪个科，再让对应专科医生看你。

**适合场景：** 输入种类多，每类需要不同处理方式（客服系统：账单问题 / 技术问题 / 退款问题）。

---

#### 3.3 Parallelization（并行）

**机制：** 同一个 prompt 同时跑多个独立任务，最后汇总结果。不等第一个返回就发第二个。

**两种子模式：**

- **Sectioning（任务拆分）：** 把大任务拆成多个独立小块，每个 LLM 负责一块——避免单个 LLM 负担过重
- **Voting（多角度同任务）：** 多个 LLM 处理同一任务但视角不同，结果投票或综合

**类比：** 多个收银台同时结账，最后汇总营业额。

**适合场景：** 任务之间互不依赖，可以并发执行。

---

#### 3.4 Orchestrator-Workers（中央调度 + 工作者）

**机制：** 中央 LLM（orchestrator）动态拆分任务，分派给多个 worker LLM，再综合他们的结果。

**跟 Parallelization 的区别：**
- Parallelization 的任务划分是**预先定好的**
- Orchestrator-Workers 的任务划分是 **orchestrator LLM 当场决定的**

这一步开始更接近"agent"——任务拆分本身已经是 LLM 在动态决策。

---

#### 3.5 Evaluator-Optimizer（评估-优化循环）

**机制：** 一个 Generator LLM 生成答案，一个 Evaluator LLM 当编辑检查——不满意就退回重写，直到 evaluator 满意。

**类比：** 编辑和写手的循环——写手交稿，编辑挑刺，写手改稿，循环到编辑点头。

**适合场景：** 输出质量有明确标准、能被 LLM 判断的任务（写代码、写营销文案）。

---

### 4. Agent（真正意义上的智能体）

**机制：** 通过人类的初始指令或交互获得目标后，**自行规划、执行、调用工具**。在执行中：

- 每一步从环境获取真实数据评估进度
- 可以在检查点或障碍处暂停，向人类请求反馈
- 可以根据预先设置的停止条件终止
- 完成后终止

**和 workflow 的根本差别：** 步骤、工具、顺序不是工程师写死的，而是 agent **当场决定**的。

**典型应用：**
- 编码 agent（独立完成多文件代码修改任务）
- 客服 agent（处理整个客户问题流程，包括查数据库、退款、升级）

---

## 我自己解决的小问题

### Q: workflow 的 gate 跟 routing 看起来都是"判断"，到底差别在哪？

**A:**
- **Gate** 是判断"**这一步做得对不对**" → 决定继续还是中止
- **Routing** 是判断"**接下来该走哪条路**" → 在多条路径间选择

一个是质检员（gate），一个是分诊医生（routing）。

---

### Q: orchestrator-workers 跟 parallelization 区别是什么？

**A:** 都是多个 LLM 同时工作，但任务**怎么被分配**不同：

- **Parallelization：** 任务划分**写死在代码里**（工程师预先决定）
- **Orchestrator-Workers：** 任务划分由 **orchestrator LLM 当场决定**

这就是为什么 orchestrator-workers 已经在向 agent 过渡——动态决策出现了。

---

## 这篇我还没完全懂的（→ questions.md）

- workflow 和 agent 边界到底有多模糊？比如 orchestrator-workers 算 workflow 还是半 agent？
- "动态规划"和"预先编排"在代码上具体差别是什么？（Phase 1 写第一个 from-scratch agent 时应该会清楚）
- gate 的"检查"用什么实现？LLM 自己判断还是写规则？

(已转记到 `phase-0/questions.md`)

---

## 这篇对我 18 周的意义

**这是 Phase 0 的奠基文章。** 之后所有概念都建立在"workflow 5 种模式 + agent"这个框架上：

- Phase 1 写的 from-scratch agent → 是真正的 **agent**（LLM 决定 control flow）
- Phase 2 的 research-analyst → 是 **orchestrator-workers** 模式
- Phase 3 的 mini-harness → 给 **agent** 提供的运行环境（harness）
- Phase 4 的 eval → 评估 **agent** 的输出和路径

如果今天没把这 5 种模式 + agent 的区别弄清楚，后面所有项目讨论都会发虚。

---

## 下一步

- [ ] Day 3 上午：读 Anthropic《Effective context engineering》
- [ ] Day 3 下午：读 LangChain《Context Engineering for Agents》（WSCI 四原语）
- [ ] Day 3 晚上：Python Automate Ch.2（流程控制 if/else/for/while）
