# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 13:28:42 2023

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
The following function is used to create a line plot.
The dataset and a list containing headers of the columns other than Year are passed as arguments
'''


def lineplot(data_1, countries):
    data1 = data_1  # Dataset for line plotting is stored in a new variable
    print(data1)  # Printing the dataset that is used for line plotting
    plt.figure(figsize=(8, 6))
    for con in countries:
        plt.plot(data1["Year"], data1[con], label=con)
    plt.xlim(1998, 2021)  # Setting the limit for the x-axis of the graph
    plt.ylim(0, 75)  # Setting the limit for the y-axis of the graph
    plt.xticks(data1["Year"], labels=data1["Year"], rotation="vertical")
    plt.xlabel("Year")  # Labelling x-axis
    plt.ylabel("Fertility Rate")  # Labelling y-axis
    # Title for the graph
    plt.title("Adolescent Fertility Rate (births per 1000 women ages 15 -19)")
    plt.legend()
    # Saving the line plot as png
    plt.savefig("Fertility Rate_Line Plot.png")
    plt.show()
    return  # Return statement is used at the end of a function


'''
The following function is used to create a pie chart.
The dataset is passed as an argument for plotting.
'''


def piechart(data_pie):
    piedata = data_pie  # Dataset for plotting pie chart is stored in new variable
    print(piedata)  # Printing the dataset that is used for pie chart plotting
    plt.figure(figsize=(5, 5))
    plt.pie(piedata["2010"], labels=piedata["Countries"], autopct="%1.1f%%")
    # Title for the pie chart
    plt.title("Internet Users (per 100 people) in 2010")
    plt.savefig("Internet Users - Pie Chart.png")
    plt.show()
    return  # Return statement is used at the end of a function


'''
The following function is used to create a bar plot.
The dataset and a list containing headers of the columns other than Year are passed as arguments
'''


def barplot(data_bar, gender):
    data3 = data_bar  # Dataset for plotting bar graph is stored in a new variable
    print(data3)  # Printing the dataset that is used for bar graph plotting
    plt.figure(figsize=(7, 6))
    for gen in gender:
        plt.bar(data3["Year"], data3[gen], label=gen)
    plt.title("Bar Plot of Suicide Mortality Rate")  # Title for the graph
    plt.ylim()
    plt.xlim(1999, 2020)  # Setting the limit for the x-axis of the graph
    plt.xticks(data3["Year"], labels=data3["Year"], rotation='vertical')
    plt.xlabel("Year")  # Labelling x-axis
    plt.ylabel("Suicide Mortality Rate")  # Labelling y-axis
    plt.legend()
    plt.savefig("Suicide Mortality - Bar Graph.png")
    plt.show()
    return  # Return statement is used at the end of a function


if __name__ == "__main__":
    #Following code is used to read the dataset in excel form for line plotting
    data_line = pd.read_excel("data_fertility_rate.xlsx")
    #Following code is used to read the dataset in excel form for plotting pie chart
    data_pie = pd.read_excel("data_internet_users.xlsx")
    #Following code is used to read the dataset in excel form for plotting bar graph
    data_bar = pd.read_excel("data_mortality_rate.xlsx")

    #Calling the lineplot function
    lineplot(data_line, ["China", "India", "Kuwait", "Pakistan"])
    #Calling the piechart function
    piechart(data_pie)
    #Calling the bar graph function
    barplot(data_bar, ["SMR_male", "SMR_female"])
