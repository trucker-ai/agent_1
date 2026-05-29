import json
import hashlib
from typing import Dict, Any, List, Optional
from datetime import datetime


class MemoryEntry:
    def __init__(self, id: str, content: str, metadata: Dict[str, Any], created_at: datetime = None):
        self.id = id
        self.content = content
        self.metadata = metadata
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat()
        }


class ProjectMemory:
    def __init__(self):
        self.memories: Dict[str, MemoryEntry] = {}
        self.index: Dict[str, List[str]] = {}

    def generate_id(self, content: str) -> str:
        return hashlib.md5(content.encode()).hexdigest()[:16]

    def add_memory(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> str:
        if metadata is None:
            metadata = {}

        memory_id = self.generate_id(content)

        if memory_id in self.memories:
            return memory_id

        entry = MemoryEntry(
            id=memory_id,
            content=content,
            metadata=metadata
        )
        self.memories[memory_id] = entry

        for key, value in metadata.items():
            index_key = f"{key}:{value}"
            if index_key not in self.index:
                self.index[index_key] = []
            if memory_id not in self.index[index_key]:
                self.index[index_key].append(memory_id)

        return memory_id

    def get_memory(self, memory_id: str) -> Optional[MemoryEntry]:
        return self.memories.get(memory_id)

    def search_by_metadata(self, **kwargs) -> List[MemoryEntry]:
        results = []

        for key, value in kwargs.items():
            index_key = f"{key}:{value}"
            if index_key in self.index:
                for memory_id in self.index[index_key]:
                    entry = self.memories.get(memory_id)
                    if entry:
                        results.append(entry)

        return results

    def search_by_content(self, query: str) -> List[MemoryEntry]:
        results = []

        for entry in self.memories.values():
            if query.lower() in entry.content.lower():
                results.append(entry)

        return results

    def update_memory(self, memory_id: str, content: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> bool:
        if memory_id not in self.memories:
            return False

        entry = self.memories[memory_id]

        if content is not None:
            entry.content = content

        if metadata is not None:
            for key, value in metadata.items():
                entry.metadata[key] = value

                index_key = f"{key}:{value}"
                if index_key not in self.index:
                    self.index[index_key] = []
                if memory_id not in self.index[index_key]:
                    self.index[index_key].append(memory_id)

        return True

    def delete_memory(self, memory_id: str) -> bool:
        if memory_id not in self.memories:
            return False

        entry = self.memories.pop(memory_id)

        for key, value in entry.metadata.items():
            index_key = f"{key}:{value}"
            if index_key in self.index and memory_id in self.index[index_key]:
                self.index[index_key].remove(memory_id)

        return True

    def list_memories(self) -> List[MemoryEntry]:
        return list(self.memories.values())

    def get_memory_count(self) -> int:
        return len(self.memories)

    def clear_all(self):
        self.memories.clear()
        self.index.clear()

    def export_to_json(self) -> str:
        data = {
            "memories": [entry.to_dict() for entry in self.memories.values()],
            "exported_at": datetime.now().isoformat()
        }
        return json.dumps(data, indent=2)

    def import_from_json(self, json_str: str) -> bool:
        try:
            data = json.loads(json_str)

            for entry_data in data.get("memories", []):
                created_at = datetime.fromisoformat(entry_data["created_at"])
                entry = MemoryEntry(
                    id=entry_data["id"],
                    content=entry_data["content"],
                    metadata=entry_data.get("metadata", {}),
                    created_at=created_at
                )
                self.memories[entry.id] = entry

                for key, value in entry.metadata.items():
                    index_key = f"{key}:{value}"
                    if index_key not in self.index:
                        self.index[index_key] = []
                    if entry.id not in self.index[index_key]:
                        self.index[index_key].append(entry.id)

            return True
        except Exception:
            return False
