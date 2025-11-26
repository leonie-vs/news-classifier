from ingest import IngestData
from train_model import TrainModel
import pandas as pd

# define file path 
input_path = "./data/train.jsonl"
output_path = "./data/data_cleaned.jsonl"

# load and process data
ingest = IngestData(input_path, output_path)
df = ingest.preprocess_pipeline()

# build and train logistic regression model
trainer = TrainModel()

# reduce data to 50,000 rows
train_reduced = trainer.reduce_data(df, n=12500)

# split data into test and train
trainer.split_data(train_reduced)

# train model
trainer.train()

# evaluate model
accuracy, report = trainer.evaluate()
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(report)

# predict example news headline
headline = "Labour will not leave 'broken' welfare system unchanged, chancellor says"
prediction = trainer.predict(headline)
print(f"Predicted label: {prediction[0]}")

# save the model
trainer.save_model()

