import pandas as pd

# define file path 
path_data = "data/train.jsonl"

# load data
data_df = pd.read_json(path_or_buf=path_data, lines=True)

# clean data function
def remove_special_characters(df):
    
    data = df.copy()
    # remove any characters that aren't a-z or basic punctuation 
    data['title'] = data['title'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)
    data['description'] = data['description'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)

    data['title'] = data['title'].str.replace(r'\s+', ' ', regex=True).str.strip()
    data['description'] = data['description'].str.replace(r'\s+', ' ', regex=True).str.strip()
    
    return data

# preprocess and save data
if __name__ == "__main__":
    data_cleaned = remove_special_characters(data_df) # call cleaning function
    data_cleaned.to_json('data/data_cleaned.jsonl', orient='records', lines=True) # write cleaned data to new jsonl file
    print("Data cleaned and saved")

