import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Create some example data to see whether we are doing the job right
xExampleData = [1, 1, 1, 2, 2, 2, 3, 3, 3]
yExampleData = [10, 20, 30, 10, 20, 30, 10, 20, 30]
zExampleData = [0, 3, 0, 3, 4, 5, 1, 1, 6]

def listDensityPlot(x,y,z):
	# Convert to numpy arrays
	x =  np.array(x)
	y =  np.array(y)
	z =  np.array(z)

	xUnique = np.unique(x) # Returns the sorted unique elements of an array
	yUnique = np.unique(y)

	imageZ = np.zeros((len(xUnique),len(yUnique))) # Create 2D numpy array for plotting

	for i,xitem in enumerate(xUnique):
		xMask = x==xitem 			# Create a array of Bool values where the value xitem is located in x
		for j,yitem in enumerate(yUnique):
			yMask = y==yitem		# Create a array of Bool values where the value yitem is located in y
			if np.sum(xMask*yMask)!=0:	# Ignore missing values
				imageZ[i,j] = z[xMask * yMask] 	# Set the value of imageZ at i,j to the appropriate value of z for the combination of xitem and yitem
	# xMask * yMask gives a Bool array where only one value is true
	# Example: 	exampleMask = np.array([False,False,True,False,False,False], dtype=bool)
	# 			exampleArray = np.array([1, 2, 3, 4, 5, 6])
	#			exampleArray[exampleMask] gives the value of 3 because there is the only True value

	# Do the plotting
	plt.imshow(np.rot90(imageZ), aspect='auto', extent=(np.min(xUnique),np.max(xUnique),np.min(yUnique),np.max(yUnique)))
	# Add norm=LogNorm(vmin=np.min(z), vmax= np.max(z)) for logarithmic axis
	plt.colorbar(label='zLabel [zUnit]')

	plt.title('plotTitle')
	plt.xlabel('xLabel [xUnit]')
	plt.ylabel('yLabel [yUnit]')
	plt.grid()
	plt.show()

if __name__ == '__main__':
	listDensityPlot(xExampleData,yExampleData,zExampleData)
