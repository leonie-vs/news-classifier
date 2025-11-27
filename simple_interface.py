from news_classifier import NewsClassifier

path = 'lr_news_model.pkl'
news_clf = NewsClassifier(path)

# define function to get category for each label
def get_category(label):
    label_mapping = {1: 'World', 2: 'Sports', 3: 'Business', 4: 'Sci/Tech'}
    category = label_mapping[label]
    return category

print("Hello, welcome to the News Classifier!\n")
print("Please type in a news headline you would like to have classified. Type 'quit' to exit.\n")

while True:

    headline = input("You: ")
    label = news_clf.classify_news(headline)

    category = get_category(label)

    if headline == "quit":
        print("\nGoodbye!")
        break

    print(f"Bot: This headline is in the category: {category}-news\n")