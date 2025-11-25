# news-classifier
Training a machine learning model on news classification data to generate insights - ingesting and storing the data using a local script forming the basis for an AWS Lambda with RDS - creating a chatbot interface that uses the model - adding RAG functionality

Dataset: https://huggingface.co/datasets/sh0416/ag_news
The AG's news topic classification dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the dataset above. It is used as a text classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).

Labels: 
1 - World
2 - Sports
3 - Business
4 - Sci/Tech

