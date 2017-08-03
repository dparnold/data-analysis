import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#read the data
testData = pd.read_csv("test_data.txt", header=None)
#sort it by some column
testData = testData.sort_values([2], ascending=False)

#create a new figure for plotting
fig = plt.figure()
#create the first subplot of a 2x2 matrix
ax = fig.add_subplot(2, 2, 1)
ax.semilogy(range(len(testData[2])), testData[2])
ax.grid(True)

#Plot a histogram of the ocurring countries and sort it descending
countries = testData.groupby(13).count().sort_values(1, ascending=False)[1]
#add the second subplot to the matrix
ax2 = fig.add_subplot(2, 2, 2)
#set the x values of the histogram
x = np.arange(len(countries))
#do the plotting
ax2.bar(range(len(countries)), height= countries)
ax2.set_ylabel('Probability')
ax2.set_yscale('log', nonposy='clip')
ax2.grid()
#change the ticks to the countries names
plt.xticks(x+0.6, countries.index, rotation=90); # +0.6 to move the font a bit to the right
plt.tight_layout()
plt.show()