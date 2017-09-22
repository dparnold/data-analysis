def polyFit(xData, yData, degree):
    pass
    fitValues = np.polyfit(xData, yData, degree)
    yFit = np.zeros(len(xData))
    for i in range(degree+1):
        yFit = yFit + xData**(degree-i)*fitValues[i]
    def function(x):
        func = 0
        for i in fitValues:
            func = func*x + i
        return func
    return (fitValues,function)



if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import pltStyle # used for formatting the plots

    # read some data
    data = pd.read_csv("polyFit.csv", header=None, names=["x","y"])
    # create a new figure object
    fig =  plt.figure()
    # create axis and a new subplot within the figure
    ax = fig.add_subplot(1, 1, 1)
    # plot the measurement data
    ax.plot(data.x, data.y,marker="+", label="Measurement data")
    # add polynomial fits with different degrees
    for i in range(1,7,1):
        ax.plot(data.x, polyFit(data.x,data.y,i)[1](data.x), label="Polynomial fit degree = "+str(i))
    # create the legend and set its position
    ax.legend(loc="lower left")
    # manually set the axes limits and label them
    ax.set_xlim([0,12])
    ax.set_ylim([-2,1.1])
    ax.set_xlabel(r'x axis label using \TeX\  and SI-units such as an upright $\si{\micro}$')
    ax.set_ylabel(r'unusual symbols {\"a} \c{s} \AE\  \~{n}')
    ax.grid(True)
    #plt.tight_layout()
    plt.savefig("polyFit.png")
