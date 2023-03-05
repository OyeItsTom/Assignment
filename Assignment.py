#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:00:52 2023

@author: tomthomas
"""


import pandas as pd
from matplotlib import pyplot as plt

#To read in and prepare railway fare data for further analysis, use this function.
def readData() :
    #importing the multi-indexing CSV file using the Pandas read csv() function. In order to use the first two rows of the CSV file as the column headings, the header parameter is set to [0,1]. 
    #The first column should be used as the row index, hence the index col option is set to [0] to denote this.
    data1 = pd.read_csv('Train Fares.csv',header=[0,1],index_col=[0])
    #selects only the "All operators" column from data1 to build a new DataFrame Fares. The DataFrame is cut using the.loc method by choosing all rows (:) and the "All operators" column.
    Fares=data1.loc[:, 'All operators']
    #With the.drop() method, the last row of Fares is removed, which removes data that can't be used to make a line plot.
    Fares.drop(Fares.tail(1).index,inplace=True)
    #uses the.astype() method to convert the Fares index to integers, then assigns the outcome to the variable x.
    x=Fares.index.astype(int)
    #Both x and Fares are variables that the function returns. Fares has the "All operators" data of the original DataFrame data1, with the final row removed, and x contains the integer index values of the rows in Fares.
    return x,Fares

#making a line plot with axes that are labelled and a legend.
def linePlot(x,Fares):
    #to make a lineplot figure 15 inches wide by 10 inches tall.
    plt.figure(figsize=(15,10))
    #to set the title of the plot.
    plt.title("From 2004 through 2022, the average change in rail fares in Great Britain",fontweight='bold')
    #should draw six distinct lines on the graph, one for each variety of fare. 
    #The years are represented on the x-axis, and the index-based inflation rates are shown on the y-axis.
    plt.plot(x, Fares["Advance"], label="Advance")
    plt.plot(x, Fares["Anytime"], label="Anytime")
    plt.plot(x, Fares["Off Peak"], label="Off Peak")
    plt.plot(x, Fares["Season"], label="Season")
    plt.plot(x, Fares["Super Off Peak"], label="Super Off Peak")
    plt.plot(x, Fares["Others"], label="Others")
    #to set the years 2004 to 2022 as the x-range axis's
    plt.xlim(2004,2022)
    # set the y-index axis's range to 100–220.
    plt.ylim(100,220)
    #to correspondingly set the labels for the x and y axes.
    plt.xlabel("Years",fontweight='bold')
    plt.ylabel("Index-based inflation rates",fontweight='bold')
    #to develop a legend for the plot
    plt.legend()
    #saving the lineplot as a picture file
    plt.savefig("linplot.png",dpi=100)
    #to make the plot visible on the screen.
    plt.show()
    return

#main code that will be executed once the script has been run
if __name__ == "__main__":
    #for reading in the data for the line plot by calling the readData() function
    result1, result2 = readData()
    #using the data read in from the readData() method, calls the linePlot() function to produce a line plot.
    linePlot(result1,result2)


    
    
    
    
    
    
