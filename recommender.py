import os
import json
from openai import OpenAI

# Initialize client to point to Groq
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

class RecommenderAgent:
    def recommend(self, buyer) -> dict:
        # Define valid categories from your catalog.py
        valid_categories = ["smart gadgets", "electronics", "sportswear"]

        prompt = f"""
        User Purchase History: {buyer.history}
        Available Categories: {valid_categories}

        Your Role: You are a "Lifestyle Curator" AI. Your goal is to build a balanced, high-quality collection for the user.

        Evaluation Strategy:
        1. Analyze the 'Category Density': Has the user already built a strong foundation in one area ?
        2. Identify Gaps: If they are tech-heavy, do they lack 'Sportswear' for health or 'Smart Gadgets' for convenience?
        3. Make a Strategic Choice: Decide whether to 'Deepen' their current interest or 'Diversify' into a new category to balance their lifestyle. 
        4. No Hard Limits: You decide when they have "enough" of a category based on the items' utility.

        Constraint: The 'recommended_category' MUST be exactly one of: {valid_categories}.

        Respond ONLY in valid JSON:
        {{
          "recommended_category": "category name",
          "reason": "Provide a high-level strategic justification for this specific pivot or focus."
        }}
        """

        # Fallback if API fails
        fallback = {
            "recommended_category": "smart gadgets",
            "reason": "Based on your tech and fitness history, smart gadgets are the perfect next step."
        }

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[
                    {"role": "system", "content": "you are a strategic personal shopper focused on lifestyle curation and variety. You only speak JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                response_format={"type": "json_object"}
            )

            res_text = response.choices[0].message.content.strip()
            return json.loads(res_text)
        except Exception as e:
            print(f"LLM Error (Falling back): {e}")
            return fallback