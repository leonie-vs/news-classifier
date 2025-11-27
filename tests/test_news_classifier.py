from news_classifier import NewsClassifier

# Test 1 
def test_news_classifier_path_attr_is_string():
    path = 'lr_news_model.pkl'
    clf = NewsClassifier(path)
    assert type(clf.path) == str
    assert clf.path == 'lr_news_model.pkl'

# Test 2 
def test_classify_news_method_returns_label_prediction():
    path = 'lr_news_model.pkl'
    clf = NewsClassifier(path)
    pred = clf.classify_news("Watch: Moment researcher finds rare flower after 13-year search")
    assert pred == 4


