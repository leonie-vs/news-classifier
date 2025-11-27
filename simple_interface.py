from news_classifier import NewsClassifier
from ingest import IngestData 

path = 'lr_news_model.pkl'
news_clf = NewsClassifier(path)

print("Hello, welcome to the News Classifier! Enter a news headline or type 'quit' to exit.\n")

while True:

    headline = input("> Enter a headline: ")
    label = news_clf.classify_news(headline)

    category = news_clf.get_category(label)

    if headline == "quit":
        print("\nGoodbye!")
        break

    print(f"[Result] {category}\n")