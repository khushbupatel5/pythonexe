# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:03:39 2023

@author: khushbu vora
"""
#task 1
import pandas as pd
df=pd.read_csv('C:/Users/khushbu vora/OneDrive/Desktop/pandas/food_consumption.csv')
print(df.shape)

df=pd.read_csv('C:/Users/khushbu vora/OneDrive/Desktop/pandas/food_consumption.csv',)
print(df.columns)

df=pd.read_csv('C:/Users/khushbu vora/OneDrive/Desktop/pandas/food_consumption.csv',)
print(type(df))
#======================================================================================
#task 2
df=pd.read_csv('C:/Users/khushbu vora/OneDrive/Desktop/pandas/food_consumption.csv')
print(df.shape)
#=============================================================================================
#task 3
print(df.dtypes)
print(df['country'].dtypes)
#============================================================================================
# task 4
dv2=df["co2_emmission"].mean()
print(dv2)
#=============================================================================================
#task 5
print("types of food",df.food_category.unique())
print("types of food",df.food_category.unique())
#==========================================================================================
#task 6
print(df.groupby("co2_emmission").max())
#===========================================================================================
#task 7
df.iloc[df['co2_emmission'].idxmax()]
print(df)
#========================================================================================
# task 8
df.query("co2_emmission > 1000")
print(df)
#======================================================================================
# task 9
(df.query("food_category=='Beef' ")
   . sort_values(by="consumption")
   . head(1))
print(df)
#==================================================================================
# task 10
(df.query("food_category=='soybeans' ")
   . sort_values(by="consumption",ascending=False)
   . head(1))
print(df)
#=======================================================================================
#task 11

meat=['Poultry','Pork','Fish','lamb & goat','Beef']
df["co2_emmission"][df['food_category'].isin(meat)].sum(())