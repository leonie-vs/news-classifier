import pandas as pd

class TrainModel:
    
    RANDOM_STATE_SEED=42

    def reduce_data(self, df, n=12500):
        reduced_data = (
            df.groupby('label', group_keys=False)
            .sample(n=n, random_state=self.RANDOM_STATE_SEED)
            .reset_index(drop=True)
            )
        return reduced_data
