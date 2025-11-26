import pandas as pd
import re

# load data
test_data = pd.read_json(path_or_buf="data/test.jsonl", lines=True)
train_data = pd.read_json(path_or_buf="data/train.jsonl", lines=True)

# clean data
# remove any characters that aren't a-z or basic punctuation 
def remove_special_characters(df):
    
    data = df.copy()
    
    data['title'] = data['title'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)
    data['description'] = data['description'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)

    data['title'] = data['title'].str.replace(r'\s+', ' ', regex=True).str.strip()
    data['description'] = data['description'].str.replace(r'\s+', ' ', regex=True).str.strip()
    
    return data

# call cleaning function 
test_cleaned = remove_special_characters(test_data)
train_cleaned = remove_special_characters(train_data)

# write cleaned data to new jsonl files
test_cleaned.to_json('data/test_cleaned.jsonl', orient='records', lines=True)
train_cleaned.to_json('data/train_cleaned.jsonl', orient='records', lines=True)