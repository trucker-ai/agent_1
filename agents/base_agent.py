from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from langchain_core.prompts import ChatPromptTemplate
from config.settings import settings

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.tools: List[BaseTool] = []
        self.memory = None
        self.cost_tracker = None
        self.task_planner = None
        self.use_mock = not settings.OPENAI_API_KEY or settings.ENVIRONMENT == "development"
    
    def set_tools(self, tools: List[BaseTool]):
        self.tools = tools
    
    def set_memory(self, memory):
        self.memory = memory
    
    def set_cost_tracker(self, cost_tracker):
        self.cost_tracker = cost_tracker
    
    def set_task_planner(self, task_planner):
        self.task_planner = task_planner
    
    @abstractmethod
    def get_system_prompt(self) -> str:
        pass
    
    def _get_mock_response(self, task: str) -> str:
        responses = {
            "分析需求": f"【{self.role}】需求分析完成：\n- 需求描述：{task}\n- 需求状态：已分析\n- 预计产出：PRD文档",
            "完善需求": f"【{self.role}】需求完善完成：\n- 需求已细化\n- 已编写需求文档\n- 优先级已确定",
            "评审需求": f"【{self.role}】需求评审完成：\n- 需求完整性：通过\n- 需求合理性：通过\n- 建议：无",
            "UI设计": f"【{self.role}】UI设计完成：\n- 设计风格：现代简约\n- 配色方案：已确定\n- 交互原型：已完成",
            "代码实现": f"【{self.role}】代码实现完成：\n- 功能开发：完成\n- 代码质量：良好\n- 测试覆盖：已编写",
            "代码审查": f"【{self.role}】代码审查完成：\n- 代码规范：符合标准\n- 潜在问题：无\n- 优化建议：无",
            "执行测试": f"【{self.role}】测试执行完成：\n- 测试用例：100%通过\n- Bug数量：0\n- 测试报告：已生成",
            "项目监控": f"【{self.role}】项目监控完成：\n- 进度：正常\n- 风险：无\n- 状态：进行中",
            "知识沉淀": f"【{self.role}】知识沉淀完成：\n- 文档已生成\n- 技能已注册\n- 经验已总结",
        }
        
        for key, response in responses.items():
            if key in task:
                return response
        
        return f"【{self.role}】正在处理任务: {task}\n\n处理结果:\n- 任务类型: {self.name}\n- 状态: 已完成\n- 产出: 任务已成功执行"
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        try:
            if self.use_mock:
                output = self._get_mock_response(task)
            else:
                llm = ChatOpenAI(model="gpt-4o-mini", api_key=settings.OPENAI_API_KEY)
                system_prompt = self.get_system_prompt()
                prompt = ChatPromptTemplate.from_messages([
                    ("system", system_prompt),
                    ("user", "{input}"),
                ])
                chain = prompt | llm
                result = chain.invoke({"input": task})
                output = result.content if hasattr(result, 'content') else str(result)
            
            if self.memory:
                self.memory.add_memory(
                    content=f"{self.name}执行任务: {task}\n结果: {output[:200]}",
                    metadata={"type": "task", "agent": self.name}
                )
            
            return {
                "success": True,
                "output": output,
                "type": self.name
            }
        
        except Exception as e:
            return {
                "success": False,
                "output": f"执行失败: {str(e)}",
                "type": self.name
            }
    
    def get_name(self) -> str:
        return self.name
    
    def log_task(self, task: str, result: str):
        if self.memory:
            self.memory.add_memory(
                content=f"任务日志\n任务: {task}\n结果: {result[:200]}",
                metadata={"type": "log", "agent": self.name}
            )
