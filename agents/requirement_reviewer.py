from typing import Dict, Any, Optional
from .base_agent import BaseAgent


class RequirementReviewer(BaseAgent):
    def __init__(self):
        super().__init__("requirement_reviewer")

    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        result = {
            "success": True,
            "output": "",
            "type": "review"
        }

        if "评审需求" in task or "需求评审" in task:
            result["output"] = self._review_requirements(task, context)
        elif "验证需求" in task:
            result["output"] = self._validate_requirements(task, context)
        elif "需求检查" in task:
            result["output"] = self._check_requirements(task, context)
        else:
            result["output"] = f"需求评审员正在处理任务: {task}\n\n评审结果:\n- 任务类型: 需求评审\n- 状态: 进行中\n- 预计产出: 评审报告"

        self.log_task(task, result["output"])
        return result

    def _review_requirements(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""需求评审报告

评审任务: {task}

评审结果:

一、需求完整性评估
- [ ] 需求描述清晰明确
- [ ] 功能点覆盖全面
- [ ] 业务规则完整
- [ ] 异常场景考虑

二、需求合理性评估
- [ ] 技术可行性
- [ ] 业务价值
- [ ] 优先级合理
- [ ] 资源预估合理

三、发现的问题
1. 问题一: 需求描述不够详细，存在歧义
2. 问题二: 部分需求缺少验收标准
3. 问题三: 技术可行性待验证

四、改进建议
- 建议补充需求细节说明
- 建议明确验收标准
- 建议进行技术方案评审

五、评审结论
评审状态: 需修改
评审人: 需求评审Agent
评审时间: 自动生成"""

    def _validate_requirements(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""需求验证报告

验证任务: {task}

验证维度:

【正确性验证】
- 需求是否符合业务目标: 待验证
- 需求是否与其他需求冲突: 待检查
- 需求是否可测试: 待评估

【完整性验证】
- 功能需求是否完整: 待评估
- 非功能需求是否明确: 待评估
- 接口需求是否清晰: 待评估

【一致性验证】
- 需求术语是否一致: 待检查
- 需求优先级是否合理: 待检查

验证结果: 待完成验证"""

    def _check_requirements(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""需求检查清单

检查任务: {task}

检查项:

□ 需求描述清晰无歧义
□ 需求有明确的验收标准
□ 需求优先级已确定
□ 需求不与其他需求冲突
□ 需求具有可测试性
□ 需求考虑了异常情况
□ 需求符合业务目标
□ 需求技术上可行

检查结果:
通过项: 0/{len(self._get_check_items())}
待完善项: 待检查

建议: 根据检查结果完善需求文档"""

    def _get_check_items(self):
        return [
            "需求描述清晰无歧义",
            "需求有明确的验收标准",
            "需求优先级已确定",
            "需求不与其他需求冲突",
            "需求具有可测试性",
            "需求考虑了异常情况",
            "需求符合业务目标",
            "需求技术上可行"
        ]
