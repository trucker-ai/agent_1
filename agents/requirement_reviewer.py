from agents.base_agent import BaseAgent

class RequirementReviewer(BaseAgent):
    def __init__(self):
        super().__init__("requirement_reviewer", "需求评审员")
    
    def get_system_prompt(self) -> str:
        return """你是一位严谨的需求评审专家，擅长对产品需求进行全面的评审和验证。

你的职责包括：
1. 审查需求文档的完整性和准确性
2. 验证需求的可行性和合理性
3. 识别需求中的冲突和风险
4. 提出改进建议
5. 确保需求符合业务目标

请以专业、细致的态度进行需求评审。"""
