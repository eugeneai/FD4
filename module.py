#!/usr/bin/python2.7
import numpy

class DynModel(object):
    """Dynamic model
    """

    def __init__(self, ):
        """
        """

        self.prepared=False

    def prepare(self):
        """Prepare the model to be simulated
        """

    def simulate(self, t=50, dt=1):
        """Perform computer simulation for t Years.
        """

    def connect(self, s1, s2, tau):
        """

        Arguments:
        - `s1`: A source state
        - `s2`: A destination state
        - `tau`: A transition intensity

        """

    def state(self, statename):
        """Declare a state existence.

        Arguments:
        - `statename`: Name of the state to be declared
        """

def tes1():
    """Make a simple model test.
    """
    m=DynModel()
    m.state('S1')
    m.state('S2')
    m.state('S3')
    m.connect('S1','S2',0.1)
    m.connect('S2','S3',0.1)

    m.prepare()
    m.simulate()



if __name__=="__main__":
    tes1()
    print "ok"
