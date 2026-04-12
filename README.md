# B站商业化 AI Agent 开发工程师 · 3个月冲刺学习路线

> 目标岗位：哔哩哔哩 — 商业化 AI Agent 开发工程师  
> 学习周期：12 周全日制冲刺 (~350 小时)  
> 学习形式：Jupyter Notebook 为主，边学边练

---

## 学习进度看板

### Phase 1: 基础夯实 (W1-W3)

| 状态 | 模块 | 主题 | 关键产出 |
|:---:|------|------|---------|
| ⬜ | [00-setup](./00-setup/) | 环境搭建 | Jupyter + API Keys + 依赖安装 |
| ⬜ | [01-python-advanced](./01-python-advanced/) | Python 进阶 | async/await, 装饰器, Pydantic |
| ⬜ | [02-database-sql](./02-database-sql/) | SQL & 数据库 | MySQL/Hive/窗口函数 |
| ⬜ | [03-llm-fundamentals](./03-llm-fundamentals/) | 大模型基础 | Transformer, API调用, Prompt Engineering |

### Phase 2: Agent 核心能力 (W4-W6)

| 状态 | 模块 | 主题 | 关键产出 |
|:---:|------|------|---------|
| ⬜ | [04-rag-pipeline](./04-rag-pipeline/) | RAG 检索增强生成 | 向量库 + 检索 + 重排 + 生成 |
| ⬜ | [05-langchain-langgraph](./05-langchain-langgraph/) | LangChain + LangGraph | Agent 编排, 状态图, 多 Agent |
| ⬜ | [06-autogen-multi-agent](./06-autogen-multi-agent/) | AutoGen 多智能体 | 多 Agent 对话 + 工具调用 |

### Phase 3: 平台 & 进阶 (W7-W9)

| 状态 | 模块 | 主题 | 关键产出 |
|:---:|------|------|---------|
| ⬜ | [07-agent-platforms](./07-agent-platforms/) | Agent 平台 | Dify / Coze / n8n 实操 |
| ⬜ | [08-openclaw](./08-openclaw/) | OpenClaw 深度 | 架构解析 + 插件开发 |
| ⬜ | [09-fine-tuning-llm](./09-fine-tuning-llm/) | LLM 微调 | SFT / LoRA / QLoRA |
| ⬜ | [10-agent-engineering](./10-agent-engineering/) | Agent 工程化 | 记忆/评估/监控/策略/后训练 |

### Phase 4: 实战冲刺 (W10-W12)

| 状态 | 模块 | 主题 | 关键产出 |
|:---:|------|------|---------|
| ⬜ | [11-capstone-projects](./11-capstone-projects/) | 综合实战 | 3个B站商业化场景项目 |
| ⬜ | [12-interview-prep](./12-interview-prep/) | 面试冲刺 | LLM理论 + Agent设计 + SQL + 系统设计 |

> 完成一个模块后将 ⬜ 改为 ✅

---

## 12 周详细计划

### W1: 环境搭建 + Python 进阶
- [ ] 配置 JupyterLab + API Keys + 安装依赖
- [ ] async/await 并发编程
- [ ] 装饰器 & 生成器
- [ ] Pydantic 类型验证 & 结构化输出
- **自检**: 能用 async/await 并发调用 3 个 LLM API

### W2: SQL 精进 + LLM 原理
- [ ] MySQL CRUD + JOIN + 子查询
- [ ] 窗口函数 (ROW_NUMBER, LAG, SUM OVER)
- [ ] Hive 基础 (DDL, 分区, 文件格式)
- [ ] Transformer 架构 (Self-Attention 计算流程)
- [ ] Tokenization & Embedding 原理
- **自检**: 手写窗口函数算 7 日留存; 画出 Attention 计算流程

### W3: LLM API + Prompt Engineering
- [ ] OpenAI / Claude / 通义千问 API 统一调用
- [ ] Prompt Engineering 系统化 (Few-shot, CoT, Structured Output)
- [ ] Context Engineering (上下文窗口管理, 长文档处理)
- **自检**: 构建一个稳定的商品分类 prompt (准确率 > 90%)

### W4: RAG 全链路
- [ ] Embedding 模型 + 向量数据库 (FAISS / Chroma)
- [ ] 文档切分策略 (固定/语义/递归)
- [ ] 检索 + Reranking
- [ ] 高级 RAG (HyDE, Self-RAG, Graph-RAG)
- [ ] **Mini Project**: B站广告知识库 Q&A 系统
- **自检**: 完整 RAG pipeline 从 PDF 到回答

### W5: LangChain + LangGraph 基础
- [ ] LangChain 核心 (Chain / Prompt / OutputParser)
- [ ] 工具调用 + ReAct Agent
- [ ] LangGraph 状态图编排 (节点/边/条件分支)
- **自检**: 用 LangGraph 实现带循环的 Agent 工作流

### W6: 多 Agent + AutoGen
- [ ] LangGraph 多 Agent 协作
- [ ] LangGraph 状态持久化 + Human-in-the-loop
- [ ] AutoGen 基础 + 工具注册 + 多 Agent 对话
- [ ] **Mini Project**: 广告素材审核 Agent + 广告策略 Agent 团队
- **自检**: 完成两个可运行的 Agent 系统

### W7: Agent 平台 + OpenClaw 入门
- [ ] Dify 工作流搭建 (RAG 知识库 Bot)
- [ ] Coze 智能体开发
- [ ] n8n 自动化流程
- [ ] OpenClaw 架构解析 (Gateway / Agent / Runner)
- **自检**: 在 Dify 上部署一个完整 Bot; 画出 OpenClaw 架构图

### W8: OpenClaw 深度 + 微调入门
- [ ] OpenClaw 插件开发实战
- [ ] OpenClaw 多渠道适配器
- [ ] SFT 监督微调原理与实战
- [ ] PEFT / LoRA 原理 + HuggingFace 实战
- **自检**: 为 OpenClaw 写一个自定义插件; 用 LoRA 微调 7B 模型

### W9: 高级微调 + Agent 工程化
- [ ] QLoRA 低资源微调
- [ ] 微调数据构造与清洗
- [ ] Agent 记忆系统 (短期/长期/向量/摘要)
- [ ] Agent 评估 (LLM-as-Judge, Golden Dataset)
- [ ] Agent 监控 (LangSmith / Phoenix 链路追踪)
- **自检**: 微调广告文案模型; 实现带长期记忆的 Agent

### W10: Agent 策略 + Capstone A
- [ ] Agent 策略 (ReAct / Plan-and-Execute / Reflection)
- [ ] Agent 后训练 (RLHF / DPO 概念 + 数据飞轮)
- [ ] **Capstone A**: B站广告素材生成 Agent (完整闭环)
- **自检**: 素材生成 Agent 跑通 prompt→生成→审核→优化

### W11: Capstone B + C
- [ ] **Capstone B**: 商业化智能客服 Agent (RAG + 记忆 + 评估)
- [ ] **Capstone C**: 多 Agent 广告投放优化平台
- **自检**: 两个项目各有完整 README + 架构图 + 可复现

### W12: 面试全力冲刺
- [ ] LLM 理论八股 (Transformer / Attention / KV Cache / RoPE)
- [ ] Agent 设计题 (架构 / 记忆 / 评估 / 多 Agent)
- [ ] RAG 深度问答
- [ ] SQL 高频面试题 (50 题)
- [ ] 系统设计 (Agent 平台 / RAG 系统 / 广告 Agent)
- [ ] 项目 STAR 话术准备
- **自检**: 模拟面试 70%+ 通过率

---

## 技术栈总览

| 类别 | 技术 |
|------|-----|
| **语言** | Python (主力), SQL (精通), TypeScript (阅读 OpenClaw) |
| **LLM** | OpenAI API, Claude API, 通义千问, HuggingFace Transformers |
| **Agent 框架** | LangChain, LangGraph, AutoGen |
| **Agent 平台** | Dify, Coze, n8n |
| **开源项目** | OpenClaw (架构 + 插件开发) |
| **RAG** | FAISS, Chroma, Sentence-Transformers, Reranker |
| **微调** | PEFT, LoRA, QLoRA, TRL, LlamaFactory |
| **数据库** | MySQL, DuckDB, Hive (基础) |
| **监控** | LangSmith, Phoenix |
| **工程** | Git, Docker, JupyterLab |

---

## 三大 Capstone 项目

### A. 广告素材生成 Agent
UP主/广告主输入产品信息 → Agent 自动生成文案+标题+封面描述 → 审核 → 优化迭代

### B. 商业化智能客服 Agent
B站广告主智能客服 → RAG 知识库 + 对话记忆 + 意图路由 + 工单创建

### C. 多 Agent 广告投放优化平台
数据分析 Agent + 策略制定 Agent + 素材生成 Agent + 执行 Agent 协作

---

## 快速开始

```bash
# 1. 克隆仓库
git clone <repo-url> && cd data-science-tutorial

# 2. 创建虚拟环境
python -m venv venv && source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置 API Keys
cp .env.example .env
# 编辑 .env 填入你的 API Keys

# 5. 启动 Jupyter
jupyter lab
```

---

## 参考资源

| 方向 | 推荐 |
|------|-----|
| LLM 基础 | Karpathy "Let's build GPT"; HuggingFace NLP Course |
| Prompt Eng | OpenAI Guide; Anthropic Docs |
| LangChain | 官方文档 + LangGraph Academy |
| AutoGen | 官方文档; Microsoft Agent Framework |
| RAG | LangChain RAG Tutorial; LlamaIndex Docs |
| OpenClaw | GitHub Repo + 知乎系列解析 |
| 微调 | HuggingFace PEFT; Unsloth 教程; LlamaFactory |
| Agent 工程 | Anthropic "Building Effective Agents"; Datawhale hello-agents |
