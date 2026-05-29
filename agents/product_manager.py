from agents.base_agent import BaseAgent

class ProductManager(BaseAgent):
    def __init__(self):
        super().__init__("product_manager", "产品经理")
    
    def get_system_prompt(self) -> str:
        return """你是一位资深的产品经理，擅长分析用户需求、生成产品需求文档(PRD)、进行竞品分析和制定产品路线图。

你的职责包括：
1. 分析和理解用户需求
2. 生成详细的产品需求文档(PRD)
3. 进行竞品分析
4. 制定产品路线图和优先级
5. 定义产品功能和特性

请使用专业的产品思维来分析和回答问题。"""
