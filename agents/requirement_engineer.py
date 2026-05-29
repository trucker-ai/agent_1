from typing import Dict, Any, Optional
from .base_agent import BaseAgent


class RequirementEngineer(BaseAgent):
    def __init__(self):
        super().__init__("requirement_engineer")

    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        result = {
            "success": True,
            "output": "",
            "type": "requirement"
        }

        if "完善需求" in task or "细化需求" in task:
            result["output"] = self._refine_requirement(task, context)
        elif "需求梳理" in task:
            result["output"] = self._organize_requirements(task, context)
        elif "用户故事" in task:
            result["output"] = self._generate_user_stories(task, context)
        else:
            result["output"] = f"需求工程师正在处理任务: {task}\n\n处理结果:\n- 任务类型: 需求工程\n- 状态: 进行中\n- 预计产出: 完善的需求文档"

        self.log_task(task, result["output"])
        return result

    def _refine_requirement(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""需求完善报告

原始需求: {task}

需求细化结果:

一、需求描述
根据原始需求，细化为以下具体需求点：

二、功能需求明细
| 需求ID | 需求描述 | 需求来源 | 优先级 |
|--------|----------|----------|--------|
| REQ-001 | 基础功能实现 | 原始需求 | P0 |
| REQ-002 | 用户交互设计 | 用户反馈 | P0 |
| REQ-003 | 数据持久化 | 技术需求 | P1 |
| REQ-004 | 性能优化 | 非功能需求 | P1 |

三、非功能需求
- 性能要求: 响应时间 < 200ms
- 可用性: 99.9%
- 安全性: 数据加密传输

四、验收标准
待与相关方确认"""

    def _organize_requirements(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""需求梳理报告

梳理任务: {task}

需求分类整理:

【功能需求】
- 核心功能: 实现产品核心价值的功能集合
- 辅助功能: 提升用户体验的附加功能
- 扩展功能: 未来可能需要的功能储备

【非功能需求】
- 性能需求: 系统响应速度、吞吐量要求
- 安全需求: 数据保护、访问控制要求
- 兼容性需求: 多平台、多浏览器支持

【接口需求】
- 内部接口: 系统模块间的交互规范
- 外部接口: 与第三方系统的集成要求

需求状态: 已梳理完成，待评审"""

    def _generate_user_stories(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""用户故事文档

任务: {task}

用户故事列表:

1. 作为[用户角色]，我希望[做某事]，以便[达到某个目的]
   - 验收标准: 明确的完成条件
   - 优先级: P0

2. 作为[用户角色]，我希望[做某事]，以便[达到某个目的]
   - 验收标准: 明确的完成条件
   - 优先级: P0

3. 作为[用户角色]，我希望[做某事]，以便[达到某个目的]
   - 验收标准: 明确的完成条件
   - 优先级: P1

4. 作为[用户角色]，我希望[做某事]，以便[达到某个目的]
   - 验收标准: 明确的完成条件
   - 优先级: P1

估算故事点数: 待评估"""
