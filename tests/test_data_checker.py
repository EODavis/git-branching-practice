import pandas as pd
import pytest
from src.data_checker import check_nulls, check_duplicates, check_dtypes


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'name':  ['Alice', 'Bob', None, 'Alice'],
        'score': [90, 85, 78, 90],
        'grade': ['A', 'B', 'C', 'A']
    })


def test_check_nulls(sample_df):
    result = check_nulls(sample_df)
    assert result['null_counts']['name'] == 1
    assert result['null_pcts']['score'] == 0.0


def test_check_duplicates(sample_df):
    assert check_duplicates(sample_df) == 1


def test_check_dtypes(sample_df):
    result = check_dtypes(sample_df)
    assert 'name' in result
    assert result['score'] == 'int64'


def test_full_report_runs(sample_df, capsys):
    from src.data_checker import full_report
    full_report(sample_df)
    captured = capsys.readouterr()
    assert 'Shape' in captured.out
