import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

Xdata = np.arange(0,6,.01)
Zdata = []
Sdata = []

# find z
def Z(x):
    z = (1/( np.sqrt( (2*np.pi) ) ))*(np.power(np.e, ( (-.5) * (x*x) ) ))
    return z

# get sum
def Sum(z1,z2):
    sum = ( (z1+z2)/2 ) * (.01)
    return sum

# loop through data get all z values
for x in Xdata:
    Zdata.append(Z(x))
Zdata = np.asarray(Zdata)

for x in range(0, len(Zdata)):
    if x==0:
        Sdata.append(0.0000)
    else:
        Sdata.append( Sdata[x-1]+Sum(Zdata[x-1], Zdata[x]))
Sdata = np.asarray(Sdata)

#######################################
# plotting data(s)
decimalPlaces = 8

col = np.arange(0.0,.1,.01)
row = np.arange(0,6,.1)
x = Sdata # for plotting
Sdata = Sdata.reshape(len(row), len(col))

p = PrettyTable()
p.field_names = "z",col[0],col[1],col[2],col[3],col[4],col[5],col[6],col[7],col[8],col[9]
for i in range(51):
    r = [ "%.1f" %row[i],str(Sdata[i][0])[:decimalPlaces],str(Sdata[i][1])[:decimalPlaces],str(Sdata[i][2])[:decimalPlaces],str(Sdata[i][3])[:decimalPlaces],str(Sdata[i][4])[:decimalPlaces],str(Sdata[i][5])[:decimalPlaces],str(Sdata[i][6])[:decimalPlaces],str(Sdata[i][7])[:decimalPlaces],str(Sdata[i][8])[:decimalPlaces],str(Sdata[i][9])[:decimalPlaces] ]
    r = [ "%.1f" %row[i],str(Sdata[i][0])[:decimalPlaces],str(Sdata[i][1])[:decimalPlaces],str(Sdata[i][2])[:decimalPlaces],str(Sdata[i][3])[:decimalPlaces],str(Sdata[i][4])[:decimalPlaces],str(Sdata[i][5])[:decimalPlaces],str(Sdata[i][6])[:decimalPlaces],str(Sdata[i][7])[:decimalPlaces],str(Sdata[i][8])[:decimalPlaces],str(Sdata[i][9])[:decimalPlaces] ]
    p.add_row(r)

#######################################
# plotting data(s) on graph

fig, ax = plt.subplots(figsize=(5.5, 5.5))
y = []
for i in range(60):
    for j in range(10):
        y.append(i+col[j])

plt.stem(x, y, use_line_collection=True)
plt.show()