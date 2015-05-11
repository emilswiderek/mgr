__author__ = 'emil'
import generator.helper as hp
from generator.generator import Generator

class HeartGenerator(Generator):
    breathFunction = []
    responseFunction = False
    breathPhase = 0

    def __init__(self):
        Generator.__init__(self)
        self.phase_transition_curve = []

    def generate(self):
        """
        :return: heart phase
        """
        if self.phase_iterator == -1:  # On initialisation both oscillators have phase 0
            self.phase_iterator = 0
            return 0

        if self.breathPhase == hp.take_breath_in_phase:
            old_phase = self.phase_iterator
            self.phase_iterator += self.responseFunction.getResponse(self.phase_iterator)
            self.phase_transition_curve.append({old_phase: self.phase_iterator})
        else:
            self.phase_iterator += 1

        if self.phase_iterator >= hp.heart_period:
                self.phase_iterator = 0

        return self.phase_iterator

    def generateProcess(self):
        for x in range(0, hp.breath_period*hp.number_of_breaths):
            self.breathPhase = self.breathFunction[x]
            self.process.append(self.generate())
        return self.process, self.phase_transition_curve

    def setBreathFunction(self, breathFunction):
        self.breathFunction = breathFunction

    def setResponseFunction(self, responseFunction):
        self.responseFunction = responseFunction