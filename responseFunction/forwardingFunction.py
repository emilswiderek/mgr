__author__ = 'emil'
from responseFunction.responseFunction import ResponseFunction


class ForwardingFunction(ResponseFunction):

    def __init__(self):
        self.forward_step = 4

    def getResponse(self, phase):
        return self.forward_step