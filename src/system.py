import numpy as np
from scipy.signal import lti
from pathlib import Path
import json


class System():

    def __init__(self,order, type, params):
        self.order = order
        self.type = type
        self.params = params

    @property    
    def lti(self):
        params = self.params

        if (self.order == 1):
            K = params["K"]
            tau = params["tau"]
            den = [tau,1]

            if self.type == "LP":
                num = [K]

        if (self.order == 2):
            K = params["K"]
            m = params["m"]
            w0 = params["w0"]

            den = [(1/w0**2),2*m/w0,1]

            if self.type == "LP":
                num = [K]

            if self.type == "BP":
                num = [2*m*K/w0,0]

            if self.type == "HP":
                num = [K/(w0**2),0,0]

        tf = lti(num,den)
        return tf

    def get_context_data(self):
        extra = {"order": self.order,
                 "type" : self.type,
                 "params" : self.params
                }
        return extra

    def plot(self,type,params=None):

        if type == "zpk":
            data = self.zpk()

        if type == "step":
            if params :
                low = params["low"]
                high = params["high"]
                T = np.linspace(low,high,300)
            else :
                T = None
            data = self.step(T=T)

        if type == "bode":
            if params :
                low = params["low"]
                high = params["high"]
                w = np.logspace(low,high,300)
            else :
                w = None

            data = self.bode(w=w)
        
        return data

    def zpk(self):

        poles = self.lti.poles
        zeros = self.lti.zeros
        data = {
                "poles":
                {  "real": np.real(poles).tolist(),
                   "imag": np.imag(poles).tolist()
                },
                "zeros":
                {
                    "real": np.real(zeros).tolist(),
                    "imag": np.imag(zeros).tolist()
                },
                "extra": self.get_context_data()
        }
        return data


    def step(self,T=None):

        t,s = self.lti.step(T=T)
        data = {
                "type" : "step",
                "t":t.tolist(),
                "s":s.tolist(),
                "extra": self.get_context_data()
                }

        return data

    def bode(self,w=None,deg=True):
        w, Hjw = self.lti.freqresp(w=w)
        abs = np.abs(Hjw)
        phase = np.angle(Hjw)

        if deg == True:
            phase = phase*180/np.pi

        data = {
                "type" : "bode",
                "w":w.tolist(),
                "abs":abs.tolist(),
                "phase":phase.tolist(),
                "extra": self.get_context_data()
                }
        
        return data
