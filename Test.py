from bs4 import BeautifulSoup
from sklearn import model_selection
import pandas as pd
import requests
from pymongo import MongoClient

#url="www.google.com"
#response= request.get(url)
#soup=BeautifulSoup(response.text,"html.parser")
#s=soup.findAll("div")

df=pd.read_csv("EVS.csv")
print(df)

cols=df["Students"].mean()
print(cols)

rk =df[(df['Rk'] >= 10) & (df['Rk'] <= 150)] 
print(rk)

princy=df[df['Rk']==5]["Princy"].reset_index()
print(princy)

Sorte = df.sort_values(by='State')
print(Sorte)