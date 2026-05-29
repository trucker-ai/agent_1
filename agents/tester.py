from typing import Dict, Any, Optional
from .base_agent import BaseAgent


class Tester(BaseAgent):
    def __init__(self):
        super().__init__("tester")

    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        result = {
            "success": True,
            "output": "",
            "type": "test"
        }

        if "执行测试" in task or "测试用例" in task:
            result["output"] = self._execute_tests(task, context)
        elif "测试计划" in task:
            result["output"] = self._create_test_plan(task, context)
        elif "测试报告" in task:
            result["output"] = self._generate_test_report(task, context)
        else:
            result["output"] = f"测试工程师正在处理任务: {task}\n\n测试结果:\n- 任务类型: 软件测试\n- 状态: 进行中\n- 预计产出: 测试报告"

        self.log_task(task, result["output"])
        return result

    def _execute_tests(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""测试执行报告

测试任务: {task}

执行结果:

一、测试概述
- 测试类型: 单元测试 / 集成测试 / 系统测试
- 测试环境: 测试环境
- 执行时间: 自动生成

二、测试用例执行
| 模块 | 用例数 | 通过 | 失败 | 跳过 |
|------|--------|------|------|------|
| 模块A | 10 | 8 | 2 | 0 |
| 模块B | 8 | 7 | 1 | 0 |
| 模块C | 5 | 5 | 0 | 0 |

三、失败用例详情
1. 用例ID: TC-001
   - 测试描述: 测试功能A
   - 失败原因: 断言失败
   - 预期结果: 期望值
   - 实际结果: 实际值

2. 用例ID: TC-002
   - 测试描述: 测试功能B
   - 失败原因: 超时
   - 预期结果: 操作成功
   - 实际结果: 超时错误

四、测试覆盖率
- 代码覆盖率: 75%
- 分支覆盖率: 65%

五、执行结论
测试状态: 部分通过
建议: 修复失败用例后重新测试"""

    def _create_test_plan(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""测试计划

任务: {task}

计划内容:

一、测试范围
- 核心功能模块
- 新增功能模块
- 关键路径测试

二、测试策略
| 测试类型 | 覆盖范围 | 优先级 |
|----------|----------|--------|
| 单元测试 | 单个函数/方法 | P0 |
| 集成测试 | 模块间交互 | P0 |
| 系统测试 | 端到端流程 | P1 |
| 性能测试 | 性能指标 | P1 |
| 安全测试 | 安全漏洞 | P1 |

三、测试进度
- 阶段1: 单元测试 (1周)
- 阶段2: 集成测试 (1周)
- 阶段3: 系统测试 (1周)
- 阶段4: 回归测试 (0.5周)

四、测试环境
- 操作系统: Linux/Ubuntu
- 数据库: PostgreSQL
- 浏览器: Chrome/Firefox

五、测试交付物
- 测试用例文档
- 测试执行报告
- 缺陷跟踪报告"""

    def _generate_test_report(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""测试报告

报告任务: {task}

报告内容:

一、项目概述
项目名称: {context.get('project_name', '未命名项目')}
报告版本: 1.0
生成时间: 自动生成

二、测试执行摘要
- 总用例数: 待执行
- 通过数: 待统计
- 失败数: 待统计
- 通过率: 待计算

三、缺陷统计
| 严重程度 | 数量 | 状态 |
|----------|------|------|
| 致命 | 0 | 待确认 |
| 严重 | 2 | 修复中 |
| 一般 | 5 | 待修复 |
| 轻微 | 3 | 待评估 |

四、测试结论
测试状态: 待执行
是否通过: 待评估

五、建议
- 建议修复严重级别缺陷
- 建议优化测试覆盖率
- 建议添加更多边界测试用例"""
