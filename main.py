from ingest import IngestData
from train_lr_model import TrainModel
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
train_reduced = trainer.reduce_data(df)

# split data into test and train
trainer.split_data(train_reduced)

# train model
trainer.train()

# evaluate model
accuracy, report = trainer.evaluate()
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(report)

# predict example news headlines
# 1 - world
headline1 = "Pope Leo arrives in Turkey on first foreign trip of papacy"
prediction1 = trainer.predict(headline1)
print(f"Prediction: {prediction1[0]}")
# 2 - sports
headline2 = "McLaren had 'porpoising concern' during Las Vegas GP"
prediction2 = trainer.predict(headline2)
print(f"Prediction: {prediction2[0]}")
# 3 - business
headline3 = "I earn £20,000 and live with my son. The Budget means we will pay more tax"
prediction3 = trainer.predict(headline3)
print(f"Prediction: {prediction3[0]}")
# 4 - sci/tech
headline4 = "'Extraordinary discovery' at Orkney Neolithic site"
prediction4 = trainer.predict(headline4)
print(f"Prediction: {prediction4[0]}")

# save the model
#trainer.save_model()

