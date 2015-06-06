__author__ = 'emil'
import numpy as np

import helpers.helper as hp


class PhaseDifferences():

    def analyze(self, breath, heart):
        """

        :param breath:
        :param heart:
        :return: Timesteps, heart_phase_after, heart_phase_before
        """
        snapshots = []
        previous_step = []
        ar = np.array(breath)
        indexes = np.where(ar == hp.take_breath_in_phase)
        for x in indexes[0]:
            snapshots.append(heart[x]/hp.heart_period)
            if x-1 > 0:
                previous_step.append(heart[x-1]/hp.heart_period)
            else:
                previous_step.append(0)
        return indexes[0]/hp.breath_period, snapshots, previous_step