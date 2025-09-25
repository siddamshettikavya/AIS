import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('financial_data.csv')  # Load the financial data

# 1️⃣ Handle missing values in closing_price and volume
df['closing_price'] = df['closing_price'].ffill().bfill()
df['volume'] = df['volume'].fillna(0)

# 2️⃣ Create lag features: 1-day and 7-day returns
df['return_1d'] = df['closing_price'].pct_change(periods=1)  # Daily return: (today - yesterday) / yesterday
df['return_7d'] = df['closing_price'].pct_change(periods=7)  # Weekly return: (today - 7_days_ago) / 7_days_ago

# 3️⃣ Normalize volume using log-scaling
df['volume_log'] = np.log1p(df['volume'])  # log1p handles zero safely

# 4️⃣ Detect outliers in closing_price using IQR method
Q1 = df['closing_price'].quantile(0.25)
Q3 = df['closing_price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Flag and optionally remove outliers
df['is_outlier'] = (df['closing_price'] < lower_bound) | (df['closing_price'] > upper_bound)
df_filtered = df[df['is_outlier'] == False].copy()

# ✅ Final dataset ready for forecasting
df_final = df_filtered[['date', 'closing_price', 'return_1d', 'return_7d', 'volume_log']]
# Display results
print("✅ Financial data preprocessing completed successfully!")
print(f"📊 Original dataset shape: {df.shape}")
print(f"📊 Filtered dataset shape (no outliers): {df_filtered.shape}")
print("\n📝 Sample of final data:")
print(df_final.head())
print(f"\n📈 Summary statistics:")
print(f"Total records: {len(df_final)}")
print(f"Average closing price: {df_final['closing_price'].mean():.2f}")
print(f"Average 1-day return: {df_final['return_1d'].mean():.4f}")
print(f"Average 7-day return: {df_final['return_7d'].mean():.4f}")
print(f"Average log-volume: {df_final['volume_log'].mean():.2f}")

# Save the final preprocessed data to a new CSV file
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f'financial_data_preprocessed_{timestamp}.csv'
try:
    df_final.to_csv(output_filename, index=False)
    print(f"\n✅ Preprocessed data saved to '{output_filename}'")
except PermissionError:
    print(f"\n⚠️  Permission denied for '{output_filename}' - file may be open in another application")
    print("💡 Please close any CSV files and try running the script again")
    print("📊 Data processing completed successfully, but file save failed")
