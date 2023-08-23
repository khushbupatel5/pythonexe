# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:17:48 2023

@author: khushbu vora
"""

import pandas as pd
df=pd.read_csv('C:/Users/khushbu vora/OneDrive/Desktop/pandas/income.csv')
print(df)
#===========================================================================
df=pd.read_csv('C:/Users/khushbu vora/OneDrive/Desktop/pandas/income.csv')
print(df.columns)
#=========================================================================
print(df.dtypes)
print(df['State'].dtypes)
#=========================================================================
df['Y2008']=df['Y2008'].astype(float)
print('Y2008',df.Y2008.dtypes)
print(df.dtypes)
#==========================================================================
print(df.shape)
print(df.shape[0])
print(df.shape[1])
#===========================================================================
print(df.head())
print(df.head(4))

print(df.tail())
print(df.tail(2))
#==================================================================
print(df[0:5])
print(df.iloc[0:5])
#===================================================================
ser=pd.Series([1,2,3,1,2],dtype="category")
print(ser)
#=======================================================================
print(df.Index.unique())
print(df.Index.nunique())
#=====================================================================
print(pd.crosstab(df.index,df.State))
#===================================================================
print(df.sample(n=5))
print(df.sample(frac=0.1))
#=====================================================================
print(df['State'])
print(df[["Index","State","Y2008"]])

print(df.loc[0:2,["Index","State","Y2008"]])
print(df.loc[:,"Index":"Y2008"])
print(df.iloc[:,0:5])
#========================================================================
import numpy as np
x=pd.DataFrame({"var1":np.arange(1,20,2)},
               index=[9,8,7,6,10,1,2,3,4,5])
print(x)

print(x.iloc[:3])
print(x.loc[:10])
#===================================================================
data=pd.DataFrame({"A":["john","Mary","julia","Kenny","Henry"],
                   "B":["Libra","capricorn","Aries","scorpio","Aquarius"]})
print(data)      
#==================================================================== 
           
data=pd.DataFrame({"A":["john","Mary","julia","Kenny","Henry"],
                   "B":["Libra","capricorn","Aries","scorpio","Aquarius"]})
print(data)      
data.columns=['Name','zodiac Signs']
print('\n',data)
#===============================================================================
data.Columns=['Name','Zodiac Signs']
print(data)
data.rename(columns={"Name":"Cust_Name"},inplace=True)
print('\n',data)
#==========================================================================
df.columns=df.columns.str.replace('Y','Year')
print(df.columns)
#=========================================================================

df.set_index("Index",inplace=True)
print(df.head())
print(df.columns,'\n')
print(df.reset_index(inplace=True))
print('\n',df.head())
#=============================================================================

print(df.drop('Index',axis=1))

print(df.drop('Index',axis="columns"))
print(df.drop(['Index','State'],axis=1))
print(df.drop(0,axis=0))
print(df.drop(0,axis="index"))
print(df.drop([0,1,2,3],axis=0)) 

#================================================================
print(df.head())
print(df.sort_values("State",ascending=False))
print(df.sort_values("State",ascending=False,inplace=True))
#print(df.Year2003.sort_Values())
#====================================================================
print(df.sort_values(["Index","Year2002"]) )
df["difference"]=df.Year2008-df.Year2009
print(df)
df["difference"]=df.Year2008-df.Year2009
df["difference"]=df.eval("Year2008-Year2009")
print(df.head())
#======================================================================
data=df.assign(ratio=(df.Year2008/df.Year2009))
print(data.head())
#=========================================================================
print(df.describe())
#print(df.describe(include=['object']))

print(df.Year2003.mean())
print(df.Year2007.median())
print(df.Year2008.min())
print(df.loc[:,["Year2002","Year2008"]].max())
#===========================================================================
print(df.groupby("Index")["Year2002","Year2003"].min())
print(df.groupby("Index")["Year2002","Year2003"].agg(["min","max","mean"]))
print(df.groupby("Index").agg({"Year2008":["min","max"],"Year2009":"mean"}))
#==========================================================================
print(df[df.Index=="A"])
print(df.loc[df.Index=="A",:])
print(df.loc[df.Index=="A","State"])
print(df.loc[(df.Index=="A")&(df.Year2002>1500000),:])
print(df.loc[(df.Index=="A")|(df.Index=="W"),:])
print(df.loc[df.Index.isin(["A","W"]),:])
print(df.query('Year2002>1700000&Year2003>1500000'))
#================================================================================
import numpy as np
mydata={'Crop':['Rice','wheat','Barley','Maize'],
        'Yield':[1010,1025.2,1404.2,1251.7],
        'Cost':[102,np.nan,20,68]}
Crop=pd.DataFrame(mydata)
print(Crop)

print(Crop.isnull())
print(Crop.notnull())
print(Crop.isnull().sum())
print(Crop[Crop.Cost.isnull()])
print(Crop[Crop.Cost.isnull()].Crop)
print(Crop[Crop.Cost.notnull()].Crop)
print(Crop.dropna(how="any").shape)
print(Crop.dropna(how="all").shape)
print(Crop.dropna(subset=['Yield',"Cost"],how='any').shape)
print(Crop.dropna(subset=['Yield',"Cost"],how='all').shape)
Crop['Cost'].fillna(value="UNKNOWN",inplace=True)
print(Crop)
#==========================================================================
data=pd.DataFrame({"Items":["TV","Washing Machine","Mobile","TV","TV","Washing Machine"],
                   "Price":[10000,50000,20000,10000,10000,40000]})
print(data)

print(data.loc[data.duplicated(),:])
print(data.loc[data.duplicated(keep="first"),:])
print(data.loc[data.duplicated(keep="last"),:])
print(data.loc[data.duplicated(keep=False),:])

print(data.drop_duplicates(keep="first"))
print(data.drop_duplicates(keep="last"))
print(data.drop_duplicates(keep=False,inplace=True))
#============================================================================
iris=pd.read_csv("C:/Users/khushbu vora/anaconda3/pkgs/bokeh-2.4.2-py39haa95532_0/Lib/site-packages/bokeh/sampledata/_data/iris.csv")
print(iris)

iris["setosa"]=iris.species.map({"setosa":1,"versicolor":0,"virginica":0})
print(iris.head())

print(pd.get_dummies(iris.species,prefix="species"))
#print(pd.get_dummies(iris.species,prefix="species").iloc[:,0,:1])

species_dummies=pd.get_dummies(iris.species,prefix="species").iloc[:,0:]
print(species_dummies)

iris=pd.concat([iris,species_dummies],axis=1)
print(iris.head())

#=========================================================================================
print(iris.rank())

iris['Rank2']=iris['sepal_length'].groupby(iris["species"]).rank(ascending=1)
print(iris.head())

iris['cum_sum2']=iris["sepal_length"].cumsum()
print(iris.head())

print(iris.quantile(0.5))
print(iris.quantile([0.1,0.2,0.5]))
print(iris.quantile(0.55))
#========================================================================================
data1=iris._get_numeric_data()
print(data.head(3))

data4=iris.select_dtypes(include=['object'])
print(data4.head(2))


students=pd.DataFrame({'Name':['John','Marry','Henry','Augustus','Kenny'],
                       'zodiac sign':['Aquarius','Libra','Gemini','Pisces','Virgo']})
students2=pd.DataFrame({'Name':['John','Mary','Henry','Augstus','Kenny'],
                        'Marks':[50,81,98,25,35]})                                             
data=pd.concat([students,students2])
print(data) 

data=pd.concat([students,students2],axis=1)
print(data)


print(students.append(students))

classes={'x':students,'y':students2} 
result=pd.concat(classes)
print(result)
#==========================================================================================

result=pd.merge(students,students2,on='Name')
print(result)

result=pd.merge(students,students2,on='Name',how="left") 
print(result)

result=pd.merge(students,students2,on='Name',how="right",indicator=True)
print(result)











