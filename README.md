# AI多Agent工作流系统

一个基于 **LangChain/LangGraph** 的AI多Agent协作工作流系统，支持完整的软件开发生命周期管理。

## 📋 功能概述

该系统实现了一个完整的AI多Agent协作平台，基于 LangChain 和 LangGraph 框架构建，包含以下核心功能：

### 🔧 核心组件

| 组件 | 说明 | 文件路径 |
|------|------|----------|
| **主控大脑** | Agent注册、任务分发、系统协调 | [agents/orchestrator.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/orchestrator.py) |
| **产品经理Agent** | 需求分析、PRD生成、竞品分析 | [agents/product_manager.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/product_manager.py) |
| **需求工程师Agent** | 需求完善、需求分析、文档编写 | [agents/requirement_engineer.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/requirement_engineer.py) |
| **需求评审Agent** | 需求评审、合规检查、风险评估 | [agents/requirement_reviewer.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/requirement_reviewer.py) |
| **设计师Agent** | UI设计、交互设计、原型设计 | [agents/designer.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/designer.py) |
| **开发者Agent** | 技术方案、代码实现、架构设计 | [agents/developer.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/developer.py) |
| **代码评审Agent** | 代码审查、质量检查、安全审计 | [agents/code_reviewer.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/code_reviewer.py) |
| **测试工程师Agent** | 测试计划、测试执行、测试报告 | [agents/tester.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/tester.py) |
| **项目经理Agent** | 项目监控、进度跟踪、风险评估 | [agents/project_manager.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/project_manager.py) |
| **知识工程Agent** | Skill生成、文档输出、知识沉淀 | [agents/knowledge_engineer.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/agents/knowledge_engineer.py) |

### 🛠️ 工具模块（基于 LangChain BaseTool）

| 工具 | 说明 | 文件路径 |
|------|------|----------|
| **文件系统工具** | 文件读写、目录操作、路径管理 | [tools/file_system.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/tools/file_system.py) |
| **代码执行工具** | Python代码执行、沙箱隔离 | [tools/code_executor.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/tools/code_executor.py) |
| **MCP客户端** | MCP服务调用、工具注册 | [tools/mcp_client.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/tools/mcp_client.py) |
| **Skill管理器** | Skill注册、发现、执行 | [tools/skill_manager.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/tools/skill_manager.py) |

### 🧠 支持模块

| 模块 | 说明 | 文件路径 |
|------|------|----------|
| **项目记忆系统** | 持久化存储、搜索查询 | [memory/project_memory.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/memory/project_memory.py) |
| **任务规划器** | 任务管理、状态追踪 | [planning/task_planner.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/planning/task_planner.py) |
| **成本追踪器** | API成本管理、预算控制 | [cost_control/cost_tracker.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/cost_control/cost_tracker.py) |
| **项目组工作流** | 原有工作流编排 | [workflow/project_team.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/workflow/project_team.py) |
| **LangGraph工作流** | 基于LangGraph的有向图工作流 | [workflow/langgraph_workflow.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/workflow/langgraph_workflow.py) |

## 🚀 快速开始

### 环境要求

- Python 3.10+
- UV（Python包管理器）

### 安装依赖

```bash
# 初始化UV环境（如未初始化）
uv init

# 安装依赖
uv sync
```

### 启动系统

```bash
# 查看帮助信息
uv run python main.py --help

# 列出所有可用Agent
uv run python main.py --list-agents

# 列出所有可用工作流
uv run python main.py --list-workflows
```

### 使用 Docker 运行

```bash
# 构建镜像
docker build -t agent-workflow .

# 运行容器
docker run -it --rm -v "$(pwd)/.env:/app/.env" agent-workflow --status

# 使用 docker-compose（推荐）
docker-compose up --build
```

## 📖 使用方法

### 1. 使用原有模式

```bash
# 列出Agent
uv run python main.py --list-agents

# 执行工作流
uv run python main.py --workflow "完整流程" --project "我的项目"

# 执行单个任务
uv run python main.py --agent product_manager --task "分析需求"
```

### 2. 使用 LangGraph 模式

```bash
# 使用 LangGraph 模式列出Agent
uv run python main.py --langgraph --list-agents

# 使用 LangGraph 模式执行单个任务
uv run python main.py --langgraph --agent product_manager --task "分析需求"

# 使用 LangGraph 模式执行完整工作流
uv run python main.py --langgraph --project "我的项目"
```

### 3. 查看系统状态

```bash
# 查看系统状态（原有模式）
uv run python main.py --status

# 查看系统状态（LangGraph模式）
uv run python main.py --langgraph --status
```

## 🔄 LangGraph 工作流

### 工作流架构

LangGraph 使用有向图定义工作流，节点顺序如下：

```
产品经理 → 需求工程师 → 需求评审 → 设计师 → 开发者 → 代码审查 → 测试 → 项目经理 → 知识工程 → END
```

### 工作流状态管理

工作流使用 `WorkflowState` 进行状态管理：

```python
class WorkflowState(TypedDict):
    project_name: str        # 项目名称
    task_description: str    # 任务描述
    context: Dict[str, Any]  # 上下文信息
    results: List[...]       # 执行结果列表
    current_agent: str       # 当前执行的Agent
    step: int                # 当前步骤
    max_steps: int           # 最大步骤数
    is_complete: bool        # 是否完成
    error: Optional[str]     # 错误信息
```

## 🧩 Agent功能详解

### 产品经理Agent

**支持的任务：**
- `分析需求` / `需求分析` - 分析产品需求
- `生成PRD` / `产品需求文档` - 生成产品需求文档
- `竞品分析` - 进行竞品分析

### 需求工程师Agent

**支持的任务：**
- `完善需求` / `需求完善` - 完善需求文档
- `需求分析` - 深入分析需求
- `编写文档` - 编写需求文档

### 需求评审Agent

**支持的任务：**
- `评审需求` / `需求评审` - 评审需求文档
- `合规检查` - 检查合规性
- `风险评估` - 评估需求风险

### 设计师Agent

**支持的任务：**
- `UI设计` - 设计UI界面
- `交互设计` - 设计交互流程
- `原型设计` - 创建产品原型

### 开发者Agent

**支持的任务：**
- `编写代码` / `代码实现` - 编写代码
- `技术方案` - 设计技术方案
- `架构设计` - 设计系统架构

### 代码评审Agent

**支持的任务：**
- `代码审查` / `代码检查` - 审查代码质量
- `安全审计` - 安全漏洞检查
- `性能分析` - 性能分析

### 测试工程师Agent

**支持的任务：**
- `执行测试` / `测试执行` - 执行测试用例
- `测试计划` - 制定测试计划
- `测试报告` - 生成测试报告

### 项目经理Agent

**支持的任务：**
- `项目监控` / `进度监控` - 监控项目进度
- `项目规划` - 规划项目计划
- `风险评估` - 评估项目风险
- `检查方向` / `偏离方向` - 检查项目方向是否偏离

### 知识工程Agent

**支持的任务：**
- `生成Skill` / `输出Skill` - 将模块输出为Skill
- `生成文档` / `输出文档` - 生成文档
- `知识沉淀` - 沉淀项目知识

## 📊 成本管理

系统内置成本追踪功能，支持：

- API调用次数统计
- 费用记录
- 预算管理
- 预算告警

配置文件：[config/settings.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/config/settings.py)

## 🧠 知识沉淀

知识工程Agent会自动将每个模块的成功实现输出为Skill或文档，实现：

- Skill注册和复用
- 文档生成和存储
- 跨模块知识传递

## 🧪 测试

```bash
# 运行所有测试
uv run pytest tests/ -v

# 运行测试并生成覆盖率报告
uv run pytest tests/ -v --cov=agents --cov=tools --cov=memory --cov=planning --cov=cost_control --cov=workflow --cov-report=term-missing

# 检查代码风格
uv run pycodestyle agents/ tools/ memory/ planning/ cost_control/ workflow/
```

## 📁 项目结构

```
agent_1/
├── agents/                 # Agent模块（基于LangChain）
│   ├── __init__.py
│   ├── base_agent.py       # 基础Agent类（使用ChatPromptTemplate）
│   ├── orchestrator.py     # 主控大脑
│   ├── product_manager.py  # 产品经理
│   ├── requirement_engineer.py  # 需求工程师
│   ├── requirement_reviewer.py  # 需求评审
│   ├── designer.py         # 设计师
│   ├── developer.py        # 开发者
│   ├── code_reviewer.py    # 代码评审
│   ├── tester.py           # 测试工程师
│   ├── project_manager.py  # 项目经理
│   └── knowledge_engineer.py # 知识工程
├── tools/                  # 工具模块（基于LangChain BaseTool）
│   ├── __init__.py
│   ├── file_system.py      # 文件系统工具
│   ├── code_executor.py    # 代码执行工具
│   ├── mcp_client.py       # MCP客户端
│   └── skill_manager.py    # Skill管理器
├── memory/                 # 记忆模块
│   ├── __init__.py
│   └── project_memory.py   # 项目记忆系统
├── planning/               # 规划模块
│   ├── __init__.py
│   └── task_planner.py     # 任务规划器
├── cost_control/           # 成本控制模块
│   ├── __init__.py
│   └── cost_tracker.py     # 成本追踪器
├── workflow/               # 工作流模块
│   ├── __init__.py
│   ├── project_team.py     # 项目组工作流（原有模式）
│   └── langgraph_workflow.py # LangGraph工作流（新模式）
├── config/                 # 配置模块
│   └── settings.py         # 配置文件
├── tests/                  # 测试模块
│   ├── test_agents.py
│   ├── test_tools.py
│   ├── test_memory.py
│   ├── test_planning.py
│   ├── test_cost_control.py
│   └── test_workflow.py
├── main.py                 # 入口文件
├── pyproject.toml          # UV配置（包含LangChain依赖）
└── README.md               # 使用文档
```

## 🔧 配置说明

配置文件位于 [config/settings.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/config/settings.py)，包含以下配置项：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `ENVIRONMENT` | 运行环境 | `development` |
| `OPENAI_API_KEY` | OpenAI API密钥 | 空 |
| `OPENAI_API_BASE` | OpenAI API地址 | `https://api.openai.com/v1` |
| `LOG_LEVEL` | 日志级别 | `INFO` |
| `MAX_API_CALLS` | 最大API调用次数 | `1000` |
| `COST_LIMIT` | 成本限制（美元） | `100.0` |

### 环境变量配置

创建 `.env` 文件：

```env
ENVIRONMENT=development
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1
LOG_LEVEL=INFO
MAX_API_CALLS=1000
COST_LIMIT=100.0
```

## 📝 扩展指南

### 添加新Agent

1. 创建新的Agent类，继承自 `BaseAgent`
2. 实现 `get_system_prompt()` 方法
3. 在 `agents/__init__.py` 中导出
4. 在 `workflow/langgraph_workflow.py` 中注册

### 添加新工具

1. 创建工具类，继承自 `langchain_core.tools.BaseTool`
2. 定义输入参数模型（继承自 `BaseModel`）
3. 实现 `_run()` 和 `_arun()` 方法
4. 在 `tools/__init__.py` 中导出

### 添加新工作流节点

在 `workflow/langgraph_workflow.py` 中的 `_build_graph()` 方法添加新节点和边。

## 🛠️ 技术栈

| 框架/库 | 版本 | 用途 |
|---------|------|------|
| Python | 3.10+ | 编程语言 |
| LangChain | 1.3+ | LLM集成和工具调用 |
| LangGraph | 1.2+ | 工作流编排 |
| LangChain-OpenAI | 1.2+ | OpenAI LLM集成 |
| Pydantic | 2.0+ | 数据验证 |
| UV | latest | 包管理器 |

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！
