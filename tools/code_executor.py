import subprocess
import tempfile
import os
from typing import Optional, Dict, Any


class CodeExecutor:
    def __init__(self):
        self.sandbox_dir = tempfile.mkdtemp(prefix="code_exec_")

    def execute_python(self, code: str, timeout: int = 30) -> Dict[str, Any]:
        result = {
            "success": False,
            "output": "",
            "error": "",
            "execution_time": 0
        }

        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name

            process = subprocess.run(
                ["python", temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=self.sandbox_dir
            )

            if process.returncode == 0:
                result["success"] = True
                result["output"] = process.stdout
            else:
                result["error"] = process.stderr

            os.unlink(temp_file)

        except subprocess.TimeoutExpired:
            result["error"] = f"Execution timed out after {timeout} seconds"
        except Exception as e:
            result["error"] = f"Error executing code: {str(e)}"

        return result

    def execute_shell(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        result = {
            "success": False,
            "output": "",
            "error": "",
            "execution_time": 0
        }

        try:
            process = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=self.sandbox_dir
            )

            if process.returncode == 0:
                result["success"] = True
                result["output"] = process.stdout
            else:
                result["error"] = process.stderr

        except subprocess.TimeoutExpired:
            result["error"] = f"Command timed out after {timeout} seconds"
        except Exception as e:
            result["error"] = f"Error executing command: {str(e)}"

        return result

    def is_safe_code(self, code: str) -> bool:
        dangerous_patterns = [
            "os.system",
            "subprocess",
            "__import__",
            "eval(",
            "exec(",
            "open(",
            "file(",
            "socket.",
            "import os",
            "import sys",
            "import subprocess",
            "del ",
            "rm ",
            "kill "
        ]

        for pattern in dangerous_patterns:
            if pattern in code:
                return False
        return True

    def execute_safe_python(self, code: str, timeout: int = 30) -> Dict[str, Any]:
        if not self.is_safe_code(code):
            return {
                "success": False,
                "output": "",
                "error": "Potentially dangerous code detected. Execution blocked.",
                "execution_time": 0
            }

        return self.execute_python(code, timeout)

    def cleanup(self):
        if os.path.exists(self.sandbox_dir):
            import shutil
            shutil.rmtree(self.sandbox_dir)
