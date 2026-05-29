import pytest
from memory import ProjectMemory, MemoryEntry


class TestMemoryEntry:
    def test_memory_entry_initialization(self):
        entry = MemoryEntry("test_id", "test content", {"key": "value"})
        assert entry.id == "test_id"
        assert entry.content == "test content"
        assert entry.metadata == {"key": "value"}

    def test_memory_entry_to_dict(self):
        entry = MemoryEntry("test_id", "test content", {"key": "value"})
        data = entry.to_dict()
        assert data["id"] == "test_id"
        assert data["content"] == "test content"
        assert data["metadata"] == {"key": "value"}


class TestProjectMemory:
    def test_project_memory_initialization(self):
        memory = ProjectMemory()
        assert memory is not None

    def test_add_memory(self):
        memory = ProjectMemory()
        memory_id = memory.add_memory("test content", {"category": "test"})
        assert memory_id is not None
        assert memory.get_memory(memory_id) is not None

    def test_get_memory(self):
        memory = ProjectMemory()
        memory_id = memory.add_memory("test content")
        entry = memory.get_memory(memory_id)
        assert entry.content == "test content"

    def test_search_by_metadata(self):
        memory = ProjectMemory()
        memory.add_memory("content 1", {"category": "cat1"})
        memory.add_memory("content 2", {"category": "cat2"})
        memory.add_memory("content 3", {"category": "cat1"})
        
        results = memory.search_by_metadata(category="cat1")
        assert len(results) == 2

    def test_search_by_content(self):
        memory = ProjectMemory()
        memory.add_memory("hello world")
        memory.add_memory("goodbye world")
        memory.add_memory("test content")
        
        results = memory.search_by_content("world")
        assert len(results) == 2

    def test_update_memory(self):
        memory = ProjectMemory()
        memory_id = memory.add_memory("original")
        success = memory.update_memory(memory_id, content="updated", metadata={"key": "value"})
        assert success is True
        
        entry = memory.get_memory(memory_id)
        assert entry.content == "updated"
        assert entry.metadata["key"] == "value"

    def test_delete_memory(self):
        memory = ProjectMemory()
        memory_id = memory.add_memory("to be deleted")
        success = memory.delete_memory(memory_id)
        assert success is True
        assert memory.get_memory(memory_id) is None

    def test_list_memories(self):
        memory = ProjectMemory()
        memory.add_memory("content 1")
        memory.add_memory("content 2")
        
        entries = memory.list_memories()
        assert len(entries) == 2

    def test_get_memory_count(self):
        memory = ProjectMemory()
        memory.add_memory("content 1")
        memory.add_memory("content 2")
        
        count = memory.get_memory_count()
        assert count == 2

    def test_clear_all(self):
        memory = ProjectMemory()
        memory.add_memory("content 1")
        memory.add_memory("content 2")
        
        memory.clear_all()
        assert memory.get_memory_count() == 0

    def test_export_import_json(self):
        memory = ProjectMemory()
        memory.add_memory("content 1", {"key": "value"})
        
        json_str = memory.export_to_json()
        assert "content 1" in json_str
        
        new_memory = ProjectMemory()
        success = new_memory.import_from_json(json_str)
        assert success is True
        assert new_memory.get_memory_count() == 1
