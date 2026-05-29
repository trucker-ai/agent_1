from typing import Optional, Dict, Any
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
import requests

class MCPAPIClientInput(BaseModel):
    tool_name: str = Field(description="MCP工具名称")
    params: Optional[Dict[str, Any]] = Field(default={}, description="工具参数")
    endpoint: Optional[str] = Field(default="http://localhost:8080", description="MCP服务端点")

class MCPAPIClient(BaseTool):
    name: str = "mcp_client"
    description: str = "MCP客户端工具，用于调用外部MCP服务"
    args_schema: type = MCPAPIClientInput
    
    def _run(self, tool_name: str, params: Optional[Dict[str, Any]] = None, endpoint: str = "http://localhost:8080") -> str:
        try:
            response = requests.post(
                f"{endpoint}/api/tools/{tool_name}",
                json=params or {},
                timeout=30
            )
            
            if response.status_code == 200:
                return str(response.json())
            else:
                return f"MCP调用失败 (状态码: {response.status_code}): {response.text}"
        
        except requests.exceptions.RequestException as e:
            return f"MCP调用异常: {str(e)}"
    
    async def _arun(self, tool_name: str, params: Optional[Dict[str, Any]] = None, endpoint: str = "http://localhost:8080") -> str:
        return self._run(tool_name, params, endpoint)
