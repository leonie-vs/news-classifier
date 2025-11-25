import pandas as pd
from ingest import test_data, train_data

# Test 1
def test_train_and_test_data_is_read_in_as_dataframe():
    assert type(test_data) == pd.DataFrame

