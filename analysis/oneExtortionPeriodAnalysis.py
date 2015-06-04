from generator.dataStorage import DataStorage

__author__ = 'emil'

import numpy as np
from generator import helper as hp
from analysis.phaseDifferences import PhaseDifferences
from analysis.plotter import Plotter


class Analyzer:
    def __init__(self, breath, heart):
        """
        :param breath: []
        :param heart: []
        :return:
        """
        self.breath = breath
        self.heart = heart
        self.bind = self.bind_breath_and_heart(breath, heart)

    def bind_breath_and_heart(self, breath, heart):
        """
        Creates numpy ndarray of the breath and heart results
        for further analysis

        :param breath:
        :param heart:
        :return:
        """
        bind = np.ndarray(shape=(3, len(breath)))

        for x in range(0, len(breath)):
            bind[0][x] = x / hp.breath_period
            bind[1][x] = breath[x] / hp.breath_period
            bind[2][x] = heart[x] / hp.heart_period
        return bind

    def analyze(self):
        phaseAnalyzer = PhaseDifferences()

        storage = DataStorage()

        indexes, results, previous_step = phaseAnalyzer.analyze(self.breath, self.heart)

        plotter = Plotter()

        # Mapa powrotu:
        storage.set_filename(str(hp.T_to_T0)+"_map.json")
        storage.store({'previous_step': previous_step, 'next_step': results})
        plotter.map(previous_step, results)

        # Faza rytmu serca:
        plotter.heart_rate(self.bind[0], self.bind[2])

        # Faza rytmu serca i oddechu:
        plotter.heart_and_breath_rate(self.bind[0], self.bind[1], self.bind[2])

        #Faza rytmu serca w momencie wystąpienia oddechu
        plotter.heart_when_breath(indexes, previous_step)