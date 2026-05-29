from typing import Dict, Any, Optional, TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from agents import (
    ProductManager, RequirementEngineer, RequirementReviewer,
    Designer, Developer, CodeReviewer, Tester, ProjectManager, KnowledgeEngineer
)
from memory import ProjectMemory
from cost_control import CostTracker
from tools import FileSystemTool, CodeExecutor, MCPAPIClient, SkillManager
from config.settings import settings

class WorkflowState(TypedDict):
    project_name: str
    task_description: str
    context: Dict[str, Any]
    results: List[Dict[str, Any]]
    current_agent: str
    step: int
    max_steps: int
    is_complete: bool
    error: Optional[str]

class LangGraphWorkflow:
    def __init__(self):
        self.memory = ProjectMemory()
        self.cost_tracker = CostTracker()
        self.skill_manager = SkillManager()
        
        self._initialize_agents()
        self._initialize_tools()
        self._build_graph()
    
    def _initialize_agents(self):
        self.agents = {
            "product_manager": ProductManager(),
            "requirement_engineer": RequirementEngineer(),
            "requirement_reviewer": RequirementReviewer(),
            "designer": Designer(),
            "developer": Developer(),
            "code_reviewer": CodeReviewer(),
            "tester": Tester(),
            "project_manager": ProjectManager(),
            "knowledge_engineer": KnowledgeEngineer()
        }
        
        for agent in self.agents.values():
            agent.set_memory(self.memory)
            agent.set_cost_tracker(self.cost_tracker)
    
    def _initialize_tools(self):
        self.tools = [
            FileSystemTool(),
            CodeExecutor(),
            MCPAPIClient(),
            self.skill_manager
        ]
        
        for agent in self.agents.values():
            agent.set_tools(self.tools)
    
    def _build_graph(self):
        workflow = StateGraph(WorkflowState)
        
        workflow.add_node("product_manager", self._run_product_manager)
        workflow.add_node("requirement_engineer", self._run_requirement_engineer)
        workflow.add_node("requirement_reviewer", self._run_requirement_reviewer)
        workflow.add_node("designer", self._run_designer)
        workflow.add_node("developer", self._run_developer)
        workflow.add_node("code_reviewer", self._run_code_reviewer)
        workflow.add_node("tester", self._run_tester)
        workflow.add_node("project_manager", self._run_project_manager)
        workflow.add_node("knowledge_engineer", self._run_knowledge_engineer)
        
        workflow.add_edge("product_manager", "requirement_engineer")
        workflow.add_edge("requirement_engineer", "requirement_reviewer")
        workflow.add_edge("requirement_reviewer", "designer")
        workflow.add_edge("designer", "developer")
        workflow.add_edge("developer", "code_reviewer")
        workflow.add_edge("code_reviewer", "tester")
        workflow.add_edge("tester", "project_manager")
        workflow.add_edge("project_manager", "knowledge_engineer")
        workflow.add_edge("knowledge_engineer", END)
        
        workflow.set_entry_point("product_manager")
        
        self.graph = workflow.compile()
    
    def _run_agent(self, state: WorkflowState, agent_name: str, task: str) -> WorkflowState:
        agent = self.agents.get(agent_name)
        if not agent:
            return {
                **state,
                "error": f"Agent not found: {agent_name}",
                "is_complete": True
            }
        
        result = agent.execute(task, state["context"])
        state["results"].append({
            "agent": agent_name,
            "task": task,
            "result": result
        })
        state["current_agent"] = agent_name
        state["step"] += 1
        
        self.memory.add_memory(
            content=f"{agent_name}执行任务: {task}\n结果: {result.get('output', '')[:200]}",
            metadata={"type": "task", "agent": agent_name}
        )
        
        return state
    
    def _run_product_manager(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "product_manager", "分析需求")
    
    def _run_requirement_engineer(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "requirement_engineer", "完善需求")
    
    def _run_requirement_reviewer(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "requirement_reviewer", "评审需求")
    
    def _run_designer(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "designer", "UI设计")
    
    def _run_developer(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "developer", "代码实现")
    
    def _run_code_reviewer(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "code_reviewer", "代码审查")
    
    def _run_tester(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "tester", "执行测试")
    
    def _run_project_manager(self, state: WorkflowState) -> WorkflowState:
        return self._run_agent(state, "project_manager", "项目监控")
    
    def _run_knowledge_engineer(self, state: WorkflowState) -> WorkflowState:
        state = self._run_agent(state, "knowledge_engineer", "知识沉淀")
        state["is_complete"] = True
        return state
    
    def execute_workflow(self, project_name: str, task_description: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        initial_state: WorkflowState = {
            "project_name": project_name,
            "task_description": task_description,
            "context": context or {},
            "results": [],
            "current_agent": "",
            "step": 0,
            "max_steps": 9,
            "is_complete": False,
            "error": None
        }
        
        self.memory.add_memory(
            content=f"项目初始化: {project_name}\n描述: {task_description}",
            metadata={"type": "project", "name": project_name}
        )
        
        final_state = self.graph.invoke(initial_state)
        
        return {
            "success": not final_state.get("error"),
            "project_name": project_name,
            "results": final_state["results"],
            "step": final_state["step"],
            "error": final_state.get("error"),
            "is_complete": final_state["is_complete"]
        }
    
    def execute_single_task(self, agent_name: str, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        agent = self.agents.get(agent_name)
        if not agent:
            return {"success": False, "error": f"Agent not found: {agent_name}"}
        
        result = agent.execute(task, context)
        self.memory.add_memory(
            content=f"{agent_name}执行任务: {task}\n结果: {result.get('output', '')[:200]}",
            metadata={"type": "task", "agent": agent_name}
        )
        
        return result
    
    def get_status(self) -> Dict[str, Any]:
        return {
            "agents": list(self.agents.keys()),
            "memory_entries": self.memory.get_memory_count(),
            "cost": self.cost_tracker.get_cost_summary()
        }
    
    def list_agents(self) -> List[str]:
        return list(self.agents.keys())
