import pandas as pd
import joblib
from sklearn import metrics


def metrics_svm():
    df_cornell = pd.read_csv('app/data/cornell_movie_reviews.csv')
    loaded_model = joblib.load('app/data/lsvc_pipeline.pkl')
    df_cornell['predicted_sentiment'] = df_cornell['review'].apply(
        lambda x: loaded_model.predict([x])[0])

    response = {
        "accuracy":
        metrics.accuracy_score(df_cornell['sentiment'],
                               df_cornell['predicted_sentiment']),
        "precision":
        metrics.precision_score(df_cornell['sentiment'],
                                df_cornell['predicted_sentiment'],
                                pos_label="positive"),
        "recall":
        metrics.recall_score(df_cornell['sentiment'],
                             df_cornell['predicted_sentiment'],
                             pos_label="positive"),
        "f1":
        metrics.f1_score(df_cornell['sentiment'],
                         df_cornell['predicted_sentiment'],
                         pos_label="positive")
    }

    return response
