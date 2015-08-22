import helpers.helper as hp
from generator.generator import Generator


class BreathGenerator(Generator):

    def generate(self):
        """
        :return: breath phase
        """
        if self.phase_iterator == -1:  # On initialisation both oscillators have phase 0
            self.phase_iterator = 0
            return 0

        self.phase_iterator += 1
        if self.phase_iterator >= hp.breath_period:
            self.phase_iterator = 0
        return self.phase_iterator

    def generateProcess(self):

        del self.process
        self.__init__()

        for x in range(0, hp.breath_period*hp.number_of_breaths):
            self.process.append(self.generate())
        return self.process