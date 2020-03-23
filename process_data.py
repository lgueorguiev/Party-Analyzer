import pandas as pd
import json
from textacy import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


# Loads data from files into pandas dataframes
def load_data():
    with open("data/raw_dem_data.txt") as infile:
        dem_data = json.load(infile)

    with open("data/raw_rep_data.txt") as infile:
        rep_data = json.load(infile)

    dem_df = pd.DataFrame(dem_data)
    rep_df = pd.DataFrame(rep_data)
    concat_data = pd.concat([dem_df, rep_df], axis=0)

    return concat_data


# Cleans up the text of the tweets
def clean_data(data):
    tweet_text = data['text'].values

    clean_text = []

    for x in tweet_text:
        x = preprocessing.replace.replace_currency_symbols(x)
        x = preprocessing.replace.replace_phone_numbers(x)
        x = preprocessing.replace.replace_urls(x)
        x = preprocessing.remove.remove_accents(x)
        x = preprocessing.remove.remove_punctuation(x)
        x = preprocessing.replace_emails(x)
        x = preprocessing.replace.replace_emojis(x)
        x = x.lower()
        clean_text.append(x)

    return clean_text


# Assigns classifications based on whether a user is a Democrat or Republican politician
def create_targets(data):
    rep_users = ['realDonaldTrump', 'senatemajldr', 'SenTedCruz', 'LindseyGrahamSC']

    y = data['handle'].map(lambda x: 1 if x in rep_users else 0).values

    return y


# Vectorizes each tweet to be used for training
def create_features(data):
    tfv = TfidfVectorizer(ngram_range=(2,4), max_features=2000)
    x = tfv.fit_transform(data).todense()

    return x


# Splits data into training and testing with a 0.8/0.2 ratio
def split(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    return x_train, x_test, y_train, y_test


# Gets called by learner.py
def main():
    raw_data = load_data()
    cleaned_data = clean_data(raw_data)

    targets = create_targets(raw_data)
    features = create_features(cleaned_data)

    train_features, test_features, train_targets, test_targets = split(features, targets)

    return train_features, test_features, train_targets, test_targets







