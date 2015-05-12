__author__ = 'emil'
import generator.helper as hp
import numpy as np


class PhaseDifferences():

    def analyze(self, breath, heart):
        snapshots = []
        next_step = []
        ar = np.array(breath)
        indexes = np.where(ar == hp.take_breath_in_phase)
        for x in indexes[0]:
            snapshots.append(heart[x]/hp.heart_period)
            if x+1 < len(heart):
                next_step.append(heart[x+1]/hp.heart_period)
        return indexes[0], snapshots, next_step