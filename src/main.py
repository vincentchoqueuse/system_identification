from system import TF
import numpy as np
import json


tf = TF([1],[3,1],name="system1")
tf.step()
tf.bode(w=np.logspace(-2,1))
tf.zpk()