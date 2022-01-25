import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics
import joblib
<<<<<<< HEAD


def train_svm():
    df = pd.read_csv('app/data/IMDB_Dataset.csv')
    X = df['review']
    y = df['sentiment']

=======
import structlog


def train_svm(logger: structlog.stdlib.BoundLogger):
    logger.info(logger_message=f"[start] train_svm")
    df = pd.read_csv('app/data/IMDB_Dataset.csv')
    X = df['review']
    y = df['sentiment']
    logger.info(logger_message=f"data have been read")
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words=[])),
        ('clf', LinearSVC()),
    ])
    pipe.fit(X, y)
<<<<<<< HEAD
    joblib.dump(pipe, 'app/data/lsvc_pipeline.pkl')
=======
    joblib.dump(pipe, 'app/data/lsvc_pipeline.pkl')
    logger.info(logger_message=f"[end] train_svm")
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369
