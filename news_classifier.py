import pickle

class NewsClassifier:

    def __init__(self, path):
        self.path = str(path)
        try:
            with open(self.path, 'rb') as f:
                self.model = pickle.load(f)
        except Exception:
            raise Exception("Model can't be found")
    
    def classify_news(self, headline):
        pred = self.model.predict([headline])
        return pred[0]

        
        
        