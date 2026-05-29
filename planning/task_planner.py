from datetime import datetime
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class Task:
    id: str
    title: str
    description: str
    status: str
    priority: str
    assignee: str
    created_at: datetime
    updated_at: datetime
    dependencies: List[str] = None

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "assignee": self.assignee,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "dependencies": self.dependencies
        }


class TaskPlanner:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.task_counter = 0

    def create_task(self, title: str, description: str, priority: str = "medium", assignee: str = "", dependencies: Optional[List[str]] = None) -> str:
        if dependencies is None:
            dependencies = []

        task_id = f"task-{self.task_counter:04d}"
        self.task_counter += 1

        task = Task(
            id=task_id,
            title=title,
            description=description,
            status="pending",
            priority=priority,
            assignee=assignee,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            dependencies=dependencies
        )

        self.tasks[task_id] = task
        return task_id

    def get_task(self, task_id: str) -> Optional[Task]:
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, **kwargs) -> bool:
        if task_id not in self.tasks:
            return False

        task = self.tasks[task_id]

        if "title" in kwargs:
            task.title = kwargs["title"]
        if "description" in kwargs:
            task.description = kwargs["description"]
        if "status" in kwargs:
            task.status = kwargs["status"]
        if "priority" in kwargs:
            task.priority = kwargs["priority"]
        if "assignee" in kwargs:
            task.assignee = kwargs["assignee"]
        if "dependencies" in kwargs:
            task.dependencies = kwargs["dependencies"]

        task.updated_at = datetime.now()
        return True

    def delete_task(self, task_id: str) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            for task in self.tasks.values():
                if task_id in task.dependencies:
                    task.dependencies.remove(task_id)
            return True
        return False

    def list_tasks(self, status: str = None, assignee: str = None) -> List[Task]:
        result = list(self.tasks.values())

        if status:
            result = [task for task in result if task.status == status]

        if assignee:
            result = [task for task in result if task.assignee == assignee]

        return sorted(result, key=lambda x: x.created_at)

    def get_tasks_by_status(self, status: str) -> List[Task]:
        return [task for task in self.tasks.values() if task.status == status]

    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        return [task for task in self.tasks.values() if task.priority == priority]

    def get_task_count(self) -> int:
        return len(self.tasks)

    def get_status_counts(self) -> Dict[str, int]:
        counts = {
            "pending": 0,
            "in_progress": 0,
            "completed": 0
        }

        for task in self.tasks.values():
            if task.status in counts:
                counts[task.status] += 1

        return counts

    def get_dependent_tasks(self, task_id: str) -> List[Task]:
        return [
            task for task in self.tasks.values()
            if task_id in task.dependencies
        ]

    def mark_task_in_progress(self, task_id: str) -> bool:
        return self.update_task(task_id, status="in_progress")

    def mark_task_completed(self, task_id: str) -> bool:
        return self.update_task(task_id, status="completed")

    def reset(self):
        self.tasks.clear()
        self.task_counter = 0
