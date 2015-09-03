import math

from responseFunction.responseFunction import ResponseFunction
import helpers.helper as hp


class CosinusFunction(ResponseFunction):
    max_amplitude = 0.6

    def getResponse(self, phase):
        global max_amplitude
        return self.max_amplitude*math.cos((phase/hp.heart_period)*math.pi*2)