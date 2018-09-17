# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 03:26:59 2018

@author: 선승엽
"""
import numpy as np


def standard_normalization(data, data_type_array):
    result=np.zeros(data.shape).astype(float)
    
    for i in range(len(data_type_array)):
        
        if data_type_array[i]==1:
            distance=np.linalg.norm(data[i])
            result[i]=data[i].__truediv__(distance)
           
        elif data_type_array[i]==0:   
            result[i] = label_encoder(data[i])
        
        elif data_type_array[i]==2:
            result[i] = str_arr(data[i])
            
            
    return result.T


    
def min_max(data, data_type_array):
    result=np.zeros(data.shape).astype(float)
    
    for i in range(len(data_type_array)):

        if data_type_array[i]==1:
            max_=data[i].max()
            min_=data[i].min()
            max_-=min_
            data[i]=data[i]-min_
            result[i]=data[i].__truediv__(max_)
        
        elif data_type_array[i]==0:
            result[i] = label_encoder(data[i])
        
        elif data_type_array[i]==2:
            result[i] = str_arr(data[i])
          

    return result.T


def z_score(data, data_type_array):
    result=np.zeros(data.shape).astype(float)
    
    for i in range(len(data_type_array)):
        if data_type_array[i]==1:
            mean_val=data[i].mean()
            std_val=data[i].std()
            data[i]=data[i]-mean_val
            result[i]=data[i].__truediv__(std_val)
        
        elif data_type_array[i]==0:
            result[i] = label_encoder(data[i])
        
        elif data_type_array[i]==2:
            result[i] = str_arr(data[i])
           
            
    return data.T


def label_encoder(data):
    
    for i in range(len(data)):
        for j in range(len(np.unique(data))):
            if data[i-1]==np.unique(data)[j-1]:
                data[i-1]=j
    
    return data


def str_arr(data):
    result=np.zeros(data.shape).astype(int)
    temp=data.tolist()
    temp_list=list()
    
    [temp_list.append(temp[i]) for i in range(len(temp)) if not temp[i] in temp_list]
    
    for i in range(len(data)):
        for j in range(len(temp_list)):
            if data[i]==temp_list[j]:
                result[i]=j
            
    
    return result
        
    



