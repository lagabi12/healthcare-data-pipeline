import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Eliminar columnas no útiles
    columns_to_drop = [
        "encounter_id",
        "patient_nbr"
    ]

    df = df.drop(columns=columns_to_drop, errors="ignore")

    # 3. Manejo de valores nulos
    df = df.dropna(thresh=int(len(df.columns) * 0.7))

    # 4. Normalizar valores categóricos
    if "gender" in df.columns:
        df["gender"] = df["gender"].replace(
            {"Unknown/Invalid": "Unknown"}
        )

    # 5. Conversión de tipos (ejemplo)
    if "age" in df.columns:
        df["age"] = df["age"].astype(str)

    logger.info("Data transformed successfully")
    return df

