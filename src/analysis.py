import pandas as pd

from .config import REPORT_DIR


def create_reports(
    df: pd.DataFrame
) -> None:

    # =================================
    # Overall sales summary
    # =================================

    summary = pd.DataFrame({

        "metric": [

            "total_orders",

            "total_revenue",

            "average_order_value",

            "total_quantity",

            "total_profit"
        ],


        "value": [

            df["order_id"].nunique(),

            df["revenue"].sum(),

            df["revenue"].mean(),

            df["quantity"].sum(),

            df["profit"].sum()
        ]
    })


    # =================================
    # Category summary
    # =================================

    category_summary = (

        df.groupby(
            "category",
            as_index=False
        )

        .agg(

            total_revenue=(
                "revenue",
                "sum"
            ),

            average_revenue=(
                "revenue",
                "mean"
            ),

            total_quantity=(
                "quantity",
                "sum"
            ),

            total_profit=(
                "profit",
                "sum"
            )
        )

        .sort_values(
            "total_revenue",
            ascending=False
        )
    )


    # =================================
    # Monthly summary
    # =================================

    monthly_summary = (

        df.groupby(
            [
                "year",
                "month"
            ],
            as_index=False
        )

        .agg(

            total_revenue=(
                "revenue",
                "sum"
            ),

            total_orders=(
                "order_id",
                "nunique"
            ),

            total_quantity=(
                "quantity",
                "sum"
            )
        )

        .sort_values(
            [
                "year",
                "month"
            ]
        )
    )


    # =================================
    # Region summary
    # =================================

    region_summary = (

        df.groupby(
            "region",
            as_index=False
        )

        .agg(

            total_revenue=(
                "revenue",
                "sum"
            ),

            total_orders=(
                "order_id",
                "nunique"
            )
        )

        .sort_values(
            "total_revenue",
            ascending=False
        )
    )


    # =================================
    # Save reports
    # =================================

    summary.to_csv(
        REPORT_DIR
        / "sales_summary.csv",

        index=False
    )


    category_summary.to_csv(
        REPORT_DIR
        / "category_summary.csv",

        index=False
    )


    monthly_summary.to_csv(
        REPORT_DIR
        / "monthly_summary.csv",

        index=False
    )


    region_summary.to_csv(
        REPORT_DIR
        / "region_summary.csv",

        index=False
    )


    # =================================
    # Pivot table
    # =================================

    pivot = pd.pivot_table(

        df,

        index="region",

        columns="category",

        values="revenue",

        aggfunc="sum",

        fill_value=0
    )


    pivot.to_csv(
        REPORT_DIR
        / "region_category_pivot.csv"
    )