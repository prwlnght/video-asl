import matplotlib.pyplot as plt
import numpy as np

def visualize(path):
    if(path is None):
        return
    my_data = np.genfromtxt(path, delimiter=' ')
    #set x-axis
    x_axis = np.arange(my_data.shape[0])
    y_axis = np.arange(my_data.shape[1])
    #iterate over x_axis
    #set up the axes for the plot
    my_plot_axis = [0, my_data.shape[0], 0, my_data.shape[1]]
    plt.clf()
    plt.axis(my_plot_axis)
    plt.scatter(x_axis, np.argmax(my_data, axis=1), s= 200 * np.amax(my_data, axis=1))
    plt.show()

#for each row
    #take maximum
    #1.plot in index thickness*value
    #plot end
#end for


visualize("C:\\Users\\ppaudyal\\workspace\\video-asl\\name")