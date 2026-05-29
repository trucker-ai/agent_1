import json
import requests
from typing import Optional, Dict, Any, List


class MCPError(Exception):
    pass


class MCPToolDescriptor:
    def __init__(self, name: str, description: str, parameters: Dict[str, Any]):
        self.name = name
        self.description = description
        self.parameters = parameters

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters
        }


class MCPResponse:
    def __init__(self, success: bool, result: Any = None, error: str = ""):
        self.success = success
        self.result = result
        self.error = error

    def to_dict(self):
        return {
            "success": self.success,
            "result": self.result,
            "error": self.error
        }


class MCPAPIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()

    def list_tools(self) -> List[MCPToolDescriptor]:
        try:
            response = self.session.get(f"{self.base_url}/tools")
            response.raise_for_status()
            data = response.json()
            return [MCPToolDescriptor(**tool) for tool in data.get("tools", [])]
        except Exception as e:
            return []

    def get_tool(self, tool_name: str) -> Optional[MCPToolDescriptor]:
        try:
            response = self.session.get(f"{self.base_url}/tools/{tool_name}")
            response.raise_for_status()
            data = response.json()
            return MCPToolDescriptor(**data)
        except Exception as e:
            return None

    def call_tool(self, tool_name: str, **kwargs) -> MCPResponse:
        try:
            response = self.session.post(
                f"{self.base_url}/tools/{tool_name}/call",
                json=kwargs
            )
            response.raise_for_status()
            data = response.json()
            return MCPResponse(
                success=data.get("success", False),
                result=data.get("result"),
                error=data.get("error", "")
            )
        except requests.exceptions.RequestException as e:
            return MCPResponse(
                success=False,
                error=f"Request failed: {str(e)}"
            )
        except Exception as e:
            return MCPResponse(
                success=False,
                error=f"Error calling tool: {str(e)}"
            )

    def health_check(self) -> bool:
        try:
            response = self.session.get(f"{self.base_url}/health")
            return response.status_code == 200
        except Exception:
            return False


class LocalMCPAdapter:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name: str, description: str, func):
        self.tools[name] = {
            "description": description,
            "function": func
        }

    def list_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": name,
                "description": tool["description"],
                "parameters": {}
            }
            for name, tool in self.tools.items()
        ]

    def call_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        if tool_name not in self.tools:
            return {
                "success": False,
                "result": None,
                "error": f"Tool not found: {tool_name}"
            }

        try:
            result = self.tools[tool_name]["function"](**kwargs)
            return {
                "success": True,
                "result": result,
                "error": ""
            }
        except Exception as e:
            return {
                "success": False,
                "result": None,
                "error": str(e)
            }
