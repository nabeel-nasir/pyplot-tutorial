# pyplot tutorial

Code samples to understand the matplotlib.pyplot interface for plotting figures.

### Terminology
This picture from the usage guide describes all of the major elements in a matplotlib plot:
![alt text](https://matplotlib.org/3.1.1/_images/anatomy.png)


#### matplotlib
- Object-oriented Python Library for plotting
- Figure and Axes are the main objects
- Figure: The "canvas" which contains the plots. It provides “figure level” operations.  
e.g.: set figure size, figure title etc.
- Axes: What we generally think of as a "plot". A figure can have one or more Axes. All of the plotting operations are done on the Axes object.  
e.g.: plot, hist, scatter etc.

#### matplotlib.pyplot
- pyplot is an interface which provides MATLAB-like syntax for matplotlib
- There is a concept of a *current Figure* when using pyplot. If you don't specify any Figure, plt automatically creates a Figure (figure with index 1) and all further operations are performed on it.
- Any operation is performed on the current Figure and the current Axes  
e.g.: ```plt.plot()```
- There are certain operations not supported by the pyplot interface. These are operations that you can be perform on the Figure object or the Axes object. You can access the current Figure or the current Axes using ```plt.gcf()``` and ```plt.gca()``` and operate on them. gcf() stands for "get current figure" and gca stands for "get current axes".  
e.g.: ```plt.gca().yaxis.set\_major\_locator(MultipleLocator(10))``` accesses the current Axes object, accesses the y-axis Axis object for the Axes, and then sets the major ticks at an interval of 10.

### References
Most of the code samples are taken from this [excellent matplotlib tutorial](https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596)  
[matplotlib Usage Guide](https://matplotlib.org/3.1.1/tutorials/introductory/usage.html)  
[Difference between drawing plots using plot, axes, and figure in matplotlib?](https://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl)  
[Load csv file with numpy](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html) 

Plotting a Cumulative Distributive Function (CDF):  
[Understanding a CDF](https://towardsdatascience.com/what-why-and-how-to-read-empirical-cdf-123e2b922480)  
[CDF with pyplot](https://stackoverflow.com/a/11692365/445964)   
[CDF in python](https://cmdlinetips.com/2019/05/empirical-cumulative-distribution-function-ecdf-in-python/)  
