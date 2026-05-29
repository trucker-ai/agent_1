import pytest
from cost_control import CostTracker, CostEntry


class TestCostEntry:
    def test_cost_entry_initialization(self):
        entry = CostEntry("test_id", "openai", "completion", 0.01, 1000, "tokens", "2024-01-01T00:00:00", metadata={"model": "gpt-4"})
        assert entry.id == "test_id"
        assert entry.service == "openai"
        assert entry.cost == 0.01
        assert entry.usage == 1000


class TestCostTracker:
    def test_cost_tracker_initialization(self):
        tracker = CostTracker()
        assert tracker is not None
        assert tracker.total_cost == 0.0

    def test_record_cost(self):
        tracker = CostTracker()
        tracker.record_cost("openai", "completion", 0.01, 1000)
        assert tracker.total_cost == 0.01
        assert tracker.get_api_call_count("openai") == 1

    def test_get_total_cost(self):
        tracker = CostTracker()
        tracker.record_cost("openai", "completion", 0.01, 1000)
        tracker.record_cost("openai", "embedding", 0.005, 500)
        assert tracker.get_total_cost() == 0.015

    def test_get_cost_by_service(self):
        tracker = CostTracker()
        tracker.record_cost("openai", "completion", 0.01, 1000)
        tracker.record_cost("anthropic", "completion", 0.02, 2000)
        assert tracker.get_cost_by_service("openai") == 0.01
        assert tracker.get_cost_by_service("anthropic") == 0.02

    def test_get_api_call_count(self):
        tracker = CostTracker()
        tracker.record_cost("openai", "completion", 0.01, 1000)
        tracker.record_cost("openai", "embedding", 0.005, 500)
        tracker.record_cost("anthropic", "completion", 0.02, 2000)
        
        assert tracker.get_api_call_count("openai") == 2
        assert tracker.get_api_call_count("anthropic") == 1
        assert tracker.get_api_call_count() == 3

    def test_get_budget_remaining(self):
        tracker = CostTracker(budget_limit=10.0)
        tracker.record_cost("openai", "completion", 3.0, 30000)
        assert tracker.get_budget_remaining() == 7.0

    def test_get_budget_usage_percentage(self):
        tracker = CostTracker(budget_limit=10.0)
        tracker.record_cost("openai", "completion", 3.0, 30000)
        assert tracker.get_budget_usage_percentage() == 30.0

    def test_is_over_budget(self):
        tracker = CostTracker(budget_limit=10.0)
        assert tracker.is_over_budget() is False
        
        tracker.record_cost("openai", "completion", 15.0, 150000)
        assert tracker.is_over_budget() is True

    def test_get_cost_summary(self):
        tracker = CostTracker(budget_limit=10.0)
        tracker.record_cost("openai", "completion", 3.0, 30000)
        
        summary = tracker.get_cost_summary()
        assert summary["total_cost"] == 3.0
        assert summary["budget_limit"] == 10.0
        assert summary["budget_remaining"] == 7.0
        assert summary["is_over_budget"] is False

    def test_reset(self):
        tracker = CostTracker()
        tracker.record_cost("openai", "completion", 0.01, 1000)
        tracker.reset()
        assert tracker.total_cost == 0.0
        assert tracker.get_api_call_count() == 0
