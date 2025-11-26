import pandas as pd
from ingest import test_data, train_data, standardise_to_lower, remove_special_characters

# Test 1
def test_train_and_test_data_is_read_in_as_dataframe():
    assert type(test_data) == pd.DataFrame
    assert type(train_data) == pd.DataFrame

# Test 2
def test_each_row_in_data_has_valid_label():
    valid_labels = {1, 2, 3, 4}
    assert test_data["label"].isin(valid_labels).all()
    assert train_data["label"].isin(valid_labels).all()

# Test 3
def test_data_has_no_missing_values():
    assert not test_data.isnull().any().any()
    assert not train_data.isnull().any().any()

# Test 4
def test_remove_special_characters_cleans_text():
    data = {
        'label': [1, 2],
        'title': ['Hello! @World#', 'Test$%^Title'],
        'description': ['Breaking news: £100 prize!', 'Update™ on COVID-19']
    }
    test_df = pd.DataFrame(data)
    cleaned_df = remove_special_characters(test_df)
    assert cleaned_df['title'].tolist() == ['Hello! World', 'TestTitle']
    assert cleaned_df['description'].tolist() == ['Breaking news: 100 prize!', 'Update on COVID-19']
    assert cleaned_df['label'].tolist() == [1, 2]

