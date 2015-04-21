__author__ = 'emil'
from responseFunction.responseFunction import ResponseFunction
import generator.helper as hp


class ForwardingFunction(ResponseFunction):
    def getResponse(self, phase):
        return (phase + 4) % hp.steps_in_phase