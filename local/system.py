import numpy as np
from scipy.signal import lti
from pathlib import Path
import json

class TF():

    def __init__(self,num,den,name="sys"):
        self.num = num 
        self.den = den
        self.name = name

    @property
    def lti(self):
        return lti(self.num,self.den)

    def get_default_filename(self,type,filename=None):

        if filename == None:
            Path("../json/").mkdir(parents=True, exist_ok=True)
            filename = "../json/{}_{}.json".format(self.name,type)

        return filename

    def zpk(self,filename = None):

        poles = self.lti.poles
        zeros = self.lti.zeros
        data = { "poles":
                {  "real": np.real(poles).tolist(),
                   "imag": np.imag(poles).tolist()
                },
                "zeros":
                {
                    "real": np.real(zeros).tolist(),
                    "imag": np.imag(zeros).tolist()
                }
        }

        filename = self.get_default_filename("zpk",filename=filename)
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def step(self,filename=None,T=None):

        t,s = self.lti.step(T=T)
        data = {"t":t.tolist(),"s":s.tolist()}

        filename = self.get_default_filename("step",filename=filename)
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def bode(self,filename=None,w=None,deg=True):
        w, Hjw = self.lti.freqresp(w=w)
        abs = np.abs(Hjw)
        phase = np.angle(Hjw)

        if deg == True:
            phase = phase*180/np.pi

        data = {"w":w.tolist(),"abs":abs.tolist(),"phase":phase.tolist()}
        
        filename = self.get_default_filename("bode",filename=filename)
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

