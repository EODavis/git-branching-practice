import pandas as pd


def check_nulls(df: pd.DataFrame) -> dict:
    """Return null counts and percentages per column."""
    if len(df) == 0:
        return {'null_counts': {}, 'null_pcts': {}}
    null_counts = df.isnull().sum()
    null_pcts = (null_counts / len(df) * 100).round(2)
    return {
        'null_counts': null_counts.to_dict(),
        'null_pcts': null_pcts.to_dict()
    }


def check_duplicates(df: pd.DataFrame) -> int:
    """Return number of duplicate rows."""
    return int(df.duplicated().sum())


def check_dtypes(df: pd.DataFrame) -> dict:
    """Return dtype of each column."""
    return df.dtypes.astype(str).to_dict()


def full_report(df: pd.DataFrame) -> None:
    """Print a full data quality report."""
    print(f"Shape: {df.shape}")
    print(f"\nDuplicate rows: {check_duplicates(df)}")
    print(f"\nNull summary:")
    nulls = check_nulls(df)
    for col, pct in nulls['null_pcts'].items():
        if pct > 0:
            print(f"  {col}: {pct}% null")
    print(f"\nDtypes:")
    for col, dtype in check_dtypes(df).items():
        print(f"  {col}: {dtype}")
