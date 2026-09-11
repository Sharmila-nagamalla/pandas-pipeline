import numpy as np
import pandas as pd

from .config import RAW_FILE, RANDOM_STATE


def generate_sales_data(n_rows: int = 1200) -> pd.DataFrame:

    # Random number generator
    rng = np.random.default_rng(RANDOM_STATE)


    # Products
    products = [
        "Laptop",
        "Phone",
        "Tablet",
        "Headphones",
        "Monitor"
    ]


    # Product -> category mapping
    categories = {
        "Laptop": "Electronics",
        "Phone": "Electronics",
        "Tablet": "Electronics",
        "Headphones": "Accessories",
        "Monitor": "Electronics"
    }


    # Other categorical values
    regions = [
        "North",
        "South",
        "East",
        "West"
    ]

    payment_methods = [
        "UPI",
        "Card",
        "Cash",
        "Net Banking"
    ]


    # Random product for every order
    product = rng.choice(
        products,
        n_rows
    )


    # Quantity between 1 and 7
    quantity = rng.integers(
        1,
        8,
        n_rows
    )


    # Product prices
    unit_price = (
        pd.Series(product)
        .map({
            "Laptop": 65000,
            "Phone": 30000,
            "Tablet": 22000,
            "Headphones": 3500,
            "Monitor": 15000
        })
        .to_numpy()
    )


    # Random discount between 0% and 25%
    discount = rng.uniform(
        0,
        0.25,
        n_rows
    )


    # Revenue
    revenue = (
        quantity
        * unit_price
        * (1 - discount)
    )


    # Dates
    dates = pd.date_range(
        "2025-01-01",
        "2025-12-31",
        freq="D"
    )


    # Random order dates
    order_date = rng.choice(
        dates,
        n_rows
    )


    # Create DataFrame
    df = pd.DataFrame({

        "order_id": [
            f"ORD{i:05d}"
            for i in range(1, n_rows + 1)
        ],

        "order_date": order_date,

        "product": product,

        "category": (
            pd.Series(product)
            .map(categories)
        ),

        "region": rng.choice(
            regions,
            n_rows
        ),

        "quantity": quantity,

        "unit_price": unit_price,

        "discount": discount,

        "revenue": revenue.round(2),

        "payment_method": rng.choice(
            payment_methods,
            n_rows
        )
    })


    # -------------------------
    # Add missing values
    # -------------------------

    missing_rows = rng.choice(
        df.index,
        25,
        replace=False
    )


    # Missing region
    df.loc[
        missing_rows[:10],
        "region"
    ] = np.nan


    # Missing payment method
    df.loc[
        missing_rows[10:20],
        "payment_method"
    ] = np.nan


    # Missing discount
    df.loc[
        missing_rows[20:],
        "discount"
    ] = np.nan


    # -------------------------
    # Add duplicate rows
    # -------------------------

    duplicate_rows = df.sample(
        15,
        random_state=RANDOM_STATE
    )

    df = pd.concat(
        [
            df,
            duplicate_rows
        ],
        ignore_index=True
    )


    # -------------------------
    # Add extreme values
    # -------------------------

    df.loc[
        df.index[-5:],
        "quantity"
    ] = [
        50,
        60,
        45,
        55,
        70
    ]


    # Save raw data
    df.to_csv(
        RAW_FILE,
        index=False
    )


    return df


if __name__ == "__main__":

    df = generate_sales_data()

    print(
        f"Generated {len(df)} rows"
    )

    print(
        f"Saved to: {RAW_FILE}"
    )