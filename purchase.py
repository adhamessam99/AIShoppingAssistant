# purchase.py
from typing import Dict, List


class PurchaseAgent:
    def __init__(self):
        self.purchases: List[Dict] = []

    def buy(self, user_id: str, product: Dict) -> Dict:
        purchase_record = {
            "user_id": user_id,
            "product": product["product"],
            "category": product["category"],
            "price": product["price"]
        }

        self.purchases.append(purchase_record)
        return purchase_record

    def get_history(self, user_id: str) -> List[Dict]:
        return [p for p in self.purchases if p["user_id"] == user_id]
