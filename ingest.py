import pandas as pd

class IngestData:
    
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    # load data
    def load_data(self):
        df = pd.read_json(path_or_buf=self.input_path, lines=True)
        return df

    # clean data 
    def remove_special_characters(self, df):
        data = df.copy()
        # remove any characters that aren't a-z, A-Z, or basic punctuation 
        data['title'] = data['title'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)
        data['description'] = data['description'].str.replace(r'[^a-zA-Z0-9\s.,!?\':"-]', '', regex=True)

        data['title'] = data['title'].str.replace(r'\s+', ' ', regex=True).str.strip()
        data['description'] = data['description'].str.replace(r'\s+', ' ', regex=True).str.strip()

        return data
    
    # save data
    def save_data(self, df):
        df.to_json(self.output_path, orient='records', lines=True) # write data to jsonl file

    # load, preprocess, and save data in one method
    def preprocess_pipeline(self):
        df = self.load_data() # load raw data
        data_cleaned = self.remove_special_characters(df) # call cleaning function
        self.save_data(data_cleaned) # save cleaned data in output file
        print("Data cleaned and saved")
        return data_cleaned
    
   



