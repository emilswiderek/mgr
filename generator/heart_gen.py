__author__ = 'emil'
import generator.helper as hp


class HeartGenerator() :
    phase_iterator = 0
    def generate(self, breath_phase):
        """
        :return: heart phase
        """
        yield (self.phase_iterator+1)%hp.steps_in_phase