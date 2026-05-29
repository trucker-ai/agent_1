import os
import importlib
import inspect
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass


@dataclass
class SkillInfo:
    name: str
    description: str
    module_path: str
    function_name: str
    parameters: Dict[str, Any]
    is_available: bool = True


class SkillManager:
    def __init__(self):
        self.skills: Dict[str, SkillInfo] = {}
        self.skill_instances: Dict[str, Any] = {}

    def discover_skills(self, directory: str = "skills") -> List[str]:
        discovered = []

        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            return discovered

        for filename in os.listdir(directory):
            if filename.endswith(".py") and not filename.startswith("_"):
                module_name = filename[:-3]
                module_path = os.path.join(directory, filename)

                try:
                    spec = importlib.util.spec_from_file_location(
                        module_name, module_path)
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)

                        for name, obj in inspect.getmembers(module):
                            if inspect.isfunction(obj) or inspect.isclass(obj):
                                description = getattr(
                                    obj, '__doc__', '') or f"{name} skill"
                                params = {}

                                if inspect.isfunction(obj):
                                    sig = inspect.signature(obj)
                                    params = {
                                        param: str(
                                            sig.parameters[param].annotation)
                                        for param in sig.parameters
                                    }

                                skill_info = SkillInfo(
                                    name=name,
                                    description=description,
                                    module_path=module_path,
                                    function_name=name,
                                    parameters=params
                                )
                                self.skills[name] = skill_info
                                discovered.append(name)
                except Exception as e:
                    continue

        return discovered

    def register_skill(self, name: str, description: str, func: Callable):
        sig = inspect.signature(func)
        params = {
            param: str(sig.parameters[param].annotation)
            for param in sig.parameters
        }

        skill_info = SkillInfo(
            name=name,
            description=description,
            module_path="",
            function_name=name,
            parameters=params
        )
        self.skills[name] = skill_info
        self.skill_instances[name] = func

    def get_skill(self, name: str) -> Optional[SkillInfo]:
        return self.skills.get(name)

    def list_skills(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": skill.name,
                "description": skill.description,
                "parameters": skill.parameters,
                "is_available": skill.is_available
            }
            for skill in self.skills.values()
        ]

    def execute_skill(self, name: str, **kwargs) -> Dict[str, Any]:
        if name not in self.skills:
            return {
                "success": False,
                "result": None,
                "error": f"Skill not found: {name}"
            }

        try:
            if name in self.skill_instances:
                func = self.skill_instances[name]
            else:
                skill_info = self.skills[name]
                spec = importlib.util.spec_from_file_location(
                    skill_info.name,
                    skill_info.module_path
                )
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    func = getattr(module, skill_info.function_name)
                    self.skill_instances[name] = func
                else:
                    return {
                        "success": False,
                        "result": None,
                        "error": "Failed to load skill module"
                    }

            result = func(**kwargs)
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

    def unregister_skill(self, name: str) -> bool:
        if name in self.skills:
            del self.skills[name]
            if name in self.skill_instances:
                del self.skill_instances[name]
            return True
        return False

    def get_skill_requirements(self, name: str) -> Optional[List[str]]:
        skill = self.skills.get(name)
        if not skill:
            return None

        try:
            spec = importlib.util.spec_from_file_location(
                skill.name,
                skill.module_path
            )
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                obj = getattr(module, skill.function_name)
                return getattr(obj, 'requirements', [])
        except Exception:
            pass

        return []
