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
        if self.phase_iterator == -1:  # On initialisation both oscillators have phase 0
            self.phase_iterator = 0.1
            return 0.1

        if breathPhase == hp.take_breath_in_phase:
            self.phase_iterator = self.responseFunction.getResponse(self.phase_iterator)
        else:
            self.phase_iterator = self.phase_iterator + self.generation_step

        if self.phase_iterator >= self.generation_step*hp.steps_in_phase:
                self.phase_iterator = 0.0

        return self.phase_iterator

    def generateProcess(self):
        for x in self.breathFunction:
            self.process.append(self.generate(x))
        return self.process

    def setBreathFunction(self, breathFunction):
        self.breathFunction = breathFunction

    def setResponseFunction(self, responseFunction):
        self.responseFunction = responseFunction