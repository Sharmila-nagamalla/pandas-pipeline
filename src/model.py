import json

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder

from .config import (
    METRICS_FILE,
    MODEL_FILE,
    RANDOM_STATE
)


def train_model(
    df: pd.DataFrame
) -> dict:

    # =================================
    # Features
    # =================================

    features = [

        "quantity",

        "unit_price",

        "discount",

        "region",

        "payment_method",

        "month",

        "is_weekend"
    ]


    # Target
    target = "revenue"


    # X = input
    X = df[
        features
    ]


    # y = output
    y = df[
        target
    ]


    # =================================
    # Categorical columns
    # =================================

    categorical_features = [

        "region",

        "payment_method"
    ]


    # =================================
    # Numerical columns
    # =================================

    numeric_features = [

        "quantity",

        "unit_price",

        "discount",

        "month",

        "is_weekend"
    ]


    # =================================
    # Preprocessing
    # =================================

    preprocessor = ColumnTransformer(

        transformers=[

            (
                "categorical",

                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                ),

                categorical_features
            ),

            (
                "numeric",

                "passthrough",

                numeric_features
            )
        ]
    )


    # =================================
    # Complete ML pipeline
    # =================================

    pipeline = Pipeline(

        steps=[

            (
                "preprocessor",

                preprocessor
            ),

            (
                "model",

                LinearRegression()
            )
        ]
    )


    # =================================
    # Train/test split
    # =================================

    X_train, X_test, y_train, y_test = (

        train_test_split(

            X,

            y,

            test_size=0.2,

            random_state=RANDOM_STATE
        )
    )


    # =================================
    # Train
    # =================================

    pipeline.fit(
        X_train,
        y_train
    )


    # =================================
    # Prediction
    # =================================

    predictions = pipeline.predict(
        X_test
    )


    # =================================
    # Evaluation
    # =================================

    mae = mean_absolute_error(
        y_test,
        predictions
    )


    rmse = (
        mean_squared_error(
            y_test,
            predictions
        )
        ** 0.5
    )


    r2 = r2_score(
        y_test,
        predictions
    )


    metrics = {

        "MAE": float(mae),

        "RMSE": float(rmse),

        "R2": float(r2)
    }


    # =================================
    # Save model
    # =================================

    joblib.dump(
        pipeline,
        MODEL_FILE
    )


    # =================================
    # Save metrics
    # =================================

    with open(
        METRICS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metrics,
            file,
            indent=4
        )


    return metrics