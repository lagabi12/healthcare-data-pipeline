from pathlib import Path
import pandas as pd

def load_data(df: pd.DataFrame):
    output_dir = Path("../data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "diabetic_data_processed.csv"
    df.to_csv(output_path, index=False)

    print(f"Data loaded successfully → {output_path}")

