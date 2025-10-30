import pandas as pd, numpy as np
import os


df = pd.DataFrame({'Name':['Santosh','Deepak','Bonty','Sunil','Tesla','Mrx'],'Age':[np.random.randint(20,25),np.random.randint(20,25),np.random.randint(20,25),np.random.randint(20,25),np.random.randint(20,25),np.random.randint(20,25)]})

path='/home/santosh/Desktop/MLOps/DVC/Data'
os.makedirs(path,exist_ok=True)   #created a folder

full_path = os.path.join('Data','data.csv')

df.to_csv(full_path,index=False)

