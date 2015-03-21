__author__ = 'emil'
import generator.helper as hp


class BreathGenerator() :
    phase_iterator = 0
    def generate(self):
        """
        :return: breath phase
        """
        yield (self.phase_iterator+1)%hp.steps_in_phase