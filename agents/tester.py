from agents.base_agent import BaseAgent

class Tester(BaseAgent):
    def __init__(self):
        super().__init__("tester", "测试工程师")
    
    def get_system_prompt(self) -> str:
        return """你是一位专业的测试工程师，擅长设计和执行测试用例。

你的职责包括：
1. 设计测试用例和测试计划
2. 执行功能测试和回归测试
3. 发现和报告bug
4. 生成测试报告
5. 确保产品质量

请以专业的测试思维来保障产品质量。"""
