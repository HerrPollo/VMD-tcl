import numpy as np
import csv
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
archivo=input("Tira el nombre de tu archivo otra vez...")

p1 = figure()
p1.grid.grid_line_alpha=1
p1.xaxis.axis_label = 'Residue number'
p1.yaxis.axis_label = 'RMSF (\u212B)'
x = []
y = []
x1 = []
xa = []
ya = []
m = 0
with open(archivo+'_RMSF.csv', newline='') as a:
    reader = csv.reader(a)
    for row in reader:
    	xa.append(row[0])
    	ya.append(row[1])
#x.pop(0)
#y.pop(0)
for n in xa:
	x1.append(float(xa[m]))
	m = m+1
p1.line(x1, ya, color='#8e8c3e', legend='RMSF vs Residue number')
p1.legend.location = "top_left"
window_size = 30
window = np.ones(window_size)/float(window_size)

output_file("RMSF.html", title="RMSF de archivo")
show(gridplot([[p1]], plot_width=1000, plot_height=600))  # open a browser
