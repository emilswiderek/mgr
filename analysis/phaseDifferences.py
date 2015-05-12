__author__ = 'emil'
import generator.helper as hp
import numpy as np


class PhaseDifferences():

    def analyze(self, breath, heart):
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
        return indexes[0], snapshots, previous_step