__author__ = 'emil'
import math

from responseFunction.responseFunction import ResponseFunction
import helpers.helper as hp


class SinusFunction(ResponseFunction):
    max_amplitude = 0.3

    def getResponse(self, phase):
        global max_amplitude
        return self.max_amplitude*math.sin((phase/hp.heart_period)*math.pi*2)