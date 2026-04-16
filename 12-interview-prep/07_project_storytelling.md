# 12-07 项目 STAR 话术准备

> **目标**: 用 STAR 法则（Situation → Task → Action → Result）讲好 3 个 Capstone 项目
> **原则**: 数据量化结果、突出技术深度、与 B站业务结合

---

## STAR 法则模板

```
S (Situation): 项目背景和动机，为什么要做这个？
T (Task):      我负责什么？目标是什么？
A (Action):    我具体做了什么？用了什么技术？遇到什么挑战？怎么解决的？
R (Result):    成果如何？有什么数据？学到了什么？
```

---

## 项目 A: B站广告素材生成 Agent

### 一句话介绍
> 基于 LangGraph 构建的广告素材自动生成系统，通过多 Agent 协作实现 "产品信息输入 → 多套广告文案/标题输出 → 自动审核 → 迭代优化" 的闭环。

### STAR 话术

**S (背景)**:
B站商业化场景中，广告主和 UP 主需要频繁产出大量广告素材（文案、标题、封面描述），人工创作效率低、质量参差不齐。我希望用 AI Agent 自动化这个流程，提高素材产出效率。

**T (任务)**:
设计并实现一个广告素材生成 Agent 系统，要求：
- 输入产品信息，自动生成多套符合 B站风格的广告文案
- 内置审核机制，过滤违规/低质量内容
- 支持人工反馈后迭代优化
- 结构化输出，可直接对接投放系统

**A (行动)**:

1. **架构设计**: 采用 LangGraph 状态图编排，设计 4 个核心节点：
   - `generate` — 调用 LLM 生成初始素材（few-shot + CoT prompt）
   - `review` — 审核 Agent，检查合规性 + 质量评分（规则引擎 + LLM 双重检查）
   - `optimize` — 根据审核意见迭代优化（最多 3 轮）
   - `output` — 结构化输出（Pydantic 模型校验）

2. **Prompt Engineering**: 
   - 设计了 B站风格的 few-shot 示例（短标题、吸引力文案、弹幕风格）
   - 用 Context Engineering 技巧管理长 prompt（分层 system/user prompt）
   - 结构化输出用 JSON Mode + Pydantic 校验，确保格式一致

3. **关键挑战 & 解决**:
   - **挑战1**: LLM 生成内容重复度高 → 加入 temperature 动态调整 + 多样性 prompt
   - **挑战2**: 审核标准难以统一 → 规则引擎（敏感词/长度/格式）+ LLM 评分双通道
   - **挑战3**: 迭代优化容易陷入死循环 → 设置 max_iterations=3 + 质量分数阈值终止

4. **技术栈**: LangGraph (编排) + OpenAI/Qwen API (生成) + Pydantic (结构化输出) + LangSmith (链路追踪)

**R (结果)**:
- 单次生成 5 套素材，平均耗时 < 15 秒
- 审核通过率从无审核时的 ~60% 提升到 ~90%
- 支持 Human-in-the-loop，人工可在任意节点干预
- 输出格式 100% 结构化，可直接对接下游系统
- 通过 LangSmith 追踪发现并优化了 3 个 prompt 瓶颈点

### 可能的追问 & 回答

| 追问 | 回答要点 |
|------|---------|
| 为什么选 LangGraph 而不是纯 LangChain? | LangGraph 支持条件分支和循环，审核不通过需要回到生成节点，这用 Chain 难以实现 |
| 审核 Agent 的准确率如何评估? | 人工标注 200 条数据做 Golden Dataset，计算 Precision/Recall，LLM-as-Judge 的一致性达到 85% |
| 如何处理 B站特有的内容规范? | 规则引擎维护 B站敏感词库和内容规范 checklist，LLM 审核补充语义层面的判断 |
| 如果要支持多语言/多平台? | 架构已解耦，只需替换 prompt 模板和审核规则，核心编排逻辑不变 |

---

## 项目 B: 商业化智能客服 Agent (RAG)

### 一句话介绍
> 基于 RAG 技术的 B站广告主智能客服系统，实现对投放规则、数据报告、账户问题的自动问答，支持多轮对话和工单创建。

### STAR 话术

**S (背景)**:
B站商业化部门的广告主经常需要咨询投放规则、查看数据报告、解决账户问题，现有人工客服响应慢、知识覆盖不全。需要一个基于知识库的智能客服来提升服务效率。

**T (任务)**:
构建一个 RAG-based 智能客服 Agent：
- 接入 B站广告帮助文档（投放指南、FAQ、API 文档）
- 支持多轮对话，理解上下文
- 无法回答时自动创建工单
- 建立评估体系，持续优化回答质量

**A (行动)**:

1. **RAG Pipeline 搭建**:
   - 文档处理：解析 200+ 篇帮助文档（Markdown/PDF），RecursiveCharacterTextSplitter 分块 (chunk_size=512, overlap=64)
   - Embedding：使用 bge-large-zh 中文 Embedding 模型
   - 向量库：FAISS 索引，支持相似度检索 + 元数据过滤
   - 检索增强：BM25 + Dense 混合检索，RRF 融合排序

2. **Agent 能力增强**:
   - **意图路由**: 用 LLM 判断用户意图（知识查询 / 数据查看 / 工单创建 / 闲聊）
   - **对话记忆**: 滑动窗口 (最近 10 轮) + 关键信息提取存入长期记忆
   - **工具调用**: 数据查询 Tool (模拟 SQL 查询) + 工单创建 Tool
   - **引用来源**: 回答附带文档来源链接，支持溯源

3. **关键挑战 & 解决**:
   - **挑战1**: 检索噪声大，无关文档干扰生成 → 加入 Reranker (交叉编码器) 精排
   - **挑战2**: 多轮对话中指代消解困难 → 对话历史摘要 + 查询改写
   - **挑战3**: 无法回答的问题误回答 → 置信度评估 + "不确定"兜底策略

4. **评估体系**:
   - 人工标注 100 个 QA pair 作为 Golden Dataset
   - 指标：Retrieval Recall@5, Answer Faithfulness, Answer Relevance
   - 用 LLM-as-Judge 自动评估 + 人工抽检

**R (结果)**:
- 知识库覆盖 200+ 文档，支持实时增量更新
- Retrieval Recall@5 达到 85%，Answer Faithfulness 达到 90%
- 多轮对话支持 10 轮以上不丢失上下文
- 无法回答的问题正确路由到工单系统，误答率 < 5%
- 平均响应时间 < 3 秒

### 可能的追问 & 回答

| 追问 | 回答要点 |
|------|---------|
| Chunk size 怎么选的? | 实验对比 256/512/1024，512 在 Recall 和 Faithfulness 上综合最优；overlap=64 防止语义截断 |
| 向量库为什么选 FAISS 不选 Milvus? | 文档量级 ~百万 chunk 以内，FAISS 性能足够且部署简单；超过千万级才考虑 Milvus |
| 如何处理文档更新? | 增量更新：文档变更触发重新 chunking + embedding，用文档 hash 判断是否需要更新 |
| Reranker 的性能开销? | 对 top-20 候选做 rerank，P99 延迟增加 ~200ms，但 Recall 提升 15%，值得 trade-off |

---

## 项目 C: 多 Agent 广告投放优化平台

### 一句话介绍
> 基于 LangGraph + AutoGen 的多 Agent 协作系统，模拟 "数据分析→策略制定→素材生成→效果监控" 的完整广告投放优化闭环。

### STAR 话术

**S (背景)**:
B站广告投放涉及多个环节：数据分析、策略制定、素材生成、效果监控，各环节需要不同的专业能力。单一 Agent 难以胜任全流程，需要多个专业 Agent 协作完成。

**T (任务)**:
设计并实现一个多 Agent 广告投放优化平台：
- 4 个专业 Agent 各司其职（分析、策略、素材、监控）
- Supervisor Agent 统一协调
- 支持完整的 "分析→决策→执行→反馈" 闭环
- 可监控、可评估、可干预

**A (行动)**:

1. **多 Agent 架构设计**:
   - **Supervisor Agent**: 任务分发与协调，基于当前阶段决定调用哪个子 Agent
   - **Data Analyst Agent**: 分析历史投放数据，生成洞察报告（CTR/CVR/ROI 趋势）
   - **Strategy Agent**: 根据数据洞察制定投放策略（预算分配、人群定向、出价）
   - **Creative Agent**: 生成广告素材（复用 Capstone A 的能力）
   - **Monitor Agent**: 监控投放效果，异常告警，触发策略调整

2. **编排方式**:
   - 使用 LangGraph 实现 Supervisor 模式的状态图
   - TypedDict 定义全局 State，包含各 Agent 的输入输出
   - 条件边根据任务阶段路由到不同 Agent
   - 支持循环优化：Monitor 发现问题 → 回到 Analyst → 重新制定策略

3. **关键挑战 & 解决**:
   - **挑战1**: Agent 间信息传递丢失 → 用结构化 TypedDict State，而非自由文本
   - **挑战2**: 多 Agent 调用成本高 → 分层策略（简单任务单 Agent，复杂任务多 Agent）
   - **挑战3**: 死循环风险 → max_iterations=5 + 质量分数单调递增约束
   - **挑战4**: 调试困难 → 集成 LangSmith 全链路追踪，每个 Agent 调用可视化

4. **工程化实践**:
   - Agent 评估：每个 Agent 独立评估 + 端到端评估
   - 监控告警：token 用量、延迟、错误率监控
   - Human-in-the-loop：关键决策节点（策略确认、素材审核）支持人工干预

**R (结果)**:
- 4 个专业 Agent + 1 个 Supervisor，完整覆盖投放优化流程
- 端到端完成一次投放优化建议平均耗时 < 60 秒
- 通过结构化 State 传递，Agent 间信息保真率 100%
- LangSmith 追踪覆盖 100% 的 Agent 调用链路
- 支持 docker-compose 一键部署，可演示完整流程

### 可能的追问 & 回答

| 追问 | 回答要点 |
|------|---------|
| 为什么用 Supervisor 而不是 Pipeline? | 投放优化不是固定流程，Monitor 可能触发回到 Analyst 重新分析，需要动态路由；Pipeline 只能线性执行 |
| 多 Agent 的成本如何控制? | 1) 简单任务直接单 Agent 处理; 2) 子 Agent 用小模型 (Qwen-7B); 3) 设置 token 预算上限; 4) 缓存常见分析结果 |
| 如何保证多 Agent 输出的一致性? | Pydantic 结构化输出约束每个 Agent 的输出格式; State 中定义严格的字段类型; 输出校验失败则 retry |
| 跟真实广告系统的差距? | 数据是模拟的（用 Faker 生成），真实系统需对接 DMP、广告 API、Hive 数仓；但 Agent 架构和编排逻辑可直接复用 |

---

## 通用追问准备

### "你遇到的最大挑战是什么？"

> 多 Agent 系统的调试。当 4 个 Agent 串联时，某个 Agent 的输出异常会级联影响后续所有 Agent。解决方案是：1) 每个 Agent 独立单测; 2) 集成 LangSmith 链路追踪，精确定位哪个节点出问题; 3) 结构化 State + Pydantic 校验，在 Agent 边界做强制类型检查。

### "如果用户量增大 10 倍怎么办？"

> 1) Agent 编排引擎无状态化，水平扩展; 2) LLM 调用走消息队列异步化; 3) 向量库从 FAISS 迁移到 Milvus 支持分布式; 4) 热门查询结果缓存; 5) 模型层面考虑用小模型+蒸馏降低推理成本。

### "这个项目你最得意的技术决策是什么？"

> 选择 LangGraph 做编排框架。它的状态图模型天然支持条件分支和循环，非常适合 Agent 需要"审核不通过→重新生成"或"效果不好→重新分析"的场景。相比纯 LangChain 的 Chain，代码更清晰、可维护性更好；相比手写状态机，LangGraph 提供了持久化、可视化、Human-in-the-loop 等开箱即用的能力。

### "你对 Agent 领域未来的看法？"

> 1) Agent 会从"demo 级"走向"生产级"，工程化能力（评估、监控、安全）变得比 prompt 技巧更重要；
> 2) 多 Agent 协作会成为主流，类似微服务架构的演进；
> 3) Agent 后训练（DPO/RLHF）会让 Agent 从"通用"变为"领域专精"；
> 4) 低代码 Agent 平台会降低使用门槛，但核心开发者仍需要深入理解底层原理。
