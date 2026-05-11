# anthropic-cookbook 抄写作业：basic_workflows.ipynb

**学习日期：** 2026-05-11 (Day 2)
**类型：** Code reading
**来源：** https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents
**原始文件：** `basic_workflows.ipynb`

---

## 这次作业的方法

Day 2 我对自己的要求是**逐行读 + 用中文注释解释自己看懂了什么**。看不懂的地方写下"我不确定这是在做什么"，不假装懂。

这份文档是我用自己的话给原 notebook 加注释的版本——**注释完全是我自己写的**，不是直接抄原作者的注释。3 个月后我回来看，应该能立刻想起当时为什么这样理解。

---

## 完整代码 + 我的注释

### 导入部分

```python
# 从 util 文件里搬出两个工具函数
# llm_call: 给 prompt, 返回 Claude 的回复文本
# extract_xml: 从一段文本里抠出 <tag>...</tag> 中间的内容
from util import extract_xml, llm_call

# 从标准库搬出线程池, parallel 函数会用它实现"同时跑多个任务"
from concurrent.futures import ThreadPoolExecutor
```

---

### 第一部分：chain 链式工作流

```python
# 链式 = 流水线
# 每一步的输出, 是下一步的输入

def chain(input: str, prompts: list[str]) -> str:
    # result 是"接力棒", 一开始拿着原始输入
    result = input

    # enumerate 给每条 prompt 编号, 从 1 开始
    for i, prompt in enumerate(prompts, start=1):
        print(f"\nStep {i}:")

        # f-string 拼接: 把当前 prompt 和上一步的 result 一起发给 Claude
        # 新结果覆盖旧 result, 传给下一轮
        result = llm_call(f"{prompt}\nInput: {result}")
        print(result)

    # 循环结束, result 是最后一步的产出
    return result
```

**我的理解：** 这就是 Building Effective Agents 那篇博客里说的 **Prompt Chaining** 模式的最简实现。流水线工人之间传递接力棒——上一个人加工完，下一个人接着加工。代码上的关键是 `result = llm_call(...)` 这一行**用同一个变量名覆盖**自己，所以每次循环 result 都更新。

---

### 第二部分：parallel 并行工作流

```python
# 同一个 prompt, 同时处理多个独立输入
# 不等第一个回复, 就立刻发第二个

def parallel(prompt: str, inputs: list[str], n_workers: int = 3) -> list[str]:

    # with 语法: 借一个线程池, 出了缩进块自动归还
    # max_workers=3 表示最多同时干 3 个活
    with ThreadPoolExecutor(max_workers=n_workers) as executor:

        # 列表推导式: 把每个 input 都扔给工人池
        # 注意! submit(llm_call, "...") 而不是 submit(llm_call("..."))
        # 前者是"安排工人去执行", 后者会先执行再 submit, 变成串行
        futures = [
            executor.submit(llm_call, f"{prompt}\nInput: {x}")
            for x in inputs
        ]

        # submit 返回的是"凭证"(future), 还不是真答案
        # .result() 才是取货, 会等到结果真的回来
        return [f.result() for f in futures]
```

**我的理解：** 对应博客里的 **Parallelization** 模式。线程池就像几个收银台同时开张，每个收银台独立处理顾客。**最容易踩坑的地方是 `submit(llm_call, "...")` 的写法**——参数是分开传的，不是直接调用函数；不然就成了 Python 先把函数算完再交给线程池，等于没并行。

---

### 第三部分：route 路由工作流

```python
# 像分诊台
# 第一次调 Claude: 判断该走哪条路
# 第二次调 Claude: 用对应的专科 prompt 真正作答

def route(input: str, routes: dict[str, str]) -> str:
    # routes 是字典, key 是路由名字, value 是专科 prompt
    # 例子: {"billing": "你是账单专家...", "technical": "你是技术支持..."}

    # 构建分诊 prompt: 让 Claude 用规定的 XML 格式回答
    # XML 标签是为了让代码能精确解析——把自由文本变结构化数据
    selector_prompt = f"""
    从这些选项中选最合适的团队: {list(routes.keys())}
    先解释理由, 再用以下 XML 格式给出选择:
    <reasoning>解释为什么这样选</reasoning>
    <selection>选中的团队名</selection>
    Input: {input}
    """.strip()

    # 第一次调用 LLM——分诊
    route_response = llm_call(selector_prompt)

    # 从返回文本里抠出两个字段
    reasoning = extract_xml(route_response, "reasoning")

    # .strip() 去掉前后空白, .lower() 转小写
    # 防御性写法: Claude 可能输出 billing 或者 Billing\n, 统一格式才能查字典
    route_key = extract_xml(route_response, "selection").strip().lower()

    # 用 key 查字典, 取出对应的专科 prompt
    selected_prompt = routes[route_key]

    # 第二次 LLM 调用——注意传的是原始 input, 不是分诊结果
    # 分诊结果只是用来选 prompt 的, 选完就丢
    return llm_call(f"{selected_prompt}\nInput: {input}")
```

**我的理解：** 对应博客里的 **Routing** 模式。**最值得注意的是 XML 标签的设计意图**——Claude 输出的是自由文本，但代码需要"结构化数据"才能继续处理。XML 标签就是 LLM 和传统代码之间的"翻译协议"。这个思路 Phase 2 应该会反复出现。

---

## 我从这次抄写学到的三件事

### 1. 三种模式共同点

- 底层都是 `llm_call` 这一块"砖"的不同组合方式
- 都靠 **f-string 动态构造 prompt**
- 都让 LLM 输出**结构化格式**（XML/JSON），代码精确解析

**LLM 输出结构化 + 代码解析 = LLM 和传统代码之间的接口** ——直觉告诉我这是 agent 工程的命门。

### 2. 三种模式什么时候用哪个

| 模式 | 适合场景 | 类比 |
|---|---|---|
| chain | 任务有清晰固定步骤 | 流水线工人 |
| parallel | 多个任务互不依赖 | 多个收银台 |
| route | 输入种类多需要分发 | 医院分诊台 |

### 3. Python 视角的收获

虽然我 Python 才学到 Variables，但抄完这份代码后我**预感到**接下来要学的：

- **函数定义**（`def`）—— Phase 0 末必须掌握
- **类型注解**（`str`、`list[str]`、`dict[str, str]`）—— Phase 2 学
- **f-string** —— 看起来很常用，下次 Python 学习时优先攻克
- **列表推导式** `[... for x in inputs]` —— Phase 1 应该会用
- **with 语句** —— Phase 1 处理文件时会再遇到
- **`*args` / lambda / `submit` 这种"把函数当数据传"** —— 概念上还没懂

---

## 我还没看懂的地方（→ questions.md）

- `ThreadPoolExecutor` 这个"线程池"具体是怎么实现"同时跑"的？Python 不是有 GIL 吗？
- `submit(llm_call, ...)` 跟 `llm_call(...)` 在 Python 内存里到底差什么？为什么前者不会立刻执行？
- `with` 语句的"自动归还"具体怎么发生的？什么是上下文管理器？
- `f"""..."""` 三引号 f-string 和 `f"..."` 单引号 f-string 有什么差别？

（这些都不急着懂，记下来作为 Phase 0-1 期间的"待消化"列表）

---

## 这次抄写对我 18 周的意义

**今天是我 0 基础第一次真正读懂一段 agent 代码。** 不是逐行明白每个 Python 语法（很多还不懂），而是**理解了代码的"意图层"**——这三段代码在做什么、为什么这样组织、跟博客理论怎么对应。

这种"看不懂 Python 细节但能看懂代码意图"的状态，是 Phase 0 应该达到的水平。Phase 1 学完 Python 基础后回头看这份文件，应该能完全看懂每一行。届时这份注释作业**会变成我自己的进度证据**——"3 周前我还看不懂这些 Python 写法"。
