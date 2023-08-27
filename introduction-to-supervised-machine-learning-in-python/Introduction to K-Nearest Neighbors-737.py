## 1. Introduction to the Dataset ##

import pandas as pd


banking_df = pd.read_csv("subscription_prediction.csv")
print(banking_df.head())
print(banking_df.dtypes.value_counts())
print(f"Shape of the dataset: {banking_df.shape}")
print(banking_df.isna().sum())
print(banking_df["y"].value_counts())
print(banking_df.describe())

## 4. Data Preparation ##

import pandas as pd
banking_df = pd.read_csv("subscription_prediction.csv")


banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)

train_df = banking_df.sample(frac=0.85, random_state=417)
test_df = banking_df.drop(train_df.index)

print(train_df["y"].value_counts(normalize=True))
print(test_df["y"].value_counts(normalize=True))

X_train = train_df.drop("y", axis=1)
y_train = train_df["y"]

X_test = test_df.drop("y", axis=1)
y_test = test_df["y"]

## 5. k-NN for One Feature ##

import pandas as pd
banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)

train_df = banking_df.sample(frac=0.85, random_state=417)
test_df = banking_df.drop(train_df.index)

X_train = train_df.drop("y", axis=1)
y_train = train_df["y"]

X_test = test_df.drop("y", axis=1)
y_test = test_df["y"]


def knn(feature, single_test_input, k):
    X_train["distance"] = abs(X_train[feature] - single_test_input[feature])
    prediction = y_train[X_train["distance"].nsmallest(n=k).index].mode()[0]
    return prediction

model_prediction = knn("age", X_test.iloc[417], 3)
print(f"Predicted label: {model_prediction}")
print(f"Actual label: {y_test.iloc[417]}")

## 6. Evaluating the Model ##

def knn(feature, single_test_input, k):
    X_train["distance"] = abs(X_train[feature] - single_test_input[feature])
    prediction = y_train[X_train["distance"].nsmallest(n=k).index].mode()[0]
    return prediction


X_test["age_predicted_y"] = X_test.apply(lambda x: knn("age", x, 3), axis=1)

model_accuracy = (X_test["age_predicted_y"] == y_test).value_counts(normalize=True)[True]*100
print(f"Accuracy of model trained on the column 'age': {model_accuracy:.2f}%")

X_test["campaign_predicted_y"] = X_test.apply(lambda x: knn("campaign", x, 3), axis=1)

model_accuracy = (X_test["campaign_predicted_y"] == y_test).value_counts(normalize=True)[True]*100
print(f"Accuracy of model trained on the column 'campaign': {model_accuracy:.2f}%")

## 7. Feature Engineering I ##

import pandas as pd
banking_df = pd.read_csv("subscription_prediction.csv")


banking_df_copy = banking_df.copy()
banking_df_copy = pd.get_dummies(data = banking_df_copy, columns = ["marital"], drop_first = True)

## 8. k-NN for Multiple Features ##

import pandas as pd
banking_df = pd.read_csv("subscription_prediction.csv")
banking_df["y"] = banking_df["y"].apply(lambda x: 1 if x=="yes" else 0)
banking_df_copy = banking_df.copy()
banking_df_copy = pd.get_dummies(data = banking_df_copy, columns = ["marital"], drop_first = True)

train_df = banking_df_copy.sample(frac=0.85, random_state=417)
test_df = banking_df_copy.drop(train_df.index)

X_train = train_df.drop("y", axis=1)
y_train = train_df["y"]

X_test = test_df.drop("y", axis=1)
y_test = test_df["y"]


def knn(features, single_test_input, k):
    squared_distance = 0
    for feature in features:
        squared_distance += (X_train[feature] - single_test_input[feature])**2
    X_train["distance"] = squared_distance**0.5
    
    prediction = y_train[X_train["distance"].nsmallest(n=k).index].mode()[0]
    return prediction

model_prediction = knn(["age", "campaign", "marital_married", "marital_single"], X_test.iloc[417], 3)
print(f"Predicted label: {model_prediction}")
print(f"Actual label: {y_test.iloc[417]}")

X_test["predicted_y"] = X_test.apply(lambda x: knn(["age", "campaign", "marital_married", "marital_single"], x, 3), axis=1)

model_accuracy = (X_test["predicted_y"] == y_test).value_counts(normalize=True)[True]*100
print(f"Accuracy of the model: {model_accuracy:.2f}%")

## 9. Feature Engineering II ##

def knn(features, test_input, k):
    distance = 0
    for feature in features:
        distance += (X_train[feature] - test_input[feature])**2
    X_train["distance"] = (distance)**0.5
    
    prediction = y_train[X_train["distance"].nsmallest(n=k).index].mode()[0]
    return prediction


features = ["age", "campaign"]

for feature in features:
    X_train[feature] = (X_train[feature] - X_train[feature].min())/(X_train[feature].max() - X_train[feature].min())
    X_test[feature] = (X_test[feature] - X_train[feature].min())/(X_train[feature].max() - X_train[feature].min())
    
X_test["predicted_y"] = X_test.apply(lambda x: knn(["age", "campaign", "marital_married", "marital_single"], x, 3), axis=1)

model_accuracy = (X_test["predicted_y"] == y_test).value_counts(normalize=True)[True]*100
print(f"Accuracy of the model: {model_accuracy:.2f}%")