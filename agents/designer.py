from typing import Dict, Any, Optional
from .base_agent import BaseAgent


class Designer(BaseAgent):
    def __init__(self):
        super().__init__("designer")

    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        result = {
            "success": True,
            "output": "",
            "type": "design"
        }

        if "UI设计" in task or "界面设计" in task:
            result["output"] = self._design_ui(task, context)
        elif "交互设计" in task:
            result["output"] = self._design_interaction(task, context)
        elif "原型设计" in task:
            result["output"] = self._design_prototype(task, context)
        else:
            result["output"] = f"设计师正在处理任务: {task}\n\n设计结果:\n- 任务类型: 产品设计\n- 状态: 进行中\n- 预计产出: 设计方案或原型"

        self.log_task(task, result["output"])
        return result

    def _design_ui(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""UI设计方案

设计任务: {task}

设计方案:

一、设计风格
- 风格定位: 现代简约风格
- 配色方案: 主色调 #1a73e8，辅助色 #4285f4
- 字体: 思源黑体，Roboto

二、界面布局
- 布局方式: 响应式网格布局
- 间距系统: 8px基础单位
- 组件间距: 16px-24px

三、组件设计
| 组件 | 设计说明 | 状态 |
|------|----------|------|
| 按钮 | 圆角8px，hover效果 | 设计中 |
| 卡片 | 阴影层级，圆角12px | 设计中 |
| 表单 | 标签对齐，错误提示 | 设计中 |

四、设计规范
- 图标: Material Icons
- 动效: 平滑过渡，200ms
- 无障碍: WCAG AA标准"""

    def _design_interaction(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""交互设计方案

交互任务: {task}

交互设计:

一、用户流程
1. 进入页面 → 加载动画 → 展示内容
2. 点击按钮 → 反馈动画 → 执行操作
3. 表单提交 → 验证 → 成功/失败反馈

二、微交互设计
- 悬停效果: 元素放大/变色
- 加载状态: 骨架屏/加载动画
- 错误状态: 红色提示+抖动效果

三、过渡动画
- 页面切换: 淡入淡出
- 弹窗出现: 缩放+淡入
- 列表滚动: 平滑滚动

四、交互原则
- 一致性: 相同操作保持一致反馈
- 反馈及时: 操作后立即响应
- 可撤销: 重要操作支持撤销"""

    def _design_prototype(self, task: str, context: Optional[Dict[str, Any]] = None) -> str:
        return f"""原型设计说明

原型任务: {task}

原型信息:

一、页面结构
- 首页: 功能入口+内容展示
- 列表页: 数据列表+筛选
- 详情页: 详细信息+操作按钮
- 设置页: 配置选项

二、交互说明
- 点击导航 → 切换页面
- 下拉刷新 → 更新数据
- 滑动删除 → 删除条目

三、原型工具
- 设计工具: Figma/Sketch
- 原型工具: Figma/Adobe XD
- 协作方式: 在线协作

四、交付物
- 设计稿: 完整页面设计
- 交互原型: 可点击演示
- 设计规范: 标注+切图"""
