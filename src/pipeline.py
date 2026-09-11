from .analysis import create_reports

from .config import CLEAN_FILE

from .data_cleaning import clean_data

from .data_loader import (
    inspect_data,
    load_data
)

from .feature_engineering import (
    create_features
)

from .generate_data import (
    generate_sales_data
)

from .model import train_model


def run_pipeline() -> None:

    print("=" * 60)

    print(
        "RETAIL SALES DATA PIPELINE"
    )

    print("=" * 60)


    # =================================
    # STEP 1
    # Generate raw data
    # =================================

    print(
        "\n[1/7] Generating raw data..."
    )


    generate_sales_data()


    # =================================
    # STEP 2
    # Load data
    # =================================

    print(
        "\n[2/7] Loading raw data..."
    )


    df = load_data()


    print(
        f"Loaded shape: {df.shape}"
    )


    # =================================
    # STEP 3
    # Inspect data
    # =================================

    print(
        "\n[3/7] Inspecting raw data..."
    )


    inspect_data(df)


    # =================================
    # STEP 4
    # Clean data
    # =================================

    print(
        "\n[4/7] Cleaning data..."
    )


    df = clean_data(
        df
    )


    print(
        f"After cleaning: {df.shape}"
    )


    # =================================
    # STEP 5
    # Feature engineering
    # =================================

    print(
        "\n[5/7] Creating features..."
    )


    df = create_features(
        df
    )


    # Save cleaned dataset
    df.to_csv(
        CLEAN_FILE,
        index=False
    )


    print(
        f"Saved: {CLEAN_FILE}"
    )


    # =================================
    # STEP 6
    # Analysis
    # =================================

    print(
        "\n[6/7] Creating reports..."
    )


    create_reports(
        df
    )


    print(
        "Reports created."
    )


    # =================================
    # STEP 7
    # Machine Learning
    # =================================

    print(
        "\n[7/7] Training model..."
    )


    metrics = train_model(
        df
    )


    print(
        "\nModel metrics:"
    )


    for name, value in metrics.items():

        print(
            f"{name}: {value:,.4f}"
        )


    print(
        "\nPipeline completed successfully."
    )