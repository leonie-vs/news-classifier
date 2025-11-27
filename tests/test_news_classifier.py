from news_classifier import NewsClassifier

# Test 1 
def test_news_classifier_path_attr_is_string():
    path = 1
    clf = NewsClassifier(path)
    assert clf.path == "1"
