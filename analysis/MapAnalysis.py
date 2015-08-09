__author__ = 'emil'
import numpy as np

import helpers.helper as hp
from analysis.plotter import Plotter
from generator.heart_gen import HeartGenerator
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

    def fit_polynomial(self, map):
        """
        fits the polynomial and returns
        :param map:
        :return:
        """
        fit = np.polyfit(map['previous_step'], map['next_step'], hp.map_fitting_degree)
        y = np.polyval(fit, map['previous_step'])
        fitting_curve = np.zeros(shape=(2, len(map['previous_step'])), )

        for i in range(0, len(map['previous_step'])):
            fitting_curve[0][i] = map['previous_step'][i]
            fitting_curve[1][i] = y[i]

        return fitting_curve, fit

    def divide_by_x(self, fitted):
        result = np.zeros(shape=(len(fitted[0]), 1))
        for i in range(0, len(fitted[0])):
            if fitted[0][i] == 0:
                result[i] = 0
            else:
                result[i] = fitted[1][i] / fitted[0][i] - fitted[0][i]
        return fitted[0], result - np.mean(result)

    def get_response_function_spectrum(self, map):
        heart_gen = HeartGenerator()
        response_function = heart_gen.getResponseFunction(hp.response_function)
        spectrum = map['previous_step']
        spectrum_response = []

        for x in spectrum:
            spectrum_response.append(response_function.getResponse(x * hp.heart_period))

        return spectrum, spectrum_response

    def map_division(self, map):
        result = []
        for i in range(0, len(map['previous_step'])):
            if (map['previous_step'][i] == 0.):
                result.append(0.)
            else:
                result.append(map['next_step'][i] / map['previous_step'][i])

        return map['previous_step'], result - np.mean(result)