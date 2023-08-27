## 1. Introduction ##

import pandas as pd


banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)

banking_df = pd.get_dummies(data = banking_df, drop_first = True)

## 2. Feature Selection ##

import pandas as pd

banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)
banking_df = pd.get_dummies(data = banking_df, drop_first = True)


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

correlations = abs(banking_df.corr())

# Identify top 5 features, excluding y itself, that correlate strongly with y.
top_5_features = correlations["y"].sort_values(ascending=False)[1:6].index

print(correlations["y"].sort_values(ascending=False)[1:6])

X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_val, y_train, y_val = train_test_split(X[top_5_features], y, test_size=0.20, random_state = 417)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20*X.shape[0]/X_train.shape[0], random_state = 417)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

## 3. Training and Evaluating the Model ##

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)
banking_df = pd.get_dummies(data = banking_df, drop_first = True)

correlations = abs(banking_df.corr())
top_5_features = correlations["y"].sort_values(ascending=False)[1:6].index

X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_val, y_train, y_val = train_test_split(X[top_5_features], y, test_size=0.20, random_state = 417)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20*X.shape[0]/X_train.shape[0], random_state = 417)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)


from sklearn.neighbors import KNeighborsClassifier

num_neighbors = [num for num in range(1, 6)]
X_val_scaled = scaler.transform(X_val)

accuracies = {}

for neighbors in num_neighbors:
    knn = KNeighborsClassifier(n_neighbors = neighbors)
    knn.fit(X_train_scaled, y_train)
    val_accuracy = knn.score(X_val_scaled, y_val)
    accuracies[neighbors] = val_accuracy

print(accuracies)

## 4. Hyperparameter Optimization ##

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)
banking_df = pd.get_dummies(data = banking_df, drop_first = True)

correlations = abs(banking_df.corr())
top_5_features = correlations["y"].sort_values(ascending=False)[1:6].index

X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_val, y_train, y_val = train_test_split(X[top_5_features], y, test_size=0.20, random_state = 417)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20*X.shape[0]/X_train.shape[0], random_state = 417)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)


from sklearn.neighbors import KNeighborsClassifier

num_neighbors = [num for num in range(1, 6)]
X_val_scaled = scaler.transform(X_val)

accuracies = {}

for neighbors in num_neighbors:
    knn = KNeighborsClassifier(n_neighbors = neighbors, weights = "distance", p = 5)
    knn.fit(X_train_scaled, y_train)
    val_accuracy = knn.score(X_val_scaled, y_val)
    accuracies[neighbors] = val_accuracy
    
print(accuracies)

## 6. Grid Search ##

import pandas as pd

banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)
banking_df = pd.get_dummies(data = banking_df, drop_first = True)

correlations = abs(banking_df.corr())

top_5_features = correlations["y"].sort_values(ascending=False)[1:6].index

X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]


from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(X[top_5_features], y, test_size=0.20, random_state = 417)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

grid_params = {"n_neighbors": range(1, 10),
                "metric": ["minkowski", "manhattan"]
              }

knn = KNeighborsClassifier()
knn_grid = GridSearchCV(knn, grid_params, scoring='accuracy')
knn_grid.fit(X_train_scaled, y_train)

best_score = knn_grid.best_score_
best_params = knn_grid.best_params_

print(f"Best model's accuracy: {best_score*100:.2f}")
print(f"Best model's parameters: {best_params}")

## 7. Evaluating the Model on Test Set ##

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)
banking_df = pd.get_dummies(data = banking_df, drop_first = True)

correlations = abs(banking_df.corr())

top_5_features = correlations["y"].sort_values(ascending=False)[1:6].index

X = banking_df.drop(["y"], axis=1)
y = banking_df["y"]

X_train, X_test, y_train, y_test = train_test_split(X[top_5_features], y, test_size=0.20, random_state = 417)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

grid_params = {"n_neighbors": range(1, 10),
                "metric": ["minkowski", "manhattan"]
              }

knn = KNeighborsClassifier()
knn_grid = GridSearchCV(knn, grid_params, scoring='accuracy')
knn_grid.fit(X_train_scaled, y_train)


X_test_scaled = scaler.transform(X_test)
accuracy = knn_grid.best_estimator_.score(X_test_scaled, y_test)
print(f" Model Accuracy on test set: {accuracy*100:.2f}")