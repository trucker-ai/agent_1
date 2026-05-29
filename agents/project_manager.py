from typing import Dict, Any, Optional
from .base_agent import BaseAgent


class ProjectManager(BaseAgent):
    def __init__(self):
        super().__init__("project_manager")

    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        result = {
            "success": True,
            "output": "",
            "type": "management"
        }

        if "项目监控" in task or "进度监控" in task:
            result["output"] = self._monitor_project(task, context)
        elif "项目规划" in task:
            result["output"] = self._plan_project(task, context)
        elif "风险评估" in task:
            result["output"] = self._assess_risks(task, context)
        elif "检查方向" in task or "偏离方向" in task:
            result["output"] = self._check_direction(task, context)
        else:
            result["output"] = f"项目经理正在处理任务: {task}\n\n处理结果:\n- 任务类型: 项目管理\n- 状态: 进行中\n- 预计产出: 管理报告"

        self.log_task(task, result["output"])
        return result

    def _monitor_project(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""项目监控报告

监控任务: {task}

项目状态:

一、进度概览
- 项目阶段: 开发阶段
- 整体进度: 65%
- 计划进度: 70%
- 进度偏差: -5%

二、任务状态
| 任务 | 状态 | 负责人 | 进度 |
|------|------|--------|------|
| 需求分析 | 已完成 | 产品组 | 100% |
| 设计阶段 | 已完成 | 设计组 | 100% |
| 开发阶段 | 进行中 | 开发组 | 60% |
| 测试阶段 | 待开始 | 测试组 | 0% |

三、资源使用
- 人力投入: 8人
- 预算使用: 60%
- 时间消耗: 55%

四、问题与风险
1. 开发进度落后
2. 测试资源紧张
3. 技术难点待攻克

五、建议措施
- 增加开发资源
- 优化任务分配
- 加强沟通协调"""

    def _plan_project(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""项目规划

规划任务: {task}

规划内容:

一、项目目标
- 目标1: 按时交付
- 目标2: 质量达标
- 目标3: 控制成本

二、阶段规划
| 阶段 | 时间 | 负责人 | 交付物 |
|------|------|--------|--------|
| 需求分析 | 第1-2周 | 产品组 | PRD文档 |
| 设计阶段 | 第3-4周 | 设计组 | 设计稿 |
| 开发阶段 | 第5-10周 | 开发组 | 代码实现 |
| 测试阶段 | 第11-12周 | 测试组 | 测试报告 |
| 上线部署 | 第13周 | 运维组 | 上线完成 |

三、资源规划
- 人力: 10人
- 预算: 100万
- 时间: 13周

四、里程碑
- M1: 需求完成 (第2周)
- M2: 设计完成 (第4周)
- M3: 开发完成 (第10周)
- M4: 测试完成 (第12周)
- M5: 上线完成 (第13周)"""

    def _assess_risks(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""风险评估报告

评估任务: {task}

风险分析:

一、风险识别
| 风险 | 概率 | 影响 | 优先级 |
|------|------|------|--------|
| 技术风险 | 中 | 高 | P0 |
| 进度风险 | 高 | 中 | P0 |
| 资源风险 | 低 | 中 | P1 |
| 需求变更 | 中 | 中 | P1 |

二、风险详情
1. 技术风险: 新技术栈可能存在未知问题
2. 进度风险: 开发任务可能延期
3. 资源风险: 人员变动可能性
4. 需求变更: 需求可能发生变更

三、应对策略
| 风险 | 策略 | 负责人 |
|------|------|--------|
| 技术风险 | 技术预研 | 技术负责人 |
| 进度风险 | 预留缓冲时间 | PM |
| 资源风险 | 备份人员计划 | HR |
| 需求变更 | 需求冻结机制 | 产品负责人 |

四、风险状态
整体风险等级: 中等"""

    def _check_direction(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""项目方向检查报告

检查任务: {task}

方向评估:

一、目标对齐检查
- [ ] 项目目标与公司战略一致
- [ ] 当前进展符合预期目标
- [ ] 交付物满足需求要求
- [ ] 质量标准符合预期

二、方向偏离分析
| 维度 | 评估 | 偏差 | 原因 |
|------|------|------|------|
| 进度 | 落后 | -5% | 技术难点 |
| 质量 | 符合 | 0% | 正常 |
| 成本 | 符合 | 0% | 正常 |
| 范围 | 符合 | 0% | 正常 |

三、偏离原因分析
1. 技术难点导致进度延迟
2. 资源不足影响效率
3. 外部依赖未按时交付

四、纠正建议
1. 增加技术资源投入
2. 优化任务优先级
3. 加强外部依赖跟进

五、结论
项目方向: 基本符合预期，但需关注进度偏差"""
