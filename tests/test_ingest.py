import pandas as pd
from ingest import IngestData

# Test 1
def test_load_data_returns_jsonl_as_dataframe():
    ingest = IngestData('./tests/test_data.jsonl', './tests/test_clean_data.jsonl')
    result = ingest.load_data()
    assert type(result) == pd.DataFrame
    assert result.shape == (20,3)

# # Test 2
def test_remove_special_characters_cleans_titles_and_descriptions():
    ingest = IngestData('./tests/test_data.jsonl', './tests/test_clean_data.jsonl')
    cleaned = ingest.load_data()
    result = ingest.remove_special_characters(cleaned)
    assert result.loc[0,'title'] == 'Hello! World'
    assert result.loc[1,'title'] == 'TestTitle'
    assert result.loc[0,'description'] == 'Breaking news: 100 prize!'
    assert result.loc[1,'description'] == 'Update on COVID-19'
    assert result['label'].nunique() == 4





