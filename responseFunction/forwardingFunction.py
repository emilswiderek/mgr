__author__ = 'emil'
from responseFunction.responseFunction import ResponseFunction
import generator.helper as hp


class ForwardingFunction(ResponseFunction):

    def __init__(self):
        self.forward_step = 4/hp.steps_in_phase

    def getResponse(self, phase):
        return phase + self.forward_step