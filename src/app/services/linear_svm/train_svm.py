import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics
import joblib
import structlog


def train_svm():
    df = pd.read_csv('app/data/IMDB_Dataset.csv')
    X = df['review']
    y = df['sentiment']

    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words=[])),
        ('clf', LinearSVC()),
    ])
    pipe.fit(X, y)
    joblib.dump(pipe, 'app/data/lsvc_pipeline.pkl')