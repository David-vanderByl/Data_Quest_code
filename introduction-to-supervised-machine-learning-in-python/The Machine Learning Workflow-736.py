## 2. Data Collection and Exploration ##

import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

print(cancer_df.head())
print(f"Shape of the dataset: {cancer_df.shape}")
print(cancer_df.isna().sum())
print(cancer_df["target"].value_counts())
print(cancer_df.head())
cancer_df.describe()

## 4. Data Preparation ##

import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target


from sklearn.model_selection import train_test_split

X = cancer_df.drop(["target"], axis=1)
y = cancer_df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)

## 5. Building and Training a Classifier ##

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

X = cancer_df.drop(["target"], axis=1)
y = cancer_df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)


from sklearn.svm import LinearSVC

model = LinearSVC(penalty="l2", loss="squared_hinge", C=10, random_state=417)
model.fit(X_train, y_train)

## 6. Evaluating the Model on Test Set I ##

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

X = cancer_df.drop(["target"], axis=1)
y = cancer_df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)

model = LinearSVC(penalty="l2", loss="squared_hinge", C=10, random_state=417)
model.fit(X_train, y_train)

test_accuracy = model.score(X_test, y_test)
print(test_accuracy)

## 7. Fine-tuning the Model ##

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

X = cancer_df.drop(["target"], axis=1)
y = cancer_df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)


model = LinearSVC(penalty="l2", loss="squared_hinge", C=20, max_iter=3500, random_state=417)
model.fit(X_train, y_train)

## 8. Evaluating the Model on Test Set II ##

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

cancer_data = load_breast_cancer(as_frame = True)
cancer_df = cancer_data.data
cancer_df['target'] = cancer_data.target

X = cancer_df.drop(["target"], axis=1)
y = cancer_df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)

model = LinearSVC(penalty="l2", loss="squared_hinge", C=20, max_iter=3500, random_state=417)
model.fit(X_train, y_train)

test_accuracy = model.score(X_test, y_test)
print(test_accuracy)