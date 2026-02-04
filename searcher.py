from catalog import PRODUCT_CATALOG


class ProductSearcher:
    def search(self, category: str, user_avg_spend: float):
        filtered_products = [
            product for product in PRODUCT_CATALOG
            if product["category"] == category
        ]

        ranked_products = sorted(
            filtered_products,
            key=lambda p: abs(p["price"] - user_avg_spend)
        )

        return ranked_products[:3]
