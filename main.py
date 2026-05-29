#!/usr/bin/env python3

import argparse
import json
from workflow import ProjectTeam, LangGraphWorkflow


def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║                    AI多Agent工作流系统                             ║
║                AI Multi-Agent Workflow System                    ║
║                   Powered by LangGraph                           ║
╚══════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_status(status):
    print("\n" + "="*50)
    print("系统状态")
    print("="*50)
    
    if "orchestrator" in status:
        print("\n📊 Agent状态:")
        for agent, info in status["orchestrator"]["agents"].items():
            print(f"  - {agent}: 可用, 工具数: {info['tools_count']}")
    else:
        print("\n📊 Agent状态:")
        for agent in status["agents"]:
            print(f"  - {agent}: 可用")
    
    print(f"\n📝 内存条目: {status['memory_entries']}")
    
    if "tasks" in status:
        print("\n📋 任务状态:")
        print(f"  总任务数: {status['tasks']['total']}")
        for status_name, count in status['tasks']['status'].items():
            print(f"  - {status_name}: {count}")
    
    print("\n💰 成本统计:")
    print(f"  总费用: {status['cost'].get('total_cost', 0):.4f}")
    print(f"  预算限制: {status['cost'].get('budget_limit', 0):.2f}")
    print(f"  预算剩余: {status['cost'].get('budget_remaining', 0):.2f}")
    print(f"  API调用: {status['cost'].get('total_api_calls', 0)}")
    
    print("\n" + "="*50)


def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="AI多Agent工作流系统")
    parser.add_argument("--project", type=str, help="项目名称")
    parser.add_argument("--workflow", type=str, help="工作流名称")
    parser.add_argument("--agent", type=str, help="Agent名称")
    parser.add_argument("--task", type=str, help="任务描述")
    parser.add_argument("--status", action="store_true", help="显示系统状态")
    parser.add_argument("--list-agents", action="store_true", help="列出所有Agent")
    parser.add_argument("--list-workflows", action="store_true", help="列出所有工作流")
    parser.add_argument("--langgraph", action="store_true", help="使用LangGraph工作流")
    
    args = parser.parse_args()
    
    if args.langgraph:
        workflow = LangGraphWorkflow()
        is_langgraph = True
    else:
        workflow = ProjectTeam()
        is_langgraph = False
    
    if args.project:
        if is_langgraph:
            print(f"🚀 初始化LangGraph工作流项目: {args.project}")
            result = workflow.execute_workflow(args.project, args.project)
            if result["success"]:
                print(f"✅ 项目 '{args.project}' 工作流执行成功")
            else:
                print(f"❌ 工作流执行失败: {result.get('error', '未知错误')}")
        else:
            result = workflow.start_project(args.project)
            print(f"✅ {result['message']}")
            print(f"🤖 可用Agent: {', '.join(result['agents'])}")
    
    if args.workflow:
        print(f"\n🚀 执行工作流: {args.workflow}")
        if is_langgraph:
            result = workflow.execute_workflow(args.workflow, args.workflow)
        else:
            result = workflow.execute_workflow(args.workflow)
        
        if result["success"]:
            print("✅ 工作流执行成功")
            for i, r in enumerate(result["results"], 1):
                print(f"\n--- 步骤 {i}: {r['agent']} ---")
                output = r["result"]["output"] if isinstance(r["result"], dict) else str(r["result"])
                print(output[:200] + "..." if len(output) > 200 else output)
        else:
            print(f"❌ 工作流执行失败: {result.get('error', '未知错误')}")
    
    if args.agent and args.task:
        print(f"\n📋 分配任务: {args.agent} -> {args.task}")
        if is_langgraph:
            result = workflow.execute_single_task(args.agent, args.task)
        else:
            result = workflow.assign_task(args.agent, args.task)
        
        if result["success"]:
            print("✅ 任务执行成功")
            print("\n📄 输出:")
            output = result["output"] if isinstance(result, dict) else str(result)
            print(output)
        else:
            print(f"❌ 任务执行失败: {result.get('error', '未知错误')}")
    
    if args.status:
        status = workflow.get_status()
        print_status(status)
    
    if args.list_agents:
        print("\n🤖 可用Agent列表:")
        for agent in workflow.list_agents():
            print(f"  - {agent}")
    
    if args.list_workflows:
        print("\n🔄 可用工作流列表:")
        if is_langgraph:
            print("  - LangGraph完整流程 (产品经理→需求工程师→需求评审→设计师→开发者→代码审查→测试→项目经理→知识工程)")
        else:
            for wf in workflow.list_available_workflows():
                print(f"  - {wf}")
    
    if not any([args.project, args.workflow, args.agent, args.status, args.list_agents, args.list_workflows]):
        print("📖 使用说明:")
        print("  python main.py --project <项目名>    # 创建项目")
        print("  python main.py --workflow <工作流>  # 执行工作流")
        print("  python main.py --agent <Agent> --task <任务>  # 分配任务")
        print("  python main.py --status           # 显示状态")
        print("  python main.py --list-agents      # 列出Agent")
        print("  python main.py --list-workflows   # 列出工作流")
        print("  python main.py --langgraph        # 使用LangGraph工作流")
        print("")
        print("🔄 LangGraph工作流模式:")
        print("  python main.py --langgraph --project <项目名>")
        print("  python main.py --langgraph --agent <Agent> --task <任务>")


if __name__ == "__main__":
    main()
