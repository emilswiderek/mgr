import statistics

import numpy as np

from helpers import helper as hp
from analysis.plotter import Plotter
from model.MeasureModel import MeasureModel
from vendor.tqdm.tqdm import *


class ExtortionSpectrumAnalyzer:

    def analyze(self, analysis):
        """

        :param measure: MeasureModel
        :return:
        """
        if not isinstance(analysis, MeasureModel):
            raise Exception("Analysis error, wrong input")

        for breath_period in tqdm(range(analysis.min_breath_period, analysis.max_breath_period)):
            measure = MeasureModel()
            measure.limit(1)
            measure.offset(0)
            measure.order('id', 'ASC')
            measure.where([('measure_type', MeasureModel.TYPE_GENERATE_EXTORTION, '='), ('breath_period', breath_period, '='), ('response_function', analysis.response_function, '=')])
            measure.load()

            measure.loadResults()
            analysis.results.breath_period.append(measure.breath_period)
            mean, sd = self.analyze_step(measure.results.heart_phase)
            del measure
            analysis.results.stdev.append(sd)
            analysis.results.mean_rr.append(mean)

        analysis.saveAll()
        del analysis
        #plt = Plotter()
        #plt.plot_rr_sd(analysisMeasure.results.breath_period, analysisMeasure.results.mean_rr, analysisMeasure.results.stdev)

        #return analysis

    def analyze_step(self, heart):
        #plt.plot(heart)
        #plt.show()
        ar = np.array(heart)
        indexes = np.where(ar.astype(int) == hp.take_breath_in_phase)
        rr = []

        for element in range(0, len(indexes[0]) - 1):
            rr.append(indexes[0][element + 1] - indexes[0][element])

        return statistics.mean(rr), statistics.stdev(rr)

    def analyze_sql(self, measure):
        """

        SELECT
            *
        FROM mgr.generation_results al
        INNER JOIN mgr.generation_results al2
            on (al.result_id = al2.result_id + 1 AND
                al2.response_function = 'sinus'
                AND al2.heart_period = 40
                AND al2.breath_period BETWEEN 100 AND 1500
            )
        WHERE
                al.response_function = 'sinus'
                AND al.heart_period = 40
                AND al.breath_period BETWEEN 100 AND 1500
        ;
        :param measure:
        :return:
        """
        pass  # @todo instead of entire analyze make sql, so this will happen in database