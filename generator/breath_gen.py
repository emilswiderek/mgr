import generator.helper as hp
from generator.generator import Generator

class BreathGenerator(Generator):

    def generate(self):
        """
        :return: breath phase
        """
        self.phase_iterator = (self.phase_iterator + 1) % hp.steps_in_phase
        return self.phase_iterator

    def generateProcess(self):
        for x in range(0, hp.steps_in_phase * hp.number_of_breaths):
            self.process.append(self.generate())
        return self.process