import statistics

import numpy as np

from helpers import helper as hp
from analysis.plotter import Plotter


class ExtortionSpectrumAnalyzer:

    def analyze(self, results):
        # breath rate and standard deviation
        container = {'br': [], 'sd': [], 'av': []}
        for row in results:
            container['br'].append(int(row))
            mean, sd = self.analyze_step(results[row]['heart'])
            container['sd'].append(sd)
            container['av'].append(mean)

        plt = Plotter()
        plt.plot_rr_sd(container['br'], container['av'], container['sd'])

        return container

    def analyze_step(self, heart):
        #plt.plot(heart)
        #plt.show()
        ar = np.array(heart)
        indexes = np.where(ar.astype(int) == hp.take_breath_in_phase)
        rr = []

        for element in range(0, len(indexes[0]) - 1):
            rr.append(indexes[0][element + 1] - indexes[0][element])

        return statistics.mean(rr), statistics.stdev(rr)