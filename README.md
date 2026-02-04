# 🛒 AI-Powered Personalized Shopping Assistant

A modular AI agent that simulates a personalized shopping assistant.

The system analyzes a buyer’s purchase history, recommends products using intelligent reasoning via Llama 3, searches a product catalog, simulates purchases, and persistently stores user memory.

This project demonstrates agent orchestration, LLM integration via Groq, clean modular design, and memory persistence.
---

## 🚀 Features

- 📥 Accepts structured buyer history (JSON)
- 🧠 LLM-Powered Reasoning: Uses Llama-3.3-70b (via Groq) for natural language product justifications.
- 🔍 Product search from a mock catalog
- 🛍️ Simulated purchase flow
- 💾 Persistent memory across runs (JSON-based)
- 🔁 Safe to run multiple times without duplicate purchases
- 🔐 Secure OpenAI API key handling (environment variables)

---

## 🧱 Project Structure

```text
ShoppingAssistant/
│
├── main.py                # Orchestrates the full agent workflow
├── buyer.py               # Buyer profile & analytics
├── recommender.py         # Groq/LLM-based recommendation agent
├── searcher.py            # Product search & ranking
├── purchase.py            # Simulated purchase agent
├── memory.py              # Persistent memory store (JSON)
├── buyer_memory.json      # Stored buyer interaction history
├── catalog.json           # mocks products catalog data
└── README.md

🧩 Workflow Overview
Load Buyer History

Reads buyer profile from input JSON

Loads stored memory if available

Recommendation (LLM-powered)

Analyzes historical purchases

Recommends a new product category

Provides a natural language explanation

Product Search

Queries a mock product catalog

Ranks products based on inferred user preferences

Simulated Purchase

Selects the best matching product

Records the transaction

Memory Update

Deduplicates purchases

Persists updated buyer history to disk

🧠 Example Buyer Input
JSON
{
  "user_id": "A123",
  "history": [
    { "product": "Bluetooth headphones", "category": "electronics", "price": 120 },
    { "product": "Running shoes", "category": "sportswear", "price": 80 }
  ]
}

▶️ How to Run the Project
1️⃣ Create & Activate Virtual Environment (Recommended)

python -m venv venv

Windows (PowerShell):

.\venv\Scripts\activate
macOS / Linux:

source venv/bin/activate
2️⃣ Install Dependencies

pip install openai  # Used as the SDK for Groq

3️⃣ LLM API Setup (Groq)
This project is configured to use Groq for high-speed inference.

✅ Option A — Full AI Mode Set your Groq API key as an environment variable:

Set your API key as an environment variable.

# Windows (PowerShell)
$env:GROQ_API_KEY="your_groq_api_key_here"

# macOS/Linux
export GROQ_API_KEY="your_groq_api_key_here"

Then run: python main.py

✅ Option B — Fallback Mode If no API key is detected, the system automatically uses deterministic recommendation logic.
 This ensures the agent never crashes and remains functional in offline or restricted environments.

📦 Persistent Memory
Buyer interactions are stored in buyer_memory.json.

Memory persists across runs

Duplicate purchases are automatically avoided

The agent evolves its recommendations over time

Example stored memory:


{
  "A123": [
    { "product": "Bluetooth headphones", "category": "electronics", "price": 120 },
    { "product": "Running shoes", "category": "sportswear", "price": 80 },
    { "product": "Smartwatch", "category": "smart gadgets", "price": 150 }
  ]
}

🧪 Safe Re-Runs
You can run python main.py multiple times without:

Duplicating purchases

Corrupting memory

Requiring manual cleanup

🎯 Objective Alignment
This project fulfills all requirements of the assignment:

✔ Buyer history ingestion

✔ LLM-driven recommendation with justification

✔ Product search and ranking

✔ Simulated purchase

✔ Persistent memory handling

👨‍💻 Author
Adham Essam Software Engineer
