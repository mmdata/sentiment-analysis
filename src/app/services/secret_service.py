import os


def load_prometheus_secrets():
    return (os.environ['PROMETHEUS_USERNAME'],
            os.environ['PROMETHEUS_PASSWORD'])


def load_training_secrets():
    return (os.environ['TRAINING_USER'], os.environ['TRAINING_PASSWORD'])
