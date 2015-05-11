from responseFunction.responseFunction import ResponseFunction
import generator.helper as hp

class Akselrod(ResponseFunction):

    def __init__(self):
        self.forward_percentage = 0.1
        self.backward_percentage = 0.4

    def getResponse(self, phase):
        if hp.heart_period/2 > phase:
            return self.forward_percentage * phase
        else:
            return - self.backward_percentage * phase