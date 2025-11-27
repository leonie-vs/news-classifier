from news_classifier import NewsClassifier
import re

def simple_interface(path):
    
    news_clf = NewsClassifier(path)
    
    print("Hello, welcome to the News Classifier! Enter a news headline or type 'quit' to exit.\n")

    while True:

        headline = input("> Enter a headline: ")

        no_special_chars = re.sub(r'[^a-zA-Z0-9\s.,!?\':"-]', '', headline)
        cleaned = " ".join(no_special_chars.split())
        print(cleaned)

        label = news_clf.classify_news(cleaned)

        category = news_clf.get_category(label)

        if headline == "quit":
            print("\nGoodbye!")
            break

        print(f"[Result] {category}\n")

