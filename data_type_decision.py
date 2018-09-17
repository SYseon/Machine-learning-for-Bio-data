# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:10:55 2018

@author: 선승엽
"""

import numpy as np


class DataTypeDecision:
    
    def __init__(self, data):
        if not hasattr(data,'__array__'):
            raise ValueError('Data must has a attribute __array__')
        self.data=data

        
    def classification(self): #데이터 타입을 배열로 반환
        temp=list()
    
        for i in range(self.data.shape[1]):
            #string data
            if np.any(self.data.T[i]==self.data.T[i].astype(str)):
                temp.append(2)
    
            #categorical data    
            elif len(np.unique(self.data.T[i].astype(float))) < 7:
                temp.append(0)
                
            #continuous data
            elif np.any(self.data.T[i].astype(int)!=self.data.T):
                temp.append(1)

            
          
        result=np.array(temp)
        
        return result

