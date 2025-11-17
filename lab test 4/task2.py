import numpy as np
import pandas as pd

def generate_healthcare_dataset(n_rows=200, seed=42, missing_rate=0.1):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "patient_id": np.arange(1, n_rows + 1),
        "age": rng.integers(18, 90, size=n_rows),
        "systolic_bp": rng.integers(90, 190, size=n_rows),
        "diastolic_bp": rng.integers(50, 110, size=n_rows),
        "cholesterol": rng.integers(120, 320, size=n_rows),
        "heart_rate": rng.integers(50, 110, size=n_rows),
        "diagnosis_score": rng.normal(loc=3.0, scale=1.0, size=n_rows),
        "gender": rng.choice(["M", "F"], size=n_rows),
    })





    # Introduce missing values randomly in numeric columns
    numeric_cols = ["age", "systolic_bp", "diastolic_bp", "cholesterol", "heart_rate", "diagnosis_score"]
    mask = rng.random((n_rows, len(numeric_cols))) < missing_rate
    for j, col in enumerate(numeric_cols):
        df.loc[mask[:, j], col] = np.nan

    return df


def fill_numeric_with_median(df, numeric_cols):
    df = df.copy()
    for col in numeric_cols:
        median = df[col].median()
        df[col] = df[col].fillna(median)
    return df


def min_max_scale(df, numeric_cols):
    df = df.copy()
    for col in numeric_cols:
        col_min = df[col].min()
        col_max = df[col].max()
        if pd.isna(col_min) or pd.isna(col_max):
            df[col] = np.nan
        elif col_max == col_min:
            df[col] = 0.0  # constant column -> all zeros after scaling
        else:
            df[col] = (df[col] - col_min) / (col_max - col_min)
    return df


def main():
    df = generate_healthcare_dataset(n_rows=200, seed=1, missing_rate=0.12)
    numeric_cols = ["age", "systolic_bp", "diastolic_bp", "cholesterol", "heart_rate", "diagnosis_score"]

    print("Sample before handling missing / scaling:")
    print(df.head(), "\n")

    df_filled = fill_numeric_with_median(df, numeric_cols)
    print("After filling missing values with medians (sample):")
    print(df_filled.head(), "\n")

    df_scaled = min_max_scale(df_filled, numeric_cols)
    print("After Min-Max scaling numeric columns (sample):")
    print(df_scaled.head(), "\n")

    # Save results
    df_scaled.to_csv("healthcare_dataset_scaled.csv", index=False)
    print("Saved scaled dataset to healthcare_dataset_scaled.csv")


if __name__ == "__main__":

    main()
    





