from responseFunction.responseFunction import ResponseFunction
import helpers.helper as hp


class Akselrod(ResponseFunction):

    def __init__(self):
        self.d = 0.09
        self.omega = 0.45
        self.a = 0.37

    def getResponse(self, phase):
        normalised_phase = phase/hp.heart_period
        if self.omega > normalised_phase:
            return (self.d/self.omega) * normalised_phase
        else:
            return (self.a/(1.-self.omega))*(normalised_phase - 1.)