from responseFunction.Akselrod import Akselrod
from responseFunction.forwardingFunction import ForwardingFunction
from responseFunction.sinusFunction import SinusFunction
import helpers.helper as hp
from generator.generator import Generator
from responseFunction.halfSinusFunction import HalfSinusFunction


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

        process = []

        for x in range(0, hp.breath_period*hp.number_of_breaths):
            self.breathPhase = self.breathFunction[x]
            process.append(self.generate())
        return process

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
        }[name]