from agents.base_agent import BaseAgent

class RequirementEngineer(BaseAgent):
    def __init__(self):
        super().__init__("requirement_engineer", "需求工程师")
    
    def get_system_prompt(self) -> str:
        return """你是一位专业的需求工程师，擅长收集、分析和完善产品需求。

你的职责包括：
1. 收集和整理用户需求
2. 分析需求的可行性和优先级
3. 编写详细的需求文档
4. 与相关方沟通确认需求
5. 管理需求变更

请使用结构化的方式来分析和完善需求。"""
