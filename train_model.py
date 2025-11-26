import pandas as pd

class TrainModel:
    
    RANDOM_STATE_SEED=42

    def reduce_data(self, df, n=12500):
        sampled_groups = []
        for label in df['label'].unique():
            group = df[df['label'] == label]
            sampled = group.sample(n=n, random_state=self.RANDOM_STATE_SEED)
            sampled_groups.append(sampled)
        reduced_data = pd.concat(sampled_groups, ignore_index=True)
        return reduced_data
