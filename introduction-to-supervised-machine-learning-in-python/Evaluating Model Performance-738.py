## 1. Introduction ##

import pandas as pd


banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)

## 2. Validation Set ##

import pandas as pd

banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)


from sklearn.model_selection import train_test_split

X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state = 417)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20*X.shape[0]/X_train.shape[0], random_state = 417)

## 3. Building and Training a k-NN ##

import pandas as pd
from sklearn.model_selection import train_test_split

banking_df = pd.read_csv("subscription_prediction.csv")
X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state = 417)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20*X.shape[0]/X_train.shape[0], random_state = 417)


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, y_train)

## 4. Feature Engineering ##

from sklearn.preprocessing import MinMaxScaler

X_train = pd.get_dummies(data = X_train, columns = ["marital", "default"], drop_first = True)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train[["marital_married", "marital_single", "marital_unknown", "default_unknown", "age", "duration"]])

## 5. Evaluating the Model on Validation Set ##

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

banking_df = pd.read_csv("subscription_prediction.csv")
X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state = 417)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20*X.shape[0]/X_train.shape[0], random_state = 417)

X_train = pd.get_dummies(data = X_train, columns = ["marital", "default"], drop_first = True)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train[["marital_married", "marital_single", "marital_unknown", "default_unknown", "age", "duration"]])


knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train_scaled, y_train)

X_val = pd.get_dummies(data = X_val, columns = ["marital", "default"], drop_first = True)

X_val_scaled = scaler.transform(X_val[["marital_married", "marital_single", "marital_unknown", "default_unknown", "age", "duration"]])

val_accuracy = knn.score(X_val_scaled, y_val)
print(f"Accuracy of model evaluated on validation set with K = 1: {val_accuracy*100:.2f}%")

knn = KNeighborsClassifier(n_neighbors = 2000)
knn.fit(X_train_scaled, y_train)

val_accuracy = knn.score(X_val_scaled, y_val)
print(f"Accuracy of model evaluated on validation set with K = 2000: {val_accuracy*100:.2f}%")

## 7. Evaluating the Model on Test Set ##

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

banking_df = pd.read_csv("subscription_prediction.csv")
X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state = 417)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20*X.shape[0]/X_train.shape[0], random_state = 417)

X_train = pd.get_dummies(data = X_train, columns = ["marital", "default"], drop_first = True)
X_val = pd.get_dummies(data = X_val, columns = ["marital", "default"], drop_first = True)

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train[["marital_married", "marital_single", "marital_unknown", "default_unknown", "age", "duration"]])

X_val_scaled = scaler.transform(X_val[["marital_married", "marital_single", "marital_unknown", "default_unknown", "age", "duration"]])
print(0, 1, sep="\n")


knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train_scaled, y_train)

val_accuracy = knn.score(X_val_scaled, y_val)
print(f"Accuracy of model evaluated on validation set with K = 5: {val_accuracy*100:.2f}%")

X_test = pd.get_dummies(data = X_test, columns = ["marital", "default"], drop_first = True)

X_test_scaled = scaler.transform(X_test[["marital_married", "marital_single", "marital_unknown", "default_unknown", "age", "duration"]])

test_accuracy = knn.score(X_test_scaled, y_test)
print(f"Accuracy of model evaluated on test set with K = 5: {test_accuracy*100:.2f}%")