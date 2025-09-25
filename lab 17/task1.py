import pandas as pd
import string
import re

# File path (your dataset)
file_path = "social_media (1).csv"  # Use relative path to avoid issues

# Load dataset
df = pd.read_csv(file_path)

# Custom stopword list (minimal)
custom_stopwords = {
    "a", "an", "the", "is", "are", "was", "were", "in", "on", "at", "for",
    "of", "and", "or", "to", "with", "this", "that", "it", "be", "by", "as",
    "from", "but", "about", "into", "over", "after"
}

# Clean text function
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r"<.*?>", "", text)   # remove HTML tags
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    text = text.lower()  # lowercase
    words = [word for word in text.split() if word not in custom_stopwords]  # remove stopwords
    return " ".join(words)

# 1. Clean post_text
df["clean_post_text"] = df["post_text"].apply(clean_text)

# 2. Handle missing values
df["likes"] = df["likes"].fillna(0).astype(int)
df["shares"] = df["shares"].fillna(0).astype(int)

# 3. Convert timestamp to datetime and extract features
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["weekday"] = df["timestamp"].dt.day_name()

# 4. Remove duplicates (spam check: same user + same cleaned text)
df_cleaned = df.drop_duplicates(subset=["clean_post_text", "user"])

# Save cleaned dataset back to the same folder
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"social_media_cleaned_{timestamp}.csv"  # Use relative path

try:
    df_cleaned.to_csv(output_path, index=False)
    print("✅ Cleaning complete! File saved at:", output_path)
except PermissionError:
    print(f"⚠️  Permission denied for '{output_path}' - file may be open in another application")
    print("💡 Please close any CSV files and try running the script again")
    print("📊 Data cleaning completed successfully, but file save failed")

print(df_cleaned.head())
