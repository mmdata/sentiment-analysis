import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics
from app.models.pydantic_models import TrainParametersSchema
import joblib

import structlog


def train_svm(logger: structlog.stdlib.BoundLogger, train_parameters) :

    logger.info(logger_message=f"[start] train_svm")
    df = pd.read_csv('app/data/IMDB_Dataset.csv')
    X = df['review']
    y = df['sentiment']

    ## These path might be invalid
    with open('/usr/src/app/app/data/test2.txt', 'w') as file:
        file.write('before training 2')
    logger.info(logger_message=f"data have been read")
    with open('app/data/test.txt', 'w') as file:
        file.write('before training')


    

    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words=[])),
        ('clf', LinearSVC(random_state = train_parameters.random_state,
                          max_iter = train_parameters.max_iter,
                          penalty = train_parameters.penalty)),
    ])
    pipe.fit(X, y)


    joblib.dump(pipe, 'app/data/lsvc_pipeline.pkl')
    logger.info(logger_message=f"[end] train_svm")
