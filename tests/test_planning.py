import pytest
from datetime import datetime
from planning import TaskPlanner, Task


class TestTask:
    def test_task_initialization(self):
        now = datetime.now()
        task = Task("test_id", "Test Task", "description", "pending", "high", "agent1", now, now)
        assert task.id == "test_id"
        assert task.title == "Test Task"
        assert task.status == "pending"
        assert task.priority == "high"
        assert task.assignee == "agent1"

    def test_task_transition(self):
        now = datetime.now()
        task = Task("test_id", "Test Task", "description", "pending", "high", "agent1", now, now)
        task.status = "in_progress"
        assert task.status == "in_progress"
        task.status = "completed"
        assert task.status == "completed"


class TestTaskPlanner:
    def test_task_planner_initialization(self):
        planner = TaskPlanner()
        assert planner is not None

    def test_create_task(self):
        planner = TaskPlanner()
        task_id = planner.create_task("Test Task", "description", priority="high", assignee="agent1")
        assert task_id is not None
        task = planner.get_task(task_id)
        assert task.title == "Test Task"
        assert task.status == "pending"

    def test_get_task(self):
        planner = TaskPlanner()
        task_id = planner.create_task("Test Task", "description")
        task = planner.get_task(task_id)
        assert task is not None
        assert task.title == "Test Task"

    def test_update_task(self):
        planner = TaskPlanner()
        task_id = planner.create_task("Test Task", "description")
        
        success = planner.update_task(task_id, title="Updated Task", status="in_progress")
        assert success is True
        
        task = planner.get_task(task_id)
        assert task.title == "Updated Task"
        assert task.status == "in_progress"

    def test_delete_task(self):
        planner = TaskPlanner()
        task_id = planner.create_task("Test Task", "description")
        
        success = planner.delete_task(task_id)
        assert success is True
        
        task = planner.get_task(task_id)
        assert task is None

    def test_list_tasks(self):
        planner = TaskPlanner()
        planner.create_task("Task 1", "description")
        planner.create_task("Task 2", "description")
        
        tasks = planner.list_tasks()
        assert len(tasks) == 2

    def test_list_tasks_by_status(self):
        planner = TaskPlanner()
        planner.create_task("Task 1", "description")
        planner.mark_task_in_progress("task-0000")
        planner.create_task("Task 2", "description")
        planner.mark_task_completed("task-0001")
        planner.create_task("Task 3", "description")
        
        pending_tasks = planner.list_tasks(status="pending")
        assert len(pending_tasks) == 1
        
        in_progress_tasks = planner.list_tasks(status="in_progress")
        assert len(in_progress_tasks) == 1
        
        completed_tasks = planner.list_tasks(status="completed")
        assert len(completed_tasks) == 1

    def test_list_tasks_by_assignee(self):
        planner = TaskPlanner()
        planner.create_task("Task 1", "description", assignee="agent1")
        planner.create_task("Task 2", "description", assignee="agent2")
        planner.create_task("Task 3", "description", assignee="agent1")
        
        agent1_tasks = planner.list_tasks(assignee="agent1")
        assert len(agent1_tasks) == 2
        
        agent2_tasks = planner.list_tasks(assignee="agent2")
        assert len(agent2_tasks) == 1

    def test_mark_task_in_progress(self):
        planner = TaskPlanner()
        task_id = planner.create_task("Test Task", "description")
        
        success = planner.mark_task_in_progress(task_id)
        assert success is True
        
        task = planner.get_task(task_id)
        assert task.status == "in_progress"

    def test_mark_task_completed(self):
        planner = TaskPlanner()
        task_id = planner.create_task("Test Task", "description")
        
        success = planner.mark_task_completed(task_id)
        assert success is True
        
        task = planner.get_task(task_id)
        assert task.status == "completed"

    def test_get_task_count(self):
        planner = TaskPlanner()
        planner.create_task("Task 1", "description")
        planner.create_task("Task 2", "description")
        
        assert planner.get_task_count() == 2

    def test_get_status_counts(self):
        planner = TaskPlanner()
        planner.create_task("Task 1", "description")
        planner.mark_task_in_progress("task-0000")
        planner.create_task("Task 2", "description")
        planner.mark_task_completed("task-0001")
        planner.create_task("Task 3", "description")
        
        counts = planner.get_status_counts()
        assert counts["pending"] == 1
        assert counts["in_progress"] == 1
        assert counts["completed"] == 1

    def test_get_tasks_by_status(self):
        planner = TaskPlanner()
        planner.create_task("Task 1", "description")
        planner.mark_task_in_progress("task-0000")
        planner.create_task("Task 2", "description")
        
        tasks = planner.get_tasks_by_status("pending")
        assert len(tasks) == 1

    def test_get_tasks_by_priority(self):
        planner = TaskPlanner()
        planner.create_task("Task 1", "description", priority="high")
        planner.create_task("Task 2", "description", priority="low")
        planner.create_task("Task 3", "description", priority="high")
        
        high_tasks = planner.get_tasks_by_priority("high")
        assert len(high_tasks) == 2

    def test_get_dependent_tasks(self):
        planner = TaskPlanner()
        task1_id = planner.create_task("Task 1", "description")
        task2_id = planner.create_task("Task 2", "description", dependencies=[task1_id])
        
        dependent_tasks = planner.get_dependent_tasks(task1_id)
        assert len(dependent_tasks) == 1
        assert dependent_tasks[0].id == task2_id

    def test_delete_task_clears_dependencies(self):
        planner = TaskPlanner()
        task1_id = planner.create_task("Task 1", "description")
        task2_id = planner.create_task("Task 2", "description", dependencies=[task1_id])
        
        planner.delete_task(task1_id)
        task2 = planner.get_task(task2_id)
        assert task1_id not in task2.dependencies
