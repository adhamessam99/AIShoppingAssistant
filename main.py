from buyer import BuyerProfile
from recommender import RecommenderAgent
from searcher import ProductSearcher
from purchase import PurchaseAgent
from memory import MemoryStore

buyer_json = {
    "user_id": "A123",
    "history": [
        {"product": "Bluetooth headphones", "category": "electronics", "price": 120},
        {"product": "Running shoes", "category": "sportswear", "price": 80}
    ]
}

def main():
    memory = MemoryStore()

    # Load past memory
    stored_history = memory.load_user_history(buyer_json["user_id"])
    if stored_history:  
        buyer_json["history"] = stored_history

    # Load buyer
    buyer = BuyerProfile.from_json(buyer_json)

    # LLM recommendation
    recommender = RecommenderAgent()
    recommendation = recommender.recommend(buyer)

    print("\nRecommended Category:")
    print(f"- {recommendation['recommended_category']}")
    print(f"Reason: {recommendation['reason']}")

    # Product search
    searcher = ProductSearcher()
    all_products = searcher.search(
        category=recommendation["recommended_category"],
        user_avg_spend=buyer.average_spend()
    )

    # Normalize what we already bought
    purchased_products = {item["product"].strip().lower() for item in buyer.history}

    # Normalize the catalog check
    top_products = [
        p for p in all_products 
        if p["product"].strip().lower() not in purchased_products
]

    if not top_products:
        print("\nNo new products to recommend. You've purchased all items in this category!")
        return

    print("\nTop Recommended Products:")
    for idx, product in enumerate(top_products, 1):
        print(f"{idx}. {product['product']} - ${product['price']}")

    # Purchase the first new product
    purchase_agent = PurchaseAgent()
    selected_product = top_products[0]

    purchase = purchase_agent.buy(
        user_id=buyer.user_id,
        product=selected_product
    )

    print("\nPurchase Successful 🎉")
    print(f"You bought: {purchase['product']}")
    print(f"Price: ${purchase['price']}")

    # Update memory
    updated_history = buyer.history + [purchase]

    # Deduplicate
    deduped_history = { 
        item["product"].strip().lower(): item 
        for item in updated_history 
}
    memory.save_user_history(buyer.user_id, list(deduped_history.values()))

    print("\nMemory Updated ✔")

if __name__ == "__main__":
    main()
