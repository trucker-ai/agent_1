from typing import Dict, Any, Optional
from .base_agent import BaseAgent


class ProductManager(BaseAgent):
    def __init__(self):
        super().__init__("product_manager")

    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        result = {
            "success": True,
            "output": "",
            "type": "prd"
        }

        if "需求分析" in task or "分析需求" in task:
            result["output"] = self._analyze_requirements(task, context)
        elif "PRD" in task or "产品需求文档" in task:
            result["output"] = self._generate_prd(task, context)
        elif "竞品分析" in task:
            result["output"] = self._competitive_analysis(task, context)
        else:
            result["output"] = f"产品经理正在处理任务: {task}\n\n分析结果:\n- 任务类型: 产品规划\n- 状态: 进行中\n- 预计产出: 需求文档或PRD"

        self.log_task(task, result["output"])
        return result

    def _analyze_requirements(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""需求分析报告

任务: {task}

需求要点:
1. 业务目标: 明确产品要解决的核心问题
2. 用户群体: 目标用户画像和使用场景
3. 功能需求: 核心功能列表和优先级
4. 非功能需求: 性能、安全、可用性要求

分析结论:
- 需求清晰程度: 待评估
- 优先级建议: 待确定
- 潜在风险: 待识别

下一步建议: 进行详细需求收集和用户调研"""

    def _generate_prd(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        ctx = context or {}
        return f"""产品需求文档 (PRD)

项目名称: {ctx.get('project_name', '未命名项目')}
文档版本: 1.0
创建时间: 自动生成

一、产品概述
本产品旨在解决用户的核心痛点，提供高效、便捷的解决方案。

二、需求清单
| 序号 | 需求描述 | 优先级 | 来源 |
|------|----------|--------|------|
| 1 | 核心功能A | P0 | 用户反馈 |
| 2 | 核心功能B | P0 | 业务需求 |
| 3 | 辅助功能C | P1 | 竞品分析 |

三、用户故事
作为用户，我希望能够...以便...

四、验收标准
待定义

五、里程碑计划
待制定"""

    def _competitive_analysis(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""竞品分析报告

分析任务: {task}

竞品概况:
1. 竞品A: 市场份额领先，功能完善，价格较高
2. 竞品B: 性价比高，用户体验良好，功能有限
3. 竞品C: 创新型产品，技术领先，市场推广中

优势分析:
- 我们的差异化优势: 待确定
- 机会点: 待挖掘

建议策略: 基于竞品分析制定差异化竞争策略"""
