import pickle

class NewsClassifier:

    def __init__(self, path):
        self.path = str(path)
        try:
            with open(self.path, 'rb') as f:
                self.model = pickle.load(f)
        except:
            print("Model can't be found, please pass valid file path")
        
        
        