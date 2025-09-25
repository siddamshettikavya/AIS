import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Load dataset
df = pd.read_csv("movie_reviews-1.csv")

# 2. Clean text (lowercase + remove HTML tags)
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"<.*?>", " ", str(text))   # remove HTML tags
    return re.sub(r"\s+", " ", text).strip().lower()

df["review_clean"] = df["review_text"].apply(clean_text)

# 3. Handle missing ratings (fill with median)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
median_rating = df["rating"].median()
df["rating_filled"] = df["rating"].fillna(median_rating)

# 4. Normalize ratings (0–10 → 0–1)
df["rating_normalized"] = df["rating_filled"] / 10

# 5. TF-IDF encoding
vectorizer = TfidfVectorizer(max_features=500, stop_words="english")
X_tfidf = vectorizer.fit_transform(df["review_clean"])

# 6. Summary before vs after
print("Before Cleaning:")
print(df[["review_text", "rating"]].head(), "\n")
print("After Cleaning:")
print(df[["review_clean", "rating_filled", "rating_normalized"]].head())

# ✅ Simple Assert Tests
assert not df["review_clean"].str.contains("<|>", regex=True).any()  # no HTML
assert df["rating_filled"].isna().sum() == 0                        # no missing ratings
assert df["rating_normalized"].between(0,1).all()                   # normalized in [0,1]

print("\n✅ All assertions passed! Data cleaning successful.")

# Save cleaned dataset
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"movie_reviews_cleaned_{timestamp}.csv"

try:
    # Save the final cleaned dataset
    df_clean = df[["review_id", "review_clean", "rating_filled", "rating_normalized"]]
    df_clean.to_csv(output_path, index=False)
    print(f"✅ Cleaned movie reviews saved to: {output_path}")
except PermissionError:
    print(f"⚠️  Permission denied for '{output_path}' - file may be open in another application")
    print("💡 Please close any CSV files and try running the script again")
    print("📊 Data cleaning completed successfully, but file save failed")
