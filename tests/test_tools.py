import pytest
import tempfile
import os
from tools import FileSystemTool, CodeExecutor, SkillManager


class TestFileSystemTool:
    def test_file_system_tool_initialization(self):
        tool = FileSystemTool()
        assert tool is not None

    def test_read_write_file(self):
        tool = FileSystemTool()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            temp_file = f.name
            f.write("test content")
        
        content = tool.read_file(temp_file)
        assert content == "test content"
        
        tool.write_file(temp_file, "new content")
        content = tool.read_file(temp_file)
        assert content == "new content"
        
        os.unlink(temp_file)

    def test_file_exists(self):
        tool = FileSystemTool()
        assert tool.file_exists(__file__) is True
        assert tool.file_exists("/nonexistent/file.txt") is False

    def test_list_directory(self):
        tool = FileSystemTool()
        files = tool.list_directory(".")
        assert isinstance(files, list)


class TestCodeExecutor:
    def test_code_executor_initialization(self):
        executor = CodeExecutor()
        assert executor is not None

    def test_execute_python(self):
        executor = CodeExecutor()
        result = executor.execute_python("print('hello')")
        assert result["success"] is True
        assert "hello" in result["output"]

    def test_execute_safe_python(self):
        executor = CodeExecutor()
        result = executor.execute_safe_python("print('safe')")
        assert result["success"] is True
        assert "safe" in result["output"]

    def test_dangerous_code_blocked(self):
        executor = CodeExecutor()
        result = executor.execute_safe_python("import os; os.system('rm -rf /')")
        assert result["success"] is False
        assert "dangerous" in result["error"]

    def test_cleanup(self):
        executor = CodeExecutor()
        sandbox_dir = executor.sandbox_dir
        assert os.path.exists(sandbox_dir)
        executor.cleanup()
        assert not os.path.exists(sandbox_dir)


class TestSkillManager:
    def test_skill_manager_initialization(self):
        manager = SkillManager()
        assert manager is not None

    def test_register_skill(self):
        manager = SkillManager()
        
        def test_skill(name: str) -> str:
            return f"Hello {name}"
        
        manager.register_skill("test_skill", "A test skill", test_skill)
        assert "test_skill" in manager.skills

    def test_execute_skill(self):
        manager = SkillManager()
        
        def test_skill(input_name: str) -> str:
            return f"Hello {input_name}"
        
        manager.register_skill("test_skill", "A test skill", test_skill)
        result = manager.execute_skill("test_skill", input_name="World")
        assert result["success"] is True
        assert result["result"] == "Hello World"

    def test_list_skills(self):
        manager = SkillManager()
        
        def test_skill(name: str) -> str:
            return f"Hello {name}"
        
        manager.register_skill("test_skill", "A test skill", test_skill)
        skills = manager.list_skills()
        assert isinstance(skills, list)
        assert len(skills) == 1
