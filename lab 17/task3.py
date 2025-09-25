import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
file_path = "iot_sensor.csv"  # Use relative path
df = pd.read_csv(file_path)

# 1. Handle missing values (forward fill)
df = df.ffill()  # Updated syntax for pandas
# 2. Remove sensor drift (apply rolling mean with window=3)
df["temperature_smooth"] = df["temperature"].rolling(window=3, min_periods=1).mean()
df["humidity_smooth"] = df["humidity"].rolling(window=3, min_periods=1).mean()

# 3. Normalize readings using Standard Scaler
scaler = StandardScaler()
df[["temperature_norm", "humidity_norm"]] = scaler.fit_transform(
    df[["temperature_smooth", "humidity_smooth"]]
)

# 4. Encode categorical sensor IDs
if "sensor_id" in df.columns:
    le = LabelEncoder()
    df["sensor_id_encoded"] = le.fit_transform(df["sensor_id"])

# Save cleaned dataset
import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"iot_sensor_cleaned_{timestamp}.csv"  # Use relative path

try:
    df.to_csv(output_path, index=False)
    print("✅ IoT sensor data cleaned and saved at:", output_path)
except PermissionError:
    print(f"⚠️  Permission denied for '{output_path}' - file may be open in another application")
    print("💡 Please close any CSV files and try running the script again")
    print("📊 Data cleaning completed successfully, but file save failed")

print(df.head())
