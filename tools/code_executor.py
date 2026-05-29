from typing import Optional
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
import subprocess
import tempfile
import os

class CodeExecutorInput(BaseModel):
    code: str = Field(description="要执行的Python代码")
    timeout: Optional[int] = Field(default=30, description="执行超时时间（秒）")

class CodeExecutor(BaseTool):
    name: str = "code_executor"
    description: str = "代码执行工具，用于安全执行Python代码"
    args_schema: type = CodeExecutorInput
    
    def _run(self, code: str, timeout: int = 30) -> str:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=os.path.dirname(temp_file)
            )
            
            if result.returncode == 0:
                return f"执行成功:\n{result.stdout}"
            else:
                return f"执行失败 (退出码: {result.returncode}):\n错误: {result.stderr}"
        
        except subprocess.TimeoutExpired:
            return f"执行超时 ({timeout}秒)"
        except Exception as e:
            return f"执行异常: {str(e)}"
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    async def _arun(self, code: str, timeout: int = 30) -> str:
        return self._run(code, timeout)
