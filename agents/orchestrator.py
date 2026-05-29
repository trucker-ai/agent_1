from typing import Dict, Any, Optional, List

class Orchestrator:
    def __init__(self):
        self.agents: Dict[str, Any] = {}
        self.tools = []
        self.memory = None
        self.task_planner = None
        self.cost_tracker = None
    
    def register_agent(self, agent):
        self.agents[agent.get_name()] = agent
    
    def set_tools(self, tools: List[Any]):
        self.tools = tools
        for agent in self.agents.values():
            agent.set_tools(tools)
    
    def set_memory(self, memory):
        self.memory = memory
        for agent in self.agents.values():
            agent.set_memory(memory)
    
    def set_task_planner(self, task_planner):
        self.task_planner = task_planner
        for agent in self.agents.values():
            agent.set_task_planner(task_planner)
    
    def set_cost_tracker(self, cost_tracker):
        self.cost_tracker = cost_tracker
        for agent in self.agents.values():
            agent.set_cost_tracker(cost_tracker)
    
    def dispatch_task(self, agent_name: str, task: str, 
                      context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if agent_name not in self.agents:
            return {
                "success": False,
                "error": f"Agent not found: {agent_name}"
            }
        
        agent = self.agents[agent_name]
        return agent.execute(task, context)
    
    def list_agents(self) -> List[str]:
        return list(self.agents.keys())
    
    def get_system_status(self) -> Dict[str, Any]:
        return {
            "agents": {
                name: {"tools_count": len(agent.tools)}
                for name, agent in self.agents.items()
            },
            "tools": [tool.name for tool in self.tools],
            "memory_enabled": self.memory is not None,
            "task_planner_enabled": self.task_planner is not None,
            "cost_tracker_enabled": self.cost_tracker is not None
        }
