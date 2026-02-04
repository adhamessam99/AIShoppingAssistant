import json
import os
from typing import Dict, List

MEMORY_FILE = "buyer_memory.json"


class MemoryStore:
    def __init__(self, file_path: str = MEMORY_FILE):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

    def load_user_history(self, user_id: str) -> List[Dict]:
        
        with open(self.file_path, "r") as f:
            data = json.load(f)

        return data.get(user_id, [])

    def save_user_history(self, user_id: str, history: List[Dict]):
        with open(self.file_path, "r") as f:
            data = json.load(f)

        data[user_id] = history

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)