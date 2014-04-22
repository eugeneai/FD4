#!/usr/bin/python2.7
import numpy

class DynModel(object):
    """Dynamic model
    """

    def __init__(self, ):
        """
        """

        self.prepared=False
        self.v=set()
        self.e={}

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
        if not s1 in self.v:
            raise ValueError, "s1 not a state"
        if not s2 in self.v:
            raise ValueError, "s2 not a state"

        obj=(s1,s2)

        if obj in self.v:
            raise ValueError, "this edge already defined"

        self.e[obj]=tau

    def state(self, statename):
        """Declare a state existence.

        Arguments:
        - `statename`: Name of the state to be declared
        """
        if statename in self.v:
            raise ValueError, "state already exists"
        self.v.add(statename)

def tes1():
    """Make a simple model test.
    """
    m=DynModel()
    m.state('S1')
    m.state('S2')
    m.state('S3')
    m.connect('S1','S2',0.1)
    m.connect('S2','S3',0.1)

    assert len(m.v)==3
    assert len(m.e)==2

    m.prepare()
    m.simulate()



if __name__=="__main__":
    tes1()
    print "ok"
