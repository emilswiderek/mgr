__author__ = 'emil'
from responseFunction.responseFunction import ResponseFunction
import generator.helper as hp
import math

class SinusFunction(ResponseFunction):
    max_amplitude = 0.2

    def getResponse(self, phase):
        global max_amplitude
        return phase + self.max_amplitude*math.sin(phase)