# Pandas Pre-Summarization Profiler
# profiler.py
# This module provides functions to profile a DataFrame before summarization.
# SPDX-License-Identifier: MIT

import pandas as pd


def parse_dates(df):
    # Returns a copy of df with any date-like object columns converted to datetime
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        try:
            converted = pd.to_datetime(df[col], format="mixed", errors="coerce")
            if converted.notna().sum() > len(df) * 0.9:  # 90%+ parsed successfully
                df[col] = converted
        except Exception:
            continue
    return df


def build_base_profile(df):
    """
    Returns a plain-text statistical profile of the DataFrame.
    Includes shape, dtypes, null counts, numeric stats, and top categorical values.
    Does not mutate the input DataFrame.

    Returns: str
    """
    lines = []
    df = parse_dates(df)

    # Shape
    num_rows, num_cols = df.shape
    lines.append(f"Rows: {num_rows}")
    lines.append(f"Columns: {num_cols}")
    lines.append("")

    # Dtypes and null counts
    lines.append("Column Overview:")
    for col in df.columns:
        null_count = df[col].isna().sum()
        lines.append(f"  {col} ({df[col].dtype}) — {null_count} nulls")
    lines.append("")

    # Numeric stats
    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) > 0:
        lines.append("Numeric Column Stats:")
        lines.append(df[numeric_cols].describe().to_string())
        lines.append("")

    # Standout values with date context
    date_cols = df.select_dtypes(include=["datetime64"]).columns
    if len(date_cols) > 0 and len(numeric_cols) > 0:
        date_col = date_cols[0]
        show_all_cols = len(df.columns) <= 5
        lines.append("Standout Values:")
        for col in numeric_cols:
            if show_all_cols:
                top5 = df.nlargest(5, col).to_string(index=False)
                bottom5 = df.nsmallest(5, col).to_string(index=False)
            else:
                top5 = df[[date_col, col]].nlargest(5, col).to_string(index=False)
                bottom5 = df[[date_col, col]].nsmallest(5, col).to_string(index=False)
            lines.append(f"  Top 5 highest {col}:")
            lines.append(top5)
            lines.append(f"  Bottom 5 lowest {col}:")
            lines.append(bottom5)
            lines.append("")

    # Categorical top values
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns
    if len(categorical_cols) > 0:
        lines.append("Categorical Column Summary:")
        for col in categorical_cols:
            unique_count = df[col].nunique()
            top_values = df[col].value_counts().head(5).to_string()
            lines.append(f"  {col} ({unique_count} unique values):")
            lines.append(f"{top_values}")
            lines.append("")

    return "\n".join(lines)


def get_sample(df, n=10):
    """
    Returns the first n rows of the DataFrame as CSV-formatted text.

    Returns: str
    """
    return df.head(n).to_csv(index=False)