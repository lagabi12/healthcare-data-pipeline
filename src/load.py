from pathlib import Path
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
def load_data(df: pd.DataFrame):
    output_dir = Path("../data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "diabetic_data_processed.csv"
    df.to_csv(output_path, index=False)

    logger.info(f"Data loaded successfully → {output_path}")

