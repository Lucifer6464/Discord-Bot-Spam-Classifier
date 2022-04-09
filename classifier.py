import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle


def spam_classifier(text):
    with open('model.pkl', "rb") as f:
        model = pickle.load(f)
        predict = pd.Series(data={0: text, 1: 'blank'}, index=[0, 1], name='EmailText',
                            dtype='object')
        x_train = pd.read_csv("spam.csv")['EmailText'][0:4457]

        cv = CountVectorizer()
        cv.fit_transform(x_train)
        if model.predict(cv.transform(predict[0:1])) == ['ham']:
            is_spam = False
        else:
            is_spam = True
        f.close()
        return is_spam
