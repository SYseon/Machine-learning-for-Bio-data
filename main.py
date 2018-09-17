# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:17:44 2018

@author: 선승엽
"""

import preprocess
import data_type_decision
import pandas as pd
import numpy as np
import classifier 
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename



def getvaluefunc(index):
    n=input("값을 입력하세요.")
    n=int(n)
    
    while(not n in index):
        n=input("잘못된 값입니다. 다시 입력해주세요.")
        n=int(n)
    
    return n

def sel_categoricalmethod(file):
    """
    Categorical Data를 자동으로 구할 지 사용자가 결정
    """
    print("Data Type을 자동으로 구하시겠습니까? 1: Yes/2: No")
    file=np.array(file)
    sel_method=getvaluefunc((1,2))
    
    if sel_method == 1:
        data_type=DataTypeDecision.DataTypeDecision(file) #DataType을 구함
        data_type_array=data_type.classification()

    elif sel_method ==2:
        temp=list()
        index=(0, 1)
        for i in range(file.shape[1]):
            print(i,'번째 데이터가 Categorical Data면 0을 아니면 1을 입력해 주세요.' )
            temp.append(getvaluefunc(index))
            data_type_array=np.array((temp))
        
    print('data_type_array',data_type_array)
    
    return data_type_array


def preprocess(f, type_arr):
    """
    Numeric Data의 Preprocessing 방법을 사용자가 결정
    """
    print("Numeric data의 preprocesss 방법을 선택하세요. (1: standard normalization 2:min max 3: z score)")
    n=getvaluefunc((1,2,3))

    if n == 1:
        result = Preprocess.standard_normalization(f, type_arr)
    
    elif n == 2:
        result = Preprocess.min_max(f, type_arr)

    elif n == 3:
        result = Preprocess.z_score(f, type_arr)
    
    
    return result

def sel_model(train_data, test_data):
    
    print("모델을 선택하세요. (1:KNN 2:SVM 3:Navie Bayes 4:Decision Tree)")
    n=getvaluefunc((1,2,3,4))
    
    if n==1:
        temp=input("KNN이 선택되었습니다. Parameter N 값을 입력하세요.")
        temp=int(temp)
        
        return Classifier.knn(train_data, test_data, temp)
        
    elif n==2:
        print("SVM이 선택되었습니다.")
        
        return Classifier.svm(train_data, test_data)
    
    elif n==3:
        print("Naive Bayes가 선택되었습니다.")
        
        return Classifier.nb(train_data, test_data)

    elif n==4:
        max_depth=input("max depth 를 입력하세요.")
        max_depth=int(max_depth)
        random_state=input("random state 를 입력하세요.")
        random_state=int(random_state)
        
        return Classifier.dt(train_data, test_data, max_depth, random_state)

def openfile():
    root=tkinter.Tk()
    root.filename = askopenfilename(title= "Choose yourdata file")
    
    return root.filename
    

        
    
print("Train 파일을 선택하세요.")
f_train=pd.read_excel(openfile()) #Excel 파일 열음
f_train=f_train.dropna(axis=1)#nan값 column 제거
data_type_array=sel_categoricalmethod(f_train) #data_type을 np.array로 반환
f_train=np.array(f_train.T)
f_train=preprocess(f_train, data_type_array)

print("Test 파일을 선택하세요.")
f_test=pd.read_excel(openfile()) #Excel 파일 열음
f_test=f_test.dropna(axis=1) #nan값 column 제거
data_type_array=sel_categoricalmethod(f_test) #data_type을 np.array로 반환
f_test=np.array(f_test.T)
f_test=preprocess(f_test, data_type_array)
result=sel_model(f_train, f_test)

print("accuracy score", result[1])
print("std",, result[2])
print("confusion matrix", result[3])
print("f1_score", result[4])
arr_data=pd.DataFrame(result[0])
print("결과를 저장할 주소를 입력하세요.")
savefile = asksaveasfilename(filetypes=(("Excel files", "*.xlsx"),("All files", "*.*") ))
arr_data.to_excel(savefile + ".xlsx", index=False, sheet_name="Results")



#C:\Users\선승엽\Documents\카카오톡 받은 파일\Arcene\Data Folder\ARCENE\arcene.test.xlsx