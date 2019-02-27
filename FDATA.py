'''Author Shivam Sharma
created on:- Jan 2, 2019
Updated on:- feb 27,2019'''
## First import panda to read an excel file as a dataframe

import pandas as pd

##Create a dictionary to hold all the tabs in different datafeames 

dict={}
count=0

##Read all the tabs at index i  and for not exceeding the limit we use exception handling 
##In panda if we use read_excel by default it reads only first tab of the excel for reading different tabs 
##we use sheet_name which starts from 0 index  

for tab in range (0,10):
    try:
        dict[tab]=pd.read_excel(r"<your excel file path>",sheet_name=i, index_col=0)
        count+=1
    except IndexError:
        i=10

##It reads rows of dataframe of tab 

dict[0].head()

##It takes name of excel file which user want to create & It also convert the data frame into excel file according to users name 

for i in range(0,count):
    c.append(input("enter  name of tab with extension"))
    dict[i].to_excel(pd.ExcelWriter(c[0],engine='xlsxwriter'))