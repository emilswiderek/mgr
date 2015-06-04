__author__ = 'emil'
import numpy as np

class MapAnalysis():
    """
    Class for analyzing heart phase map

    """
    def analyze(self, map):
        fit = np.polyfit(map['previous_step'], map['next_step'], 5)
        print(fit)
        pass