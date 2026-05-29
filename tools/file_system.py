from typing import Optional
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
import os

class FileSystemToolInput(BaseModel):
    action: str = Field(description="操作类型: read, write, list, delete")
    file_path: str = Field(description="文件路径")
    content: Optional[str] = Field(description="文件内容，仅写入时需要")

class FileSystemTool(BaseTool):
    name: str = "file_system"
    description: str = "文件系统工具，支持文件的读取、写入、列出和删除操作"
    args_schema: type = FileSystemToolInput
    
    def _run(self, action: str, file_path: str, content: Optional[str] = None) -> str:
        try:
            if action == "read":
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        return f.read()
                return f"文件不存在: {file_path}"
            
            elif action == "write":
                directory = os.path.dirname(file_path)
                if directory and not os.path.exists(directory):
                    os.makedirs(directory)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content or "")
                return f"文件写入成功: {file_path}"
            
            elif action == "list":
                if os.path.exists(file_path) and os.path.isdir(file_path):
                    return "\n".join(os.listdir(file_path))
                return f"目录不存在: {file_path}"
            
            elif action == "delete":
                if os.path.exists(file_path):
                    os.remove(file_path)
                    return f"文件删除成功: {file_path}"
                return f"文件不存在: {file_path}"
            
            else:
                return f"未知操作: {action}"
        
        except Exception as e:
            return f"操作失败: {str(e)}"
    
    async def _arun(self, action: str, file_path: str, content: Optional[str] = None) -> str:
        return self._run(action, file_path, content)
