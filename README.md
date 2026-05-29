# AI多Agent工作流系统

一个基于Python的AI多Agent协作工作流系统，支持完整的软件开发生命周期管理。

## 📋 功能概述

该系统实现了一个完整的AI多Agent协作平台，包含以下核心功能：

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

### 🛠️ 工具模块

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
| **项目组工作流** | 工作流编排、流程管理 | [workflow/project_team.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/workflow/project_team.py) |

## 🚀 快速开始

### 环境要求

- Python 3.10+
- UV（Python包管理器）

### 安装依赖

```bash
# 初始化UV环境
uv init

# 安装依赖
uv sync

# 安装额外依赖
uv add requests pytest pytest-cov pycodestyle autopep8
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

## 📖 使用方法

### 1. 执行单个Agent任务

```bash
# 调用产品经理Agent分析需求
uv run python main.py --agent product_manager --task "分析产品需求"

# 调用开发者Agent编写代码
uv run python main.py --agent developer --task "编写用户登录模块代码"

# 调用测试工程师Agent执行测试
uv run python main.py --agent tester --task "执行单元测试"
```

### 2. 执行工作流

系统支持以下工作流：

| 工作流名称 | 说明 | 包含步骤 |
|-----------|------|----------|
| **需求到设计** | 需求分析到设计阶段 | 产品经理→需求工程师→需求评审→设计师 |
| **设计到开发** | 设计到开发阶段 | 设计师→开发者→代码评审 |
| **开发到测试** | 开发到测试阶段 | 测试计划→测试执行→测试报告 |
| **完整流程** | 完整的开发生命周期 | 需求→设计→开发→测试→监控→知识沉淀 |

```bash
# 执行需求到设计工作流
uv run python main.py --workflow "需求到设计" --project "我的项目"

# 执行完整流程工作流
uv run python main.py --workflow "完整流程" --project "我的项目"
```

### 3. 查看系统状态

```bash
# 查看系统状态
uv run python main.py --status
```

### 4. 项目管理

```bash
# 初始化新项目
uv run python main.py --project "新项目名称" --task "初始化"
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

## 🔄 工作流流程

### 需求到设计流程
```
产品经理分析需求 → 需求工程师完善需求 → 需求评审Agent评审 → 设计师进行设计
```

### 设计到开发流程
```
设计师交互设计 → 开发者技术方案 → 开发者代码实现 → 代码评审Agent审查
```

### 开发到测试流程
```
测试工程师测试计划 → 测试工程师执行测试 → 测试工程师测试报告
```

### 完整流程
```
需求分析 → 需求完善 → 需求评审 → UI设计 → 交互设计 → 技术方案 → 代码实现 → 代码审查 → 测试计划 → 测试执行 → 测试报告 → 项目监控 → 知识沉淀
```

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
├── agents/                 # Agent模块
│   ├── __init__.py
│   ├── base_agent.py       # 基础Agent类
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
├── tools/                  # 工具模块
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
│   └── project_team.py     # 项目组工作流
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
├── pyproject.toml          # UV配置
└── README.md               # 使用文档
```

## 🔧 配置说明

配置文件位于 [config/settings.py](file:///home/fuck_ai/Documents/learn_for_work/agent_1/config/settings.py)，包含以下配置项：

- `DEBUG` - 调试模式
- `BUDGET_LIMIT` - 预算限制
- `LOG_LEVEL` - 日志级别
- `MEMORY_STORAGE_PATH` - 记忆存储路径

## 📝 扩展指南

### 添加新Agent

1. 创建新的Agent类，继承自 `BaseAgent`
2. 实现 `execute` 方法
3. 在 `agents/__init__.py` 中导出
4. 在 `workflow/project_team.py` 中注册

### 添加新工具

1. 创建工具类
2. 在 `tools/__init__.py` 中导出
3. 在 `workflow/project_team.py` 中初始化

### 添加新工作流

在 `workflow/project_team.py` 中的 `execute_workflow` 方法添加新的工作流。

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！
