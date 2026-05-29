import pytest
from agents import (
    Orchestrator,
    ProductManager,
    RequirementEngineer,
    RequirementReviewer,
    Designer,
    Developer,
    CodeReviewer,
    Tester,
    ProjectManager,
    KnowledgeEngineer
)


class TestOrchestrator:
    def test_orchestrator_initialization(self):
        orchestrator = Orchestrator()
        assert orchestrator is not None
        assert len(orchestrator.list_agents()) == 0

    def test_register_agent(self):
        orchestrator = Orchestrator()
        agent = ProductManager()
        orchestrator.register_agent(agent)
        assert "product_manager" in orchestrator.list_agents()

    def test_dispatch_task(self):
        orchestrator = Orchestrator()
        agent = ProductManager()
        orchestrator.register_agent(agent)
        
        result = orchestrator.dispatch_task("product_manager", "分析需求")
        assert result["success"] is True
        assert "需求分析报告" in result["result"]["output"]


class TestProductManager:
    def test_product_manager_initialization(self):
        agent = ProductManager()
        assert agent.get_name() == "product_manager"

    def test_execute_task(self):
        agent = ProductManager()
        result = agent.execute("分析需求")
        assert result["success"] is True
        assert "需求分析报告" in result["output"]

    def test_generate_prd(self):
        agent = ProductManager()
        result = agent.execute("生成PRD")
        assert result["success"] is True
        assert "产品需求文档" in result["output"]


class TestRequirementEngineer:
    def test_requirement_engineer_initialization(self):
        agent = RequirementEngineer()
        assert agent.get_name() == "requirement_engineer"

    def test_refine_requirement(self):
        agent = RequirementEngineer()
        result = agent.execute("完善需求")
        assert result["success"] is True
        assert "需求完善报告" in result["output"]


class TestRequirementReviewer:
    def test_requirement_reviewer_initialization(self):
        agent = RequirementReviewer()
        assert agent.get_name() == "requirement_reviewer"

    def test_review_requirements(self):
        agent = RequirementReviewer()
        result = agent.execute("评审需求")
        assert result["success"] is True
        assert "需求评审报告" in result["output"]


class TestDesigner:
    def test_designer_initialization(self):
        agent = Designer()
        assert agent.get_name() == "designer"

    def test_design_ui(self):
        agent = Designer()
        result = agent.execute("UI设计")
        assert result["success"] is True
        assert "UI设计方案" in result["output"]


class TestDeveloper:
    def test_developer_initialization(self):
        agent = Developer()
        assert agent.get_name() == "developer"

    def test_write_code(self):
        agent = Developer()
        result = agent.execute("编写代码")
        assert result["success"] is True
        assert "代码实现方案" in result["output"]


class TestCodeReviewer:
    def test_code_reviewer_initialization(self):
        agent = CodeReviewer()
        assert agent.get_name() == "code_reviewer"

    def test_review_code(self):
        agent = CodeReviewer()
        result = agent.execute("代码审查")
        assert result["success"] is True
        assert "代码审查报告" in result["output"]


class TestTester:
    def test_tester_initialization(self):
        agent = Tester()
        assert agent.get_name() == "tester"

    def test_execute_tests(self):
        agent = Tester()
        result = agent.execute("执行测试")
        assert result["success"] is True
        assert "测试执行报告" in result["output"]


class TestProjectManager:
    def test_project_manager_initialization(self):
        agent = ProjectManager()
        assert agent.get_name() == "project_manager"

    def test_monitor_project(self):
        agent = ProjectManager()
        result = agent.execute("项目监控")
        assert result["success"] is True
        assert "项目监控报告" in result["output"]

    def test_check_direction(self):
        agent = ProjectManager()
        result = agent.execute("检查方向")
        assert result["success"] is True
        assert "项目方向检查报告" in result["output"]


class TestKnowledgeEngineer:
    def test_knowledge_engineer_initialization(self):
        agent = KnowledgeEngineer()
        assert agent.get_name() == "knowledge_engineer"

    def test_generate_skill(self):
        agent = KnowledgeEngineer()
        result = agent.execute("生成Skill")
        assert result["success"] is True
        assert "Skill生成结果" in result["output"]

    def test_generate_document(self):
        agent = KnowledgeEngineer()
        result = agent.execute("生成文档")
        assert result["success"] is True
        assert "文档生成结果" in result["output"]
