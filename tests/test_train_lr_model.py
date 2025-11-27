import pandas as pd
from train_lr_model import TrainModel

# Test 1 
def test_reduce_data_returns_balanced_dataframe():
    trainer = TrainModel()
    df = pd.read_json(path_or_buf='./tests/test_data.jsonl', lines=True)
    result = trainer.reduce_data(df, n=2)
    assert result['label'].nunique() == 4
    assert result.shape == (8,3)
    assert (result['label'].value_counts() == 2).all()



