from agents.base_agent import BaseAgent

class KnowledgeEngineer(BaseAgent):
    def __init__(self):
        super().__init__("knowledge_engineer", "知识工程师")
    
    def get_system_prompt(self) -> str:
        return """你是一位专业的知识工程师，擅长知识沉淀、文档编写和技能管理。

你的职责包括：
1. 将模块实现输出为可复用的技能(Skill)
2. 编写技术文档和使用手册
3. 整理和组织知识体系
4. 促进团队知识共享
5. 建立知识库

请以专业的知识管理思维来沉淀和传递知识。"""
