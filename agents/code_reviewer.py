from agents.base_agent import BaseAgent

class CodeReviewer(BaseAgent):
    def __init__(self):
        super().__init__("code_reviewer", "代码审查员")
    
    def get_system_prompt(self) -> str:
        return """你是一位专业的代码审查专家，擅长对代码进行全面的质量检查。

你的职责包括：
1. 审查代码的正确性和安全性
2. 检查代码风格和规范
3. 评估代码的可维护性和可扩展性
4. 识别潜在的bug和性能问题
5. 提出改进建议

请以专业、严谨的态度进行代码审查。"""
