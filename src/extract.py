import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def extract_data():
    file_path = "C:/Users/gabid/OneDrive/Escritorio/healthcare-data-pipeline/data/raw/diabetic_data.csv"

    df = pd.read_csv(file_path)

    logger.info("Data extracted successfully")
    logger.info("Shape:", df.shape)
    logger.info("Columns:", list(df.columns))

    return df

if __name__ == "__main__":
    extract_data()

from transform import transform_data
from load import load_data

if __name__ == "__main__":
    df = extract_data()
    df_transformed = transform_data(df)
    load_data(df_transformed)

