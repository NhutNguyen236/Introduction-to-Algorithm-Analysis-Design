# What's up danger? Im here to help you draw :)
# Also in my report, I have illustrate run-time of an algorithm so drawing is an essential skill in this case

#There are a lot of drawing lib out there but I am going to use just pylab and pyplot, turtle will come later

#Drawing with pylab 
from matplotlib import pylab
import numpy as np

def pylab_1():
    # pylab function: n^2 

    # Identify x axis value
    x = np.linspace(0,20,10)

    print(x)

    # Identify y axis value
    y = x**2

    # Put in the title

    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.title('O(n) = n^2')

    pylab.plot(x,y,'mo-')
    pylab.show()


pylab_1()

#Drawing with pyplot
from matplotlib import pyplot


def pyplot_1():
    # pyplot function: log(n)

    # Identify x axis value
    x = np.linspace(1,20,10)

    # Identify y axis value
    y = np.log10(x)

    # Put in the title

    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.suptitle('O(n) = log(n)')

    pyplot.plot(x,y,'mo-')
    pyplot.show()

pyplot_1()
