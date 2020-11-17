# What's up danger? Im here to help you draw :)
# Also in my report, I have illustrate run-time of an algorithm so drawing is an essential skill in this case

#There are a lot of drawing lib out there but I am going to use just pylab and matplotlib, turtle will come later

#Drawing with pylab 
from matplotlib import pylab
import numpy as np

def pylab_1():
    # pylabfunction n^2 

    # Identify x axis value
    x = np.linspace(0,20,1000)

    # Identify y axis value
    y = np.sin(x)

    # Put in the title

    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.title('sin(x)')

    pylab.plot(x,y)
    pylab.show()


pylab_1()

    
    
