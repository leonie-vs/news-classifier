import pandas as pd
from ingest import test_data, train_data

# Test 1
def test_train_and_test_data_is_read_in_as_dataframe():
    assert type(test_data) == pd.DataFrame
    assert type(train_data) == pd.DataFrame

# Test 2
def test_each_row_in_data_has_valid_label():
    valid_labels = {1, 2, 3, 4}
    assert test_data["label"].isin(valid_labels).all
    assert train_data["label"].isin(valid_labels).all

# Test 3
def test_data_has_no_missing_values():
    assert not test_data.isnull().any().any()
    assert not train_data.isnull().any().any()


