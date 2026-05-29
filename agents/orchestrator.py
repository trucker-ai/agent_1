from typing import Dict, Any, Optional, List
from .base_agent import BaseAgent


class Orchestrator:
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}
        self.tools = []
        self.memory = None
        self.cost_tracker = None
        self.task_planner = None

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.get_name()] = agent

        if self.tools:
            agent.set_tools(self.tools)
        if self.memory:
            agent.set_memory(self.memory)
        if self.cost_tracker:
            agent.set_cost_tracker(self.cost_tracker)
        if self.task_planner:
            agent.set_task_planner(self.task_planner)

    def get_agent(self, agent_name: str) -> Optional[BaseAgent]:
        return self.agents.get(agent_name)

    def list_agents(self) -> List[str]:
        return list(self.agents.keys())

    def dispatch_task(self, agent_name: str, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        agent = self.get_agent(agent_name)

        if not agent:
            return {
                "success": False,
                "error": f"Agent not found: {agent_name}",
                "result": None
            }

        try:
            result = agent.execute(task, context)
            return {
                "success": True,
                "error": "",
                "result": result,
                "agent": agent_name
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "result": None,
                "agent": agent_name
            }

    def broadcast_message(self, message: str, context: Optional[Dict[str, Any]] = None):
        results = {}
        for agent_name, agent in self.agents.items():
            try:
                result = agent.execute(message, context)
                results[agent_name] = {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                results[agent_name] = {
                    "success": False,
                    "error": str(e)
                }
        return results

    def set_tools(self, tools: list):
        self.tools = tools
        for agent in self.agents.values():
            agent.set_tools(tools)

    def set_memory(self, memory):
        self.memory = memory
        for agent in self.agents.values():
            agent.set_memory(memory)

    def set_cost_tracker(self, cost_tracker):
        self.cost_tracker = cost_tracker
        for agent in self.agents.values():
            agent.set_cost_tracker(cost_tracker)

    def set_task_planner(self, task_planner):
        self.task_planner = task_planner
        for agent in self.agents.values():
            agent.set_task_planner(task_planner)

    def get_system_status(self) -> Dict[str, Any]:
        agent_status = {}
        for name, agent in self.agents.items():
            agent_status[name] = {
                "available": True,
                "tools_count": len(agent.get_available_tools())
            }

        cost_summary = {}
        if self.cost_tracker:
            cost_summary = self.cost_tracker.get_cost_summary()

        task_summary = {}
        if self.task_planner:
            task_summary = {
                "total_tasks": self.task_planner.get_task_count(),
                "status_counts": self.task_planner.get_status_counts()
            }

        return {
            "agents": agent_status,
            "cost": cost_summary,
            "tasks": task_summary,
            "total_agents": len(self.agents)
        }
