import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go #no need COMPLEX 

def Line(start,end):
    line = "{0} {1} {2} {3}"
    return line.format(start[0] ,end[0],start[1],end[1])

def BBRectange(bbMin,bbMax):
    x1 = bbMin[0]
    y1 = bbMin[1]
    x3 = bbMax[0]
    y3 = bbMax[1]
    x2 = x1
    y2 = y3
    x4 = x3
    y4 = y1
    rec = "{0} {1} {2} {3} {4} {5} {6} {7}"
    return rec.format(x1,y1,x2,y2,x3,y3,x4,y4)

def plotRectange(_bbMin,_bbMax,scale):
    bbMin = _bbMin.split(" ")
    bbMax = _bbMax.split(" ")
    x1 = float(bbMin[0])/float(scale)
    y1 = float(bbMin[1])/float(scale)
    x3 = float(bbMax[0])/float(scale)
    y3 = float(bbMax[1])/float(scale)
    x2 = x1
    y2 = y3
    x4 = x3
    y4 = y1
    xpoints = np.array([x1,x2,x3,x4,x1,x3])
    ypoints = np.array([y1,y2,y3,y4,y1,y3])
    plt.plot(xpoints, ypoints)
    plt.show()
def plotLine(StartPoint,EndPoint,scale):
    x1 = float(StartPoint[0])/float(scale)
    y1 = float(StartPoint[1])/float(scale)
    x3 = float(EndPoint[0])/float(scale)
    y3 = float(EndPoint[1])/float(scale)
    x2 = x1
    y2 = y3
    x4 = x3
    y4 = y1
    xpoints = np.array([x1,x3])
    ypoints = np.array([y1,y3])
    plt.plot(xpoints, ypoints)
    plt.show()
def plotLines(Lines,scale):
    L = len(Lines)
    xArray = []
    yArray = []
    for i in range(L):
        xs = []
        ys = []
        line = Lines[i]
        StartPoint = line.split(" ")[0:2]
        EndPoint = line.split(" ")[2:]
        x1 = float(StartPoint[0])/float(scale)
        y1 = float(StartPoint[1])/float(scale)
        x3 = float(EndPoint[0])/float(scale)
        y3 = float(EndPoint[1])/float(scale)
        x2 = x1
        y2 = y3
        x4 = x3
        y4 = y1
        xArray.append(x1)
        xArray.append(x3)
        yArray.append(y1)
        yArray.append(y3)

    x1 = xArray[0]
    y1 = yArray[0]
    xArray.append(x1) #for loop
    yArray.append(y1) #for loop

    xpoints = np.array(xArray)
    ypoints = np.array(yArray)
    plt.plot(xpoints, ypoints)
    plt.show()

# bbMin = input("X Y Boundingbox MIN point:").split(" ") # -18000 -74000
# bbMax= input("X Y Boundingbox MAX point:").split(" ") # 116000 105000
# scale = float(input("Plot Scale (1/x):"))
# plotRectange(bbMin,bbMax,scale)
# plotLine(bbMin,bbMax,scale)