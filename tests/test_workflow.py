import pytest
from workflow import ProjectTeam


class TestProjectTeam:
    def test_project_team_initialization(self):
        team = ProjectTeam()
        assert team is not None
        assert len(team.list_agents()) > 0

    def test_list_agents(self):
        team = ProjectTeam()
        agents = team.list_agents()
        assert isinstance(agents, list)
        assert len(agents) > 0

    def test_list_workflows(self):
        team = ProjectTeam()
        workflows = team.list_available_workflows()
        assert isinstance(workflows, list)
        assert "需求到设计" in workflows
        assert "设计到开发" in workflows
        assert "开发到测试" in workflows
        assert "完整流程" in workflows

    def test_execute_workflow_requirement_to_design(self):
        team = ProjectTeam()
        result = team.execute_workflow("需求到设计", {"需求描述": "分析产品需求"})
        assert result["success"] is True
        assert "需求到设计" in result["workflow"]

    def test_execute_workflow_design_to_development(self):
        team = ProjectTeam()
        result = team.execute_workflow("设计到开发", {"需求描述": "开发一个功能"})
        assert result["success"] is True
        assert "设计到开发" in result["workflow"]

    def test_execute_workflow_development_to_test(self):
        team = ProjectTeam()
        result = team.execute_workflow("开发到测试", {"测试内容": "测试功能"})
        assert result["success"] is True
        assert "开发到测试" in result["workflow"]

    def test_execute_workflow_full_pipeline(self):
        team = ProjectTeam()
        result = team.execute_workflow("完整流程", {"需求描述": "完整项目流程"})
        assert result["success"] is True
        assert "完整流程" in result["workflow"]

    def test_assign_task(self):
        team = ProjectTeam()
        result = team.assign_task("product_manager", "分析需求")
        assert result["success"] is True
        assert "需求分析报告" in result["result"]["output"]

    def test_get_status(self):
        team = ProjectTeam()
        status = team.get_status()
        assert isinstance(status, dict)
        assert "orchestrator" in status
        assert "memory_entries" in status
        assert "tasks" in status
        assert "cost" in status

    def test_start_project(self):
        team = ProjectTeam()
        result = team.start_project("测试项目", "测试描述")
        assert result["success"] is True
        assert "测试项目" in result["message"]

    def test_unknown_workflow(self):
        team = ProjectTeam()
        result = team.execute_workflow("不存在的工作流", {})
        assert result["success"] is False
        assert "未知工作流" in result["error"]
