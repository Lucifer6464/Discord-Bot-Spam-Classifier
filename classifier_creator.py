import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import pickle

dataframe = pd.read_csv("spam.csv")

# split the data
x = dataframe["EmailText"]
y = dataframe["Label"]
x_train, y_train = x[0:4457], y[0:4457]
x_test, y_test = x[4457:], y[4457:]

# extract the features
cv = CountVectorizer()
features = cv.fit_transform(x_train)

# create the model
tuned_parameters = {'kernel': ['rbf', 'linear'], 'gamma': [1e-3, 1e-4],
                    'C': [1, 10, 100, 1000]}
model = GridSearchCV(svm.SVC(), tuned_parameters)
model.fit(features, y_train)

# accuracy
print(model.score(cv.transform(x_test), y_test))
print(model.predict(cv.transform(x_test[0:1])))

# save the model using pickle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
    f.close()
