#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:44:08 2018

@author: caucse
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

import numpy as np


def find_xy(data):
    n=3
    
    while(not n in (0,1)):
        n=input("마지막 column을 y값으로 지정합니끼? 거부 할 시 y column을 직접 지정합니다. (0: No, 1: Yes)")
        n=int(n)
    
    if n==1:
        x=data.T[:data.shape[1]-2]
        y=data.T[data.shape[1]-1]
        y=np.rint(y)
        
        return x.T, y.T
    
    else:
        n=input("y값의 column을 입력하세요.")
        n=int(n)
        x_left=data.T[:n-2]
        y=data.T[n-1]
        x_right=data.T[n:data.shape[1]-1]
        x=np.concatenate((x_left,x_right))
        
        return x.T, y.T

def knn(train_data, test_data, n):
    print("\n\n\n\n### ABOUT TRAIN DATA ###")
    train_x, train_y=find_xy(train_data)
    print("\n\n\n\n### ABOUT TEST DATA ###")
    test_x, test_y=find_xy(test_data)
    _knn=KNeighborsClassifier(n_neighbors=n,p=2, metric='minkowski')
    _knn.fit(train_x,train_y)
    result_y=_knn.predict(test_x)
    accuracy=accuracy_score(test_y, result_y)
    
    return result_y, accuracy, result_y.std(), confusion_matrix(test_y, result_y), f1_score(test_y, result_y)


def svm(train_data, test_data):
    print("\n\n\n\n### ABOUT TRAIN DATA ###")
    train_x, train_y=find_xy(train_data)
    print("\n\n\n\n### ABOUT TEST DATA ###")
    test_x, test_y=find_xy(test_data)
    _svm=SVC()
    _svm.fit(train_x,train_y)
    result_y=_svm.predict(test_x)
    accuracy=accuracy_score(test_y, result_y)
    
    return result_y, accuracy, result_y.std(), confusion_matrix(test_y, result_y), f1_score(test_y, result_y)
    


def nb(train_data, test_data):
    print("\n\n\n\n### ABOUT TRAIN DATA ###")
    train_x, train_y=find_xy(train_data)
    print("\n\n\n\n### ABOUT TEST DATA ###")
    test_x, test_y=find_xy(test_data)
    _nb= GaussianNB()
    _nb.fit(train_x, train_y)
    result_y=_nb.predict(test_x)
    accuracy=accuracy_score(test_y, result_y)
    
    return result_y, accuracy, result_y.std(), confusion_matrix(test_y, result_y), f1_score(test_y, result_y)
    
    
def dt(train_data, test_data, n1, n2):
    print("\n\n\n\n### ABOUT TRAIN DATA ###")
    train_x, train_y=find_xy(train_data)
    print("\n\n\n\n### ABOUT TEST DATA ###")
    test_x, test_y=find_xy(test_data)
    _dt=DecisionTreeClassifier(criterion='entropy', max_depth=n1, random_state=n2)
    _dt.fit(train_x,train_y)
    result_y=_dt.predict(test_x)
    accuracy=accuracy_score(test_y, result_y)
    
    return result_y, accuracy, result_y.std(), confusion_matrix(test_y, result_y), f1_score(test_y, result_y)