from typing import Dict, List


class BuyerProfile:
    def __init__(self, user_id: str, history: List[Dict]):
        self.user_id = user_id
        self.history = history

    @staticmethod
    def from_json(data: Dict) -> "BuyerProfile":
        if "user_id" not in data:
            raise ValueError("Missing user_id")

        if "history" not in data or not isinstance(data["history"], list):
            raise ValueError("History must be a list")

        for item in data["history"]:
            if not all(key in item for key in ("product", "category", "price")):
                raise ValueError("Each history item must contain product, category, and price")

        return BuyerProfile(
            user_id=data["user_id"],
            history=data["history"]
        )

    def average_spend(self) -> float:
        total = sum(item["price"] for item in self.history)
        return total / len(self.history) if self.history else 0.0
