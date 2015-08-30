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
            measure.where([('measure_type', MeasureModel.TYPE_GENERATE_EXTORTION, '='), ('breath_period', breath_period, '='), ('response_function', analysis.response_function, '='), ('heart_period', hp.heart_period, '=')])
            measure.load()

            analysis.results.breath_period.append(measure.breath_period)
            res = analysis.db.execute(self.analyze_sql(measure.id))
            analysis.results.mean_rr.append(res[0]['mean'])  # when insufficient results this will be 0
            analysis.results.stdev.append(res[0]['stdev'])


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
        if len(rr) < 2:
            return 0., 0.

        return statistics.mean(rr), statistics.stdev(rr)

    def analyze_sql(self, measureId):
        sql = """ SELECT
                    -- calculate mean and standard deviation for each measurement:
                        COALESCE(avg(result.diff), 0) as mean,
	                    COALESCE(std(result.diff), 0) as stdev
                    FROM
                        (
                        SELECT
                            -- distance between following heartbeats:
                            (diff.following_heartbeat_id - diff.id) as diff
                        FROM (
                            SELECT
                                *,
                                (
                                    -- id of the next heat beat
                                    SELECT
                                        al2.id
                                    FROM
                                        (
                                            -- extract all heartbeats
                                            SELECT
                                                *
                                            FROM
                                                mgr2.generation_results r
                                            WHERE
                                                r.heart_phase = """+str(hp.take_breath_in_phase)+"""
                                                and r.measure_id = """+str(measureId)+"""
                                            ORDER BY
                                                r.id ASC
                                        ) al2
                                    WHERE
                                        al2.id > al.id
                                    LIMIT 1
                                ) as following_heartbeat_id
                            FROM
                                (
                                    -- we extract all heartbeats
                                    SELECT
                                        *
                                    FROM
                                        mgr2.generation_results r
                                    WHERE
                                        r.heart_phase = """+str(hp.take_breath_in_phase)+"""
                                        and r.measure_id = """+str(measureId)+"""
                                    ORDER BY
                                        r.id ASC
                                ) al
                            ) diff
                            WHERE
                                -- last one is always null
                                diff.following_heartbeat_id IS NOT NULL
                        ) result
                    """
        return sql