# Retail Sales Data Pipeline

A complete Python and Pandas-based data science project that demonstrates an end-to-end data pipeline:

**Raw Data → Loading → Inspection → Cleaning → Feature Engineering → Analysis → Machine Learning → Evaluation → Model Saving**

---

## 📌 Project Overview

The Retail Sales Data Pipeline is an end-to-end Data Science project built using Python, Pandas, NumPy, and Scikit-learn.

The project takes raw retail sales data, cleans and transforms it, performs business analysis, creates useful features, trains a Machine Learning model, evaluates the model, and saves the trained model for future predictions.

The project is designed to demonstrate important Data Science concepts used in real-world projects.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Load raw sales data
- Inspect the dataset
- Identify missing values
- Identify duplicate records
- Convert incorrect data types
- Handle missing values
- Handle outliers
- Perform feature engineering
- Perform business analysis
- Generate summary reports
- Train a Machine Learning model
- Evaluate the model
- Save the trained model
- Create a reusable data pipeline

---

## 🏗️ Project Architecture

```text
                    RAW DATA
                       |
                       ↓
              sales_raw.csv
                       |
                       ↓
               data_loader.py
                       |
                       ↓
              Data Inspection
                       |
                       ↓
              data_cleaning.py
                       |
                       ↓
               Cleaned Data
                       |
                       ↓
          feature_engineering.py
                       |
                       ↓
              New Features
                       |
                       ↓
                 analysis.py
                       |
              ┌────────┴────────┐
              ↓                 ↓
        Business Reports    ML Dataset
                                |
                                ↓
                            model.py
                                |
                                ↓
                       Linear Regression
                                |
                                ↓
                         Model Evaluation
                                |
                    ┌───────────┴───────────┐
                    ↓                       ↓
          sales_model.joblib          metrics.json