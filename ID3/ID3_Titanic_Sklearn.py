import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

'''
    Author: Levi Schanding
    Description:
'''
# Goal attribute: Survived
# [Global Vars]
orig_train_set = pd.read_csv(".\\dataset\\Titanic_training.csv")  # used to train the decision tree
orig_test_set = pd.read_csv(".\\dataset\\Titanic_test.csv")  # used to test the decision tree
# Processing dataset
train_set = orig_train_set.drop('Name', axis=1)
test_set = orig_test_set.drop('Name', axis=1)
train_set = train_set.drop('Ticket', axis=1)
test_set = test_set.drop('Ticket', axis=1)
train_set = train_set.drop('Cabin', axis=1)
test_set = test_set.drop('Cabin', axis=1)
train_set['Sex'].replace('male', 0, True)
train_set['Sex'].replace('female', 1, True)
train_set['Embarked'].replace('S', 1, True)
train_set['Embarked'].replace('C', 2, True)
train_set['Embarked'].replace('Q', 3, True)
train_set['Embarked'] = train_set['Embarked'].fillna(0)
train_set['Age'] = train_set['Age'].fillna(0)




X = train_set.drop('Survived', axis=1)
y = train_set['Survived']


X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.30)
tree_classifier = DecisionTreeClassifier()


def default_train():
    tree_classifier.fit(X_train, Y_train)


def show_tree():
    print(tree.export_text(tree_classifier))


def predict():
    y_pred = tree_classifier.predict(X_test)
    print(confusion_matrix(Y_test, y_pred))
    print(classification_report(Y_test, y_pred))


def main():
    print("[Program Start]")
    default_train()
    show_tree()
    predict()
    print("[Program End]")


main()
