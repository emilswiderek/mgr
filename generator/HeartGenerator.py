from responseFunction.Akselrod import Akselrod
from responseFunction.forwardingFunction import ForwardingFunction
from responseFunction.sinusFunction import SinusFunction
import helpers.helper as hp
from generator.Generator import Generator
from responseFunction.halfSinusFunction import HalfSinusFunction
from responseFunction.testingSample.AkselrodianFunction import Akselrodian
from responseFunction.testingSample.SinusFunction2 import SinusFunction2
from responseFunction.testingSample.HalfSinusFunction2 import HalfSinusFunction2
from responseFunction.testingSample.ForwardingFunction2 import ForwardingFunction2
from responseFunction.AkselrodBisFunction import AkselrodBisFunction
from responseFunction.CosinusFunction import CosinusFunction
from responseFunction.HalfSinusBisFunction import HalfSinusBisFunction
from responseFunction.ForwardingBisFunction import ForwardingBisFunction


class HeartGenerator(Generator):
    breathFunction = []
    responseFunction = False
    breathPhase = 0

    def generate(self):
        """
        :return: heart phase
        """
        if self.phase_iterator == -1:  # On initialisation both oscillators have phase 0
            self.phase_iterator = 0
            return 0

        if self.breathPhase == hp.take_breath_in_phase:
            self.phase_iterator += self.responseFunction.getResponse(self.phase_iterator)*hp.heart_period
        else:
            self.phase_iterator += 1

        if self.phase_iterator >= hp.heart_period:
                self.phase_iterator = 0

        return self.phase_iterator

    def generateProcess(self):

        self.process = []

        for x in range(0, hp.breath_period*hp.number_of_breaths):
            self.breathPhase = self.breathFunction[x]
            self.process.append(self.generate())
        return self.process

    def setBreathFunction(self, breathFunction):
        self.breathFunction = breathFunction

    def setResponseFunction(self, responseFunction):
        self.responseFunction = responseFunction

    def getResponseFunction(self, name):
        return {
            'forwarding': ForwardingFunction(),
            'sinus': SinusFunction(),
            'akselrod': Akselrod(),
            'halfSinus': HalfSinusFunction(),
            'sinus2': SinusFunction2(),
            'akselrodian': Akselrodian(),
            'halfSinus2': HalfSinusFunction2(),
            'forwarding2': ForwardingFunction2(),
            'forwardingBis': ForwardingBisFunction(),
            'cosinus': CosinusFunction(),
            'akselrodBis':AkselrodBisFunction(),
            'halfSinusBis':HalfSinusBisFunction()
        }[name]