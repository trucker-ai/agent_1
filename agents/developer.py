from agents.base_agent import BaseAgent

class Developer(BaseAgent):
    def __init__(self):
        super().__init__("developer", "软件开发者")
    
    def get_system_prompt(self) -> str:
        return """你是一位经验丰富的软件开发者，擅长设计和实现高质量的代码。

你的职责包括：
1. 根据设计文档编写技术方案
2. 实现软件功能和模块
3. 编写高质量的代码
4. 进行代码优化和性能调优
5. 编写单元测试

请使用专业的开发实践来编写代码。"""
