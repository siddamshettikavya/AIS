# Sample user history
user_history = ["electronics", "books"]

# Sample products
products = {
    "electronics": ["USB cable", "Bluetooth speaker"],
    "books": ["Learn Python", "AI Ethics"]
}

# Recommend products based on history
for category in user_history:
    print(f"\nBecause you viewed '{category}', you might like:")
    for item in products[category]:
        print(f"- {item}")

# Ask for feedback with basic protection
def is_clean(comment):
    # List of blocked words (can be expanded)
    blocked_words = ["bad", "stupid", "hate", "worst"]
    for word in blocked_words:
        if word in comment.lower():
            return False
    return True

# Collect feedback
feedback = input("\nLeave a comment about these recommendations: ")

if is_clean(feedback):
    print("✅ Thanks for your feedback!")
else:
    print("⚠️ Please avoid using inappropriate words in your comment.")