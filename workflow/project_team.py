from typing import Dict, Any, Optional, List
from agents import Orchestrator, ProductManager, RequirementEngineer, RequirementReviewer, Designer, Developer, CodeReviewer, Tester, ProjectManager, KnowledgeEngineer
from memory import ProjectMemory
from planning import TaskPlanner
from cost_control import CostTracker
from tools import FileSystemTool, CodeExecutor, MCPAPIClient, SkillManager


class ProjectTeam:
    def __init__(self):
        self.orchestrator = Orchestrator()
        self.memory = ProjectMemory()
        self.task_planner = TaskPlanner()
        self.cost_tracker = CostTracker()
        self.skill_manager = SkillManager()

        self._initialize_agents()
        self._initialize_tools()

    def _initialize_agents(self):
        self.orchestrator.register_agent(ProductManager())
        self.orchestrator.register_agent(RequirementEngineer())
        self.orchestrator.register_agent(RequirementReviewer())
        self.orchestrator.register_agent(Designer())
        self.orchestrator.register_agent(Developer())
        self.orchestrator.register_agent(CodeReviewer())
        self.orchestrator.register_agent(Tester())
        self.orchestrator.register_agent(ProjectManager())
        self.orchestrator.register_agent(KnowledgeEngineer())

        self.orchestrator.set_memory(self.memory)
        self.orchestrator.set_task_planner(self.task_planner)
        self.orchestrator.set_cost_tracker(self.cost_tracker)

    def _initialize_tools(self):
        tools = [
            FileSystemTool(),
            CodeExecutor(),
            MCPAPIClient(),
            self.skill_manager
        ]
        self.orchestrator.set_tools(tools)

    def start_project(self, project_name: str, description: str = ""):
        self.memory.add_memory(
            content=f"项目初始化\n名称: {project_name}\n描述: {description}",
            metadata={"type": "project", "name": project_name}
        )

        self.task_planner.create_task(
            title="需求分析",
            description="分析项目需求，生成PRD文档",
            priority="high",
            assignee="product_manager"
        )

        return {
            "success": True,
            "message": f"项目 '{project_name}' 已初始化",
            "agents": self.orchestrator.list_agents()
        }

    def execute_workflow(self, workflow_name: str, context: Optional[Dict[str, Any]] = None):
        workflows = {
            "需求到设计": self._workflow_requirement_to_design,
            "设计到开发": self._workflow_design_to_development,
            "开发到测试": self._workflow_development_to_test,
            "完整流程": self._workflow_full_pipeline
        }

        if workflow_name not in workflows:
            return {
                "success": False,
                "error": f"未知工作流: {workflow_name}"
            }

        return workflows[workflow_name](context)

    def _workflow_requirement_to_design(self, context: Optional[Dict[str, Any]] = None):
        results = []

        results.append(self.orchestrator.dispatch_task(
            "product_manager", "分析需求", context))
        results.append(self.orchestrator.dispatch_task(
            "requirement_engineer", "完善需求", context))
        results.append(self.orchestrator.dispatch_task(
            "requirement_reviewer", "评审需求", context))
        results.append(self.orchestrator.dispatch_task(
            "designer", "UI设计", context))

        return {
            "success": all(r["success"] for r in results),
            "results": results,
            "workflow": "需求到设计"
        }

    def _workflow_design_to_development(self, context: Optional[Dict[str, Any]] = None):
        results = []

        results.append(self.orchestrator.dispatch_task(
            "designer", "交互设计", context))
        results.append(self.orchestrator.dispatch_task(
            "developer", "技术方案", context))
        results.append(self.orchestrator.dispatch_task(
            "developer", "代码实现", context))
        results.append(self.orchestrator.dispatch_task(
            "code_reviewer", "代码审查", context))

        return {
            "success": all(r["success"] for r in results),
            "results": results,
            "workflow": "设计到开发"
        }

    def _workflow_development_to_test(self, context: Optional[Dict[str, Any]] = None):
        results = []

        results.append(self.orchestrator.dispatch_task(
            "tester", "测试计划", context))
        results.append(self.orchestrator.dispatch_task(
            "tester", "执行测试", context))
        results.append(self.orchestrator.dispatch_task(
            "tester", "测试报告", context))

        return {
            "success": all(r["success"] for r in results),
            "results": results,
            "workflow": "开发到测试"
        }

    def _workflow_full_pipeline(self, context: Optional[Dict[str, Any]] = None):
        results = []

        results.extend(
            self._workflow_requirement_to_design(context)["results"])
        results.extend(
            self._workflow_design_to_development(context)["results"])
        results.extend(self._workflow_development_to_test(context)["results"])

        results.append(self.orchestrator.dispatch_task(
            "project_manager", "项目监控", context))
        results.append(self.orchestrator.dispatch_task(
            "knowledge_engineer", "知识沉淀", context))

        return {
            "success": all(r["success"] for r in results),
            "results": results,
            "workflow": "完整流程"
        }

    def get_status(self) -> Dict[str, Any]:
        return {
            "orchestrator": self.orchestrator.get_system_status(),
            "memory_entries": self.memory.get_memory_count(),
            "tasks": {
                "total": self.task_planner.get_task_count(),
                "status": self.task_planner.get_status_counts()
            },
            "cost": self.cost_tracker.get_cost_summary()
        }

    def assign_task(self, agent_name: str, task: str, context: Optional[Dict[str, Any]] = None):
        return self.orchestrator.dispatch_task(agent_name, task, context)

    def list_available_workflows(self) -> List[str]:
        return ["需求到设计", "设计到开发", "开发到测试", "完整流程"]

    def list_agents(self) -> List[str]:
        return self.orchestrator.list_agents()
