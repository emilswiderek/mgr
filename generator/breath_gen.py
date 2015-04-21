import generator.helper as hp
import numpy as np
from generator.generator import Generator

class BreathGenerator(Generator):

    def generate(self):
        """
        :return: breath phase
        """
        if self.phase_iterator == -1:  # On initialisation both oscillators have phase 0
            self.phase_iterator = 0.0
            return 0.0

        self.phase_iterator = (self.phase_iterator + self.generation_step)
        if self.phase_iterator >= self.generation_step*hp.steps_in_phase:
            self.phase_iterator = 0.0
        return self.phase_iterator

    def generateProcess(self):
        for x in np.arange(0, hp.steps_in_phase, self.generation_step):
            self.process.append(self.generate())
        return self.process