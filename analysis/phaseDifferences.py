__author__ = 'emil'
import generator.helper as hp
import numpy as np


class PhaseDifferences():

    def analyze(self, breath, heart):
        snapshots = []
        ar = np.array(breath)
        indexes = np.where(ar == hp.take_breath_in_phase)
        for x in indexes[0]:
            snapshots.append(heart[x])
        return indexes[0], snapshots