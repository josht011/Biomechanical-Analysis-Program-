import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as pt
import csv
import os
import generateGraphs








##lists to hold the data from the csv file
x = []
yLKnee = []
yRKnee = []

inputFile = "tse/scan_data.csv"
##open the csv file as read only, read the column needed
with open (inputFile, "r") as dataSet:
    plots = csv.reader(dataSet, delimiter=",") 

    ##changes the above lists with CSV values
    for row in plots:
        x.append(row[0])
        yLKnee.append(row[1])
        yRKnee.append(row[4])


        

    



##remove the first value from list (non int value)
x.remove(x[0])
yLKnee.remove(yLKnee[0])
yRKnee.remove(yRKnee[0])


##convert lists to INT from string
xInt = [eval(i) for i in x]
yLKneeInt = [eval(i) for i in yLKnee]
yRKneeInt = [eval(i) for i in yRKnee]


##create graph
pt.axis([0, 200, 0, 70]) ##(X AXIS)(Y AXIS)

##plot graph
pt.plot(xInt,yLKneeInt, color = "red", label = "Left Knee")
pt.plot(xInt, yRKneeInt, color = "blue", label = "Right Knee")
pt.legend(loc="upper left") ##location of key
pt.show() ##show graph


