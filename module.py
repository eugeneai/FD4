#!/usr/bin/python2.7
import numpy
import math
from collections import OrderedDict

label=object()

class Storage(object):
    """Stores the results of the modeling
    """

    def __init__(self, ):
        """
        """

        self.S=[]
        self.T=[]

class DynModel(object):
    """Dynamic model
    """

    def __init__(self, ):
        """
        """

        self.prepared=False
        self.v=OrderedDict()
        self.rv={}
        self.e={}

    def prepare(self):
        """Prepare the model to be simulated
        """
        ls=len(self.v)
        self.S=numpy.zeros(ls)
        self.A=numpy.zeros((ls,ls))

        for k,v in self.e.items():
            b,e=k
            bi,ei=self.rv[b],self.rv[e]
            self.A[bi,bi]-=v
            self.A[bi,ei]+=v

    def simulate(self, t=50, dt=1, init=True, save=label):
        """Perform computer simulation for t Years.
        - `init`: Should the system initialize state
        to the initial values at first.
        """

        if init:
            self.initialize()

        #dS=numpy.zeros(S.shape)
        steps=int(math.ceil(t/dt))
        if save==label:
            st_steps=int(math.ceil(1/dt))
        else:
            st_steps=save
        t=0.0
        S=self.S
        A=self.A
        for s in xrange(steps):
            if s % st_steps == 0:
                self.storage.S.append(self.S)
                self.storage.T.append(t)
            dS=numpy.dot(S, A)
            if dt!=1:
                dS=dS*dt

            #print dS
            S+=dS
            t+=dt

        self.S=S

        # Perform simulation

    def initialize(self):
        """Initialize the initial values of the states
        """

        for i, item in enumerate(self.v.items()):
            state, value = item
            if value == None:
                raise ValueError, "state '%s' has no value" % state
            self.S[i]=value
        self.storage=Storage()


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

    def state(self, statename, value=None):
        """Declare a state existence.

        Arguments:
        - `statename`: Name of the state to be declared
        """
        if statename in self.v:
            raise ValueError, "state already exists"
        self.rv[statename]=len(self.v)
        self.v[statename]=value

def tes1():
    """Make a simple model test.
    """
    m=DynModel()
    m.state('S1',1.0)
    m.state('S2',0.0)
    m.state('S3',0.0)
    m.connect('S1','S2',0.1)
    m.connect('S2','S3',0.1)
    #import pudb; pu.db
    assert len(m.v)==3
    assert len(m.e)==2

    m.prepare()
    m.simulate()

    print m.storage.S
    print m.storage.T


if __name__=="__main__":
    tes1()
    print "ok"
