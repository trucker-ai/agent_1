from datetime import datetime
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class CostEntry:
    id: str
    service: str
    operation: str
    cost: float
    usage: float
    unit: str
    timestamp: datetime
    metadata: Dict[str, Any]


class CostTracker:
    def __init__(self, budget_limit: float = 100.0):
        self.entries: List[CostEntry] = []
        self.budget_limit = budget_limit
        self.total_cost = 0.0
        self.api_calls = {}

    def record_cost(self, service: str, operation: str, cost: float, usage: float, unit: str = "tokens", metadata: Optional[Dict[str, Any]] = None):
        if metadata is None:
            metadata = {}

        entry = CostEntry(
            id=f"{service}-{operation}-{len(self.entries)}",
            service=service,
            operation=operation,
            cost=cost,
            usage=usage,
            unit=unit,
            timestamp=datetime.now(),
            metadata=metadata
        )

        self.entries.append(entry)
        self.total_cost += cost

        if service not in self.api_calls:
            self.api_calls[service] = 0
        self.api_calls[service] += 1

    def get_total_cost(self) -> float:
        return self.total_cost

    def get_cost_by_service(self, service: str) -> float:
        return sum(entry.cost for entry in self.entries if entry.service == service)

    def get_api_call_count(self, service: str = None) -> int:
        if service is None:
            return sum(self.api_calls.values())
        return self.api_calls.get(service, 0)

    def get_cost_by_period(self, start_time: datetime, end_time: datetime) -> float:
        return sum(
            entry.cost for entry in self.entries
            if start_time <= entry.timestamp <= end_time
        )

    def get_recent_entries(self, limit: int = 10) -> List[CostEntry]:
        return sorted(self.entries, key=lambda x: x.timestamp, reverse=True)[:limit]

    def get_budget_remaining(self) -> float:
        return max(0.0, self.budget_limit - self.total_cost)

    def get_budget_usage_percentage(self) -> float:
        return (self.total_cost / self.budget_limit) * 100

    def is_over_budget(self) -> bool:
        return self.total_cost >= self.budget_limit

    def get_cost_summary(self) -> Dict[str, Any]:
        return {
            "total_cost": self.total_cost,
            "budget_limit": self.budget_limit,
            "budget_remaining": self.get_budget_remaining(),
            "budget_usage_percentage": self.get_budget_usage_percentage(),
            "api_calls": self.api_calls,
            "total_api_calls": self.get_api_call_count(),
            "is_over_budget": self.is_over_budget()
        }

    def reset(self):
        self.entries = []
        self.total_cost = 0.0
        self.api_calls = {}

    def export_to_csv(self) -> str:
        lines = ["id,service,operation,cost,usage,unit,timestamp"]
        for entry in self.entries:
            lines.append(
                f"{entry.id},{entry.service},{entry.operation},{entry.cost},{entry.usage},{entry.unit},{entry.timestamp.isoformat()}"
            )
        return "\n".join(lines)
