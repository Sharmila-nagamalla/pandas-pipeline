import numpy as np
import pandas as pd


def create_features(
    df: pd.DataFrame
) -> pd.DataFrame:

    df = df.copy()


    # ---------------------------------
    # Date features
    # ---------------------------------

    df["year"] = (
        df["order_date"]
        .dt.year
    )


    df["month"] = (
        df["order_date"]
        .dt.month
    )


    df["month_name"] = (
        df["order_date"]
        .dt.month_name()
    )


    df["day_of_week"] = (
        df["order_date"]
        .dt.day_name()
    )


    # ---------------------------------
    # Weekend feature
    # ---------------------------------

    df["is_weekend"] = (
        df["order_date"]
        .dt.dayofweek >= 5
    )


    # ---------------------------------
    # Gross sales
    # ---------------------------------

    df["gross_sales"] = (
        df["quantity"]
        * df["unit_price"]
    )


    # ---------------------------------
    # Discount amount
    # ---------------------------------

    df["discount_amount"] = (
        df["gross_sales"]
        * df["discount"]
    )


    # ---------------------------------
    # Profit
    # Assume 15% profit margin
    # ---------------------------------

    df["profit"] = (
        df["revenue"]
        * 0.15
    )


    # ---------------------------------
    # Profit margin
    # ---------------------------------

    df["profit_margin"] = np.where(

        df["revenue"] > 0,

        df["profit"]
        / df["revenue"],

        0
    )


    # ---------------------------------
    # map() example
    # ---------------------------------

    region_code = {

        "North": 1,

        "South": 2,

        "East": 3,

        "West": 4,

        "Unknown": 0
    }


    df["region_code"] = (

        df["region"]
        .map(region_code)
        .fillna(0)
    )


    # ---------------------------------
    # apply() example
    # ---------------------------------

    df["order_size"] = (

        df["revenue"]

        .apply(
            lambda x:
            "High"
            if x >= 50000
            else "Low"
        )
    )


    # Convert boolean to integer
    df["is_weekend"] = (
        df["is_weekend"]
        .astype(int)
    )


    return df