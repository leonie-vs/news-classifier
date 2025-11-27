from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

class TrainModel:

    RANDOM_STATE_SEED=42
    
    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=10000)),
            ('classifier', LogisticRegression(max_iter=500, random_state=self.RANDOM_STATE_SEED))
            ])
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
    
    def reduce_data(self, df, n=12500):
        reduced_data = (
            df.groupby('label', group_keys=False)
            .sample(n=n, random_state=self.RANDOM_STATE_SEED)
            .reset_index(drop=True)
            )
        return reduced_data
    
    def split_data(self, reduced_df):
        X = reduced_df['title'] + ' ' + reduced_df['description']
        y = reduced_df['label']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=self.RANDOM_STATE_SEED,
            stratify=y
        )
        return self.X_train, self.X_test, self.y_train, self.y_test
    
    def train(self):
        if self.X_train is None or self.y_train is None:
            raise ValueError("Split data before training model")
        self.model.fit(self.X_train, self.y_train)
        return self.model
    
    def evaluate(self):
        if self.X_test is None or self.y_test is None:
            raise ValueError("Split data and train model before evaluating")
        
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        report = classification_report(self.y_test, predictions)
        
        return accuracy, report
    
    def predict(self, headline):
        return self.model.predict([headline])
    
     # save trained model
    def save_model(self):
        with open('news_model.pkl', 'wb') as f:
            pickle.dump(self.model, f)
    
    # load trained model
    def load_model(self):
        with open('news_model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model


    
