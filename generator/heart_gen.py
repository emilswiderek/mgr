__author__ = 'emil'
import generator.helper as hp
from generator.generator import Generator


class HeartGenerator(Generator):
    breathFunction = []
    responseFunction = False

    def generate(self, breathPhase):
        """
        :return: heart phase
        """
        if(breathPhase == hp.take_breath_in_phase):
            self.phase_iterator = self.responseFunction.getResponse(self.phase_iterator)
        else:
            self.phase_iterator = (self.phase_iterator + 1) % hp.steps_in_phase

        return self.phase_iterator

    def generateProcess(self):
        for x in self.breathFunction:
            self.process.append(self.generate(x))
        return self.process

    def setBreathFunction(self, breathFunction):
        self.breathFunction = breathFunction

    def setResponseFunction(self, responseFunction):
        self.responseFunction = responseFunction