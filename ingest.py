import pandas as pd
import re

# load data
test_data = pd.read_json(path_or_buf="data/test.jsonl", lines=True)
train_data = pd.read_json(path_or_buf="data/train.jsonl", lines=True)

# clean data
# convert everything to lowercase in title and description
def standardise_to_lower(df):
    data = df.copy()
    data['title'] = data['title'].str.lower()
    data['description'] = data['description'].str.lower()
    return data
# remove any characters that aren't a-z or basic punctuation 
def remove_special_characters(df):
    data = df.copy()
    data['title'] = data['title'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)
    data['description'] = data['description'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)
    data['title'] = data['title'].str.replace(r'\s+', ' ', regex=True).str.strip()
    data['description'] = data['description'].str.replace(r'\s+', ' ', regex=True).str.strip()
    return data