import pandas as pd


def cap_iqr_outliers(
    df: pd.DataFrame,
    column: str,
    multiplier: float = 1.5
) -> pd.DataFrame:

    df = df.copy()


    # First quartile
    q1 = df[column].quantile(
        0.25
    )


    # Third quartile
    q3 = df[column].quantile(
        0.75
    )


    # Interquartile range
    iqr = q3 - q1


    # Lower limit
    lower = (
        q1
        - multiplier * iqr
    )


    # Upper limit
    upper = (
        q3
        + multiplier * iqr
    )


    # Cap extreme values
    df[column] = df[column].clip(
        lower=lower,
        upper=upper
    )


    return df


def clean_data(
    df: pd.DataFrame
) -> pd.DataFrame:

    df = df.copy()


    # ---------------------------------
    # 1. Remove duplicate rows
    # ---------------------------------

    df = df.drop_duplicates()


    # ---------------------------------
    # 2. Convert date column
    # ---------------------------------

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )


    # ---------------------------------
    # 3. Fill categorical missing values
    # ---------------------------------

    df["region"] = df[
        "region"
    ].fillna(
        "Unknown"
    )


    df["payment_method"] = df[
        "payment_method"
    ].fillna(
        "Unknown"
    )


    # ---------------------------------
    # 4. Fill numerical missing values
    # ---------------------------------

    df["discount"] = df[
        "discount"
    ].fillna(
        df["discount"].median()
    )


    # ---------------------------------
    # 5. Remove rows where important
    #    values are missing
    # ---------------------------------

    df = df.dropna(
        subset=[
            "order_id",
            "order_date",
            "product",
            "quantity",
            "unit_price",
            "revenue"
        ]
    )


    # ---------------------------------
    # 6. Convert numeric columns
    # ---------------------------------

    numeric_columns = [

        "quantity",

        "unit_price",

        "discount",

        "revenue"
    ]


    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


    # Remove rows that still contain
    # invalid numeric values

    df = df.dropna(
        subset=numeric_columns
    )


    # ---------------------------------
    # 7. Keep discount between 0 and 1
    # ---------------------------------

    df["discount"] = df[
        "discount"
    ].clip(
        0,
        1
    )


    # ---------------------------------
    # 8. Handle quantity outliers
    # ---------------------------------

    df = cap_iqr_outliers(
        df,
        "quantity"
    )


    # ---------------------------------
    # 9. Sort by date
    # ---------------------------------

    df = df.sort_values(
        "order_date"
    )


    # Reset index
    df = df.reset_index(
        drop=True
    )


    return df