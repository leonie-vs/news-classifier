import pandas as pd
from train_model import TrainModel
from ingest import IngestData

# Test 1 
def test_reduce_data_returns_balanced_dataframe():
    trainer = TrainModel()
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    result = trainer.reduce_data(df,n=10)
    assert result['label'].nunique() == 4
    assert result.shape() == (10,3)


