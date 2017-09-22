import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LogNorm

def listDensityPlot(x,y,z, ax):
	data = pd.DataFrame(
		{'x':x,
		 'y':y,
		 'z':z
		}
	)
	xUnique = np.sort(data.x.unique())
	yUnique = data.y.unique()
	matrix = np.zeros((len(xUnique),len(yUnique)))
	for i, xValue in enumerate(xUnique):
		matrix[i, :] = data.sort_values(['y'])[data.x == xValue]['z']
	matrix = np.rot90(matrix)

	densityPlot = ax.imshow(matrix, aspect='auto',
			   extent=(np.min(xUnique), np.max(xUnique), np.min(yUnique), np.max(yUnique)))
	# norm=LogNorm(vmin=data.z.min(), vmax=data.z.max()) can also be used

	return densityPlot

if __name__ == "__main__":
	import pltStyle # used for formatting the plots
	data = pd.read_csv("listDensityPlot.csv", sep=",")

	# create a new figure and some subplots
	fig, ((ax1, ax2)) = plt.subplots(2, 1, sharex=True,)

	# add first plot to ax1
	densityPlot1 = listDensityPlot(data.E1,data.E2,data.timeSpread, ax1)
	plt.colorbar(densityPlot1, ax=ax1, label='zLabel1 [zUnit]')
	ax1.set_ylabel("yLabel1 [yUnit]")
	# add second plot to ax2
	densityPlot2 = listDensityPlot(data.E1, data.E2, data.TOF, ax2)
	plt.colorbar(densityPlot2, ax=ax2, label="zLabel2 [zUnit]")
	ax2.set_ylabel("yLabel2 [yUnit]")
	ax2.set_xlabel("xLabel [xUnit]")
	plt.tight_layout()
	plt.savefig("listDensityPlot.png")

