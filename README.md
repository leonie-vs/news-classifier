# news-classifier
Training a machine learning model on news classification data to generate insights - ingesting and storing the data using a local script forming the basis for an AWS Lambda with RDS - creating a chatbot interface that uses the model - adding RAG functionality

Dataset: https://huggingface.co/datasets/sh0416/ag_news
The AG's news topic classification dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the dataset above. It is used as a text classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).

Labels: 
1 - World
2 - Sports
3 - Business
4 - Sci/Tech


1. Set up the project
- Fork and clone the repository. 
- Create a venv at the root of the directory via the command **python3 -m venv venv**.
- Run **pip install -r requirements.txt** to install the dependencies.
- Run the command **export PYTHONPATH=$(pwd)**.
- Run the unit tests in **test_ingest.py** and **test_train_model.py** using the command **pytest ./tests/<test_file>.py** to ensure all tests pass. These scripts make use of a test dataset stored in **./tests/test_data.json**. 


2. Data Ingestion
- In **main.py**, import the IngestData class to preprocess the data.
- Create an instance of IngestData (defined in **ingest.py**). To do this, you need to pass in a string of the raw data file path, and a string of the file path pointing to where the data should be saved after preprocessing.
    - E.g. **ingest = IngestData('input_file_path', 'output_file_path')**.

- To load, clean, and save the data, use the **preprocess_pipeline()** method.
- This method uses..
    - .. the **load_data()** method, which reads in the input data as a pandas dataframe.
    - .. the **remove_special_characters(df)** method, which standardises the strings in the columns 'title' and 'description' by removing extra spaces and any special characters that aren't a-z, A-Z, or basic punctuation (.,!?\':"-).
    - .. the **save_data(df)** method, which saves the dataframe to a jsonl file which was defined as output_path when instantiating IngestData. 


3. Train the Model
- To train the model on the preprocessed data, import the TrainModel class from **train_model.py** in **main.py**. 

- Then, use the **reduce_rows(df, n=50,000)** method to get a balanced sample (equal amount of objects for each label) of the cleaned data, where **df** should be the cleaned dataset from the previous step, and **n** is the overall number of rows you want, defaulting to 50,000. 

- For this project, I suggest using the default sample size of n=50,000, which will reduce the data to 12,5000 rows per label. To ensure consistent random sampling, set a variable RANDOM_STATE_SEED to 42 before reducing the data. 



