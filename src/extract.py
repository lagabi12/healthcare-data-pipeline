import pandas as pd
from pathlib import Path

def extract_data():
    file_path = "C:/Users/gabid/OneDrive/Escritorio/healthcare-data-pipeline/data/raw/diabetic_data.csv"

    df = pd.read_csv(file_path)

    print("Data extracted successfully")
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))

    return df

if __name__ == "__main__":
    extract_data()
