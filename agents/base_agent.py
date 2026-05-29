from typing import Dict, Any, Optional
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.tools = []
        self.memory = None
        self.cost_tracker = None
        self.task_planner = None

    def set_tools(self, tools: list):
        self.tools = tools

    def set_memory(self, memory):
        self.memory = memory

    def set_cost_tracker(self, cost_tracker):
        self.cost_tracker = cost_tracker

    def set_task_planner(self, task_planner):
        self.task_planner = task_planner

    @abstractmethod
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        pass

    def get_available_tools(self) -> list:
        return self.tools

    def get_name(self) -> str:
        return self.name

    def log_task(self, task: str, result: str):
        if self.memory:
            self.memory.add_memory(
                content=f"Task: {task}\nResult: {result}",
                metadata={"agent": self.name, "task_type": "execution"}
            )

    def record_cost(self, service: str, operation: str, cost: float, usage: float):
        if self.cost_tracker:
            self.cost_tracker.record_cost(service, operation, cost, usage)
