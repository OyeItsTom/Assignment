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

#This function is helpful for reading in and preprocessing rail revenue data in preparation for further analysis, particularly where the "Time period" column is crucial for examining trends over time.
def readData1():
    #The Excel file is read using the Pandas read excel() function, and the resulting DataFrame is then assigned to the variable data2.
    data2 = pd.read_excel("Rail Revenue.xlsx")
    #sets the index of the data2 to be the "Time period" column when creating a new DataFrame with the name data2_updated.
    data2_updated=data2.set_index('Time period')
    #to remove the last column from the DataFrame data2_updated
    data2_updated=data2_updated.drop(data2_updated.columns[-1], axis=1)
    #data2 and data2_updated are the two variables that the function returns. Whereas data2_updated has the same DataFrame with the 'Time period' column used as the new index, data2 contains the original DataFrame read in from the Excel file.
    return data2,data2_updated
 

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

#to be plotting a bar graph of the "Total passenger revenue" data against the "Time period" column in the given DataFrame.
def barPlot(data):
    #the process of giving x and y values
    x = data['Time period']
    y = data['Total passenger revenue']
    # Create the barplot figure 20 inches wide by 17 inches tall.
    plt.figure(figsize=(20,17))
    plt.bar(x, y)
    #to vertically rotate the x-labels for readability
    plt.xticks(rotation=90)
    # Add labels and a title
    plt.xlabel('Time period',fontsize=16, fontweight='bold')  
    plt.ylabel('Income in millions(GBP)',fontsize=16, fontweight='bold')
    plt.title('Great Britains rail passenger revenue from April 2010 to March 2022',fontsize=16, fontweight='bold')
    #saving the barplot as a picture file
    plt.savefig("Barplot.png",dpi=100)
    # Display the plot
    plt.show()
    return

#creating a two-level pie chart for two time periods.    
def piePlot(data2_updated):
    #Choosing the information and calculating the total revenue for each period
    a = data2_updated.loc['Apr 2020 to Mar 2021']
    b = data2_updated.loc['Apr 2021 to Mar 2022']
    total1 = round(sum(a),2)
    total2 = round(sum(b),2)
    # Create subplots for each time period
    fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(8,10))
    #Creating a pie chart for the years 2021–2022, adding a title and the total value.
    ax1.pie(data2_updated.loc['Apr 2021 to Mar 2022'], labels=data2_updated.columns, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'purple','orange'])
    ax1.set_title('Great Britain, 2020–2021, proportion of passenger revenue by ticket type',fontweight='bold')
    ax1.text(0, 0, f'Total Revenue: £{total1:,} Millions',ha='left', va='baseline', transform=ax1.transAxes, fontsize=10, fontweight='bold')
    #Creating a pie chart for the years 2020–2021, adding a title and the total value.
    ax2.pie(data2_updated.loc['Apr 2020 to Mar 2021'], labels=data2_updated.columns, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'purple','orange'])
    ax2.set_title('Great Britain, 2021–2022, proportion of passenger revenue by ticket type',fontweight='bold')
    ax2.text(0, 0, f'Total Revenue: £{total2:,} Millions',ha='left', va='baseline', transform=ax2.transAxes, fontsize=10, fontweight='bold')
    #Save the figure
    plt.savefig("Pieplot.png",dpi=100)
    #Show the figure
    plt.show()
    return
    

#main code that will be executed once the script has been run
if __name__ == "__main__":
    #for reading in the data for the line plot by calling the readData() function
    result1, result2 = readData()
    #readData1() is used to read data into the bar and pie charts.
    result3, result4 = readData1()
    #using the data read in from the readData() method, calls the linePlot() function to produce a line plot.
    linePlot(result1,result2)
    #using the data read in from the readData1() method, calls the barPlot() function to produce a bar plot.
    barPlot(result3)
    #using the data read in from the readData1() method, calls the piePlot() function to produce a pie plot.
    piePlot(result4)


    
    
    
    
    
    
