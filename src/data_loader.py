import pandas as pd

from .config import RAW_FILE


# Columns that must exist
REQUIRED_COLUMNS = [

    "order_id",

    "order_date",

    "product",

    "category",

    "region",

    "quantity",

    "unit_price",

    "discount",

    "revenue",

    "payment_method"
]


def load_data(path=RAW_FILE) -> pd.DataFrame:

    # Read CSV
    df = pd.read_csv(path)


    # Check required columns
    missing_columns = [

        column

        for column in REQUIRED_COLUMNS

        if column not in df.columns
    ]


    # If any columns are missing
    if missing_columns:

        raise ValueError(
            f"Missing required columns: "
            f"{missing_columns}"
        )


    return df


def inspect_data(df: pd.DataFrame) -> None:

    print("\n--- SHAPE ---")

    print(
        df.shape
    )


    print("\n--- DATA TYPES ---")

    print(
        df.dtypes
    )


    print("\n--- MISSING VALUES ---")

    print(
        df.isnull().sum()
    )


    print("\n--- DUPLICATE ROWS ---")

    print(
        df.duplicated().sum()
    )


    print("\n--- NUMERIC SUMMARY ---")

    print(
        df.describe()
    )