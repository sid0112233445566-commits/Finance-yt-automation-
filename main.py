import datetime

print("--- US Finance YouTube Automation Bot ---")
print("Execution Time:", datetime.datetime.now())

# US Finance topics aur unke chote outlines/scripts
finance_content = {
    "5 Smart Ways to Save Money in the US": """# 5 Smart Ways to Save Money in the US
1. Automate your savings as soon as your paycheck hits.
2. Cut down on high-subscription models and unused apps.
3. Use high-yield savings accounts (HYSAs) for better interest.
4. Cook meals at home instead of dining out in US cities.
5. Review and negotiate your utility and insurance bills annually.""",
    
    "How to Build an Emergency Fund from Scratch": """# How to Build an Emergency Fund from Scratch
1. Set a realistic target (3 to 6 months of living expenses).
2. Start small: save even $20 or $50 a week.
3. Keep the money separate in a high-yield savings account.
4. Direct any tax refunds or side hustle money straight into this fund."""
}

# Aaj ke din ke hisab se topic select karna
topics = list(finance_content.keys())
day_index = datetime.datetime.now().day % len(topics)
selected_topic = topics[day_index]
script_text = finance_content[selected_topic]

# File ke andar script save karna
filename = "generated_script.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(script_text)

print(f"\n[SUCCESS] Script generated for topic: {selected_topic}")
print(f"File saved successfully as {filename}")
