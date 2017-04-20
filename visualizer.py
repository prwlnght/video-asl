import matplotlib.pyplot as plt
import numpy as np
import os
import time
#function takes a path and optional
def visualize(path_to_matrix, path_to_save = None, name_to_save = None):
    if path_to_matrix is None:
        return
    if name_to_save is None:
        name_to_save = "visualize_"
    if path_to_save is None:
        path_to_save = 'visualized\\'
    my_data = np.genfromtxt(path_to_matrix, delimiter=' ')
    #set x-axis
    x_axis = np.arange(my_data.shape[0])
    y_axis = np.arange(my_data.shape[1])
    #iterate over x_axis
    #set up the axes for the plot
    my_plot_axis = [0, my_data.shape[0]+1, 0, my_data.shape[1]]
    plt.clf()
    plt.axis(my_plot_axis)
    plt.scatter(x_axis, np.argmax(my_data, axis=1)+1, s= 200 * np.amax(my_data, axis=1))
    #plt.show()
    visualize_path_name = path_to_save + name_to_save + "_" + time.strftime("%Y%m%d-%H%M%S") + ".png"
    plt.savefig(visualize_path_name)
#for each row
    #take maximum
    #1.plot in index thickness*value
    #plot end
#end for


#visualize("C:\\Users\\ppaudyal\\workspace\\video-asl\\name")