__author__ = 'emil'
import numpy as np

import helpers.helper as hp
from analysis.plotter import Plotter
from generator.HeartGenerator import HeartGenerator
from helpers.dataStorage import DataStorage


class MapAnalysis():
    """
    Class for analyzing heart phase map

    """
    def analyze(self, map):
        """

        :param map:
        :return:
        """
        result = list()
        hg = HeartGenerator()
        responseFunction = hg.getResponseFunction(hp.response_function)
        responseResult = list()
        for i in range(0, len(map['previous_step'])):
            result.append(map['next_step'][i] - map['previous_step'][i])
            responseResult.append(responseFunction.getResponse(map['previous_step'][i]*hp.heart_period))#because of normalisation happening inside of the function


        plotter = Plotter()
        plotter.plot_response_function_from_map(result, map, responseResult)