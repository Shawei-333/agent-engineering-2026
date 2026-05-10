HuggingFace LLM Course - Chapter 1 笔记
学习日期： 2026-05-10 (Day 1)
章节： Chapter 1 - Transformer 模型介绍
链接： https://huggingface.co/learn/llm-course/chapter1/1

我学到的核心概念
1. 三种 Transformer 模型架构
Transformer 不是一种统一的模型，根据使用 encoder（编码器）和 decoder（解码器）的方式不同，分为三大类：
模型类型别名结构代表模型GPT-like自回归 Transformerdecoder-onlyGPT、Claude、LlamaBERT-like自动编码 Transformerencoder-onlyBERT、RoBERTaBART/T5-like序列到序列 Transformerencoder + decoderT5、BART
它们的区别（我自己的理解）
Encoder（编码器）：理解输入

把输入文本压缩成向量表示
像"读懂一段话"——读完之后大脑里有了对这段话的理解
适合：文本分类、情感分析、命名实体识别等需要"理解"的任务

Decoder（解码器）：生成输出

一个 token 一个 token 地生成文本
"自回归"的意思是：生成下一个词时会看自己前面已经生成的词
像"写文章"——写一个字之前会看前面写了什么
适合：文本生成、对话、补全（GPT、Claude 都是这种）

Encoder + Decoder：理解输入 + 生成输出

先用 encoder 理解输入，再用 decoder 生成输出
适合：翻译、摘要、问答（输入需要被"理解"后转换成另一种形式输出）

2. 为什么不直接用任务数据训练模型？
我的理解（用医疗例子重述）
如果想训练一个"能看懂医疗诊断报告"的 AI：
两种数据：
数据类型数量级成本来源任务数据（医疗报告）1 万条左右极高（资深医生人工标注）医院、专家通用数据（书、网页、对话）数万亿词汇极低互联网
直接用 1 万条医疗数据从零训练的问题：

数据量太小，模型连"中文怎么说话"都学不会
严重过拟合——背下了 1 万条原文，但换一种说法就彻底傻了

正确做法（预训练 + 微调）：

预训练：用海量通用数据让模型先学会"说人话"、"逻辑推理"、"基础常识"
微调：用少量任务数据（医疗报告）让已经"会说话"的模型学会"医疗领域的具体知识"

核心洞察：任务数据永远稀缺，通用数据永远海量。利用海量数据先建底座，再用稀缺数据做专精——这是为什么"基础模型"这个概念存在。

Q: import transformers 为什么什么都不返回？
A: 这是 Python 的 import 机制——正确导入一个包是不会返回任何东西的。如果包没装好或者名字写错，才会报错（ImportError 或 ModuleNotFoundError）。

