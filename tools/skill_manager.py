from typing import Optional, Dict, Any, List
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

class SkillManagerInput(BaseModel):
    action: str = Field(description="操作类型: register, list, execute")
    skill_name: Optional[str] = Field(description="技能名称")
    skill_info: Optional[Dict[str, Any]] = Field(description="技能信息")
    params: Optional[Dict[str, Any]] = Field(default={}, description="执行参数")

class SkillManager(BaseTool):
    name: str = "skill_manager"
    description: str = "技能管理器，用于注册、查询和执行技能"
    args_schema: type = SkillManagerInput
    
    def __init__(self):
        super().__init__()
        object.__setattr__(self, '_skills', {})
    
    @property
    def skills(self) -> Dict[str, Dict[str, Any]]:
        return object.__getattribute__(self, '_skills')
    
    def _run(self, action: str, skill_name: Optional[str] = None, 
             skill_info: Optional[Dict[str, Any]] = None, 
             params: Optional[Dict[str, Any]] = None) -> str:
        try:
            if action == "register":
                if not skill_name or not skill_info:
                    return "注册技能需要提供技能名称和技能信息"
                self.skills[skill_name] = skill_info
                return f"技能 '{skill_name}' 注册成功"
            
            elif action == "list":
                if not self.skills:
                    return "暂无已注册的技能"
                return "\n".join([f"- {name}: {info.get('description', '无描述')}" 
                                for name, info in self.skills.items()])
            
            elif action == "execute":
                if not skill_name:
                    return "执行技能需要提供技能名称"
                if skill_name not in self.skills:
                    return f"技能 '{skill_name}' 未注册"
                skill = self.skills[skill_name]
                return f"执行技能 '{skill_name}': {skill.get('description', '')}\n参数: {params}"
            
            elif action == "delete":
                if not skill_name:
                    return "删除技能需要提供技能名称"
                if skill_name in self.skills:
                    del self.skills[skill_name]
                    return f"技能 '{skill_name}' 删除成功"
                return f"技能 '{skill_name}' 未找到"
            
            else:
                return f"未知操作: {action}"
        
        except Exception as e:
            return f"操作失败: {str(e)}"
    
    async def _arun(self, action: str, skill_name: Optional[str] = None,
                    skill_info: Optional[Dict[str, Any]] = None,
                    params: Optional[Dict[str, Any]] = None) -> str:
        return self._run(action, skill_name, skill_info, params)
    
    def get_skills(self) -> List[str]:
        return list(self.skills.keys())
