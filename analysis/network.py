__author__ = 'emil'
import neurolab as nl
import helpers.helper as hp
import numpy as np
from generator.heart_gen import HeartGenerator
from analysis.plotter import Plotter
from model.MeasureModel import MeasureModel


class Network():
    OUTPUT_NUMBER_OF_POINTS = 10
    NUMBER_OF_NEURONS = 50
    LEARNING_RESPONSE_FUNCTIONS = ['sinus', 'forwarding', 'akselrod', 'halfSinus']
    TESTING_RESPONSE_FUNCTIONS = ['sinus2', 'akselrodian', 'halfSinus2', 'forwarding2']

    def __init__(self):
        """
        inicjalizacja sieci...
        :return:
        """
        self.network = None

    def trainNetwork(self):
        """
        Neurolab doesnt work like it should
        # How can i provide many training samples for it

        :param input:
        :return:
        """
        output = self.prepareExpectedOutput()

        trainingSample = None
        target = np.ndarray(shape=(len(self.LEARNING_RESPONSE_FUNCTIONS), self.OUTPUT_NUMBER_OF_POINTS))
        counter = 0
        for respF in self.LEARNING_RESPONSE_FUNCTIONS:
            measure = MeasureModel()
            measure.where([('measure_type', MeasureModel.TYPE_ANALYZE_EXTORTION, '='), ('response_function', respF, '=')])
            measure.load()
            measure.loadResults()
            if trainingSample is None:
                trainingSample = np.ndarray(shape=(len(self.LEARNING_RESPONSE_FUNCTIONS), len(measure.results.stdev)))
            trainingSample[counter] = measure.results.stdev  # results for one learning set
            target[counter] = output[respF]  # target for one learning set
            counter += 1

        mi = trainingSample.min()
        ma = trainingSample.max()
        self.network = nl.net.newff([[mi, ma]]*len(trainingSample[0]), [self.NUMBER_OF_NEURONS, self.OUTPUT_NUMBER_OF_POINTS])
        self.network.trainf = nl.train.train_gd
        self.network.train(trainingSample, target, goal=0.0001)  #  @todo check what happens here? tranposed????

        return True

    def prepareExpectedOutput(self):
        # remember to normalise

        hg = HeartGenerator()
        #  points of x axis (not normalised!)
        x = np.linspace(0, hp.heart_period, self.OUTPUT_NUMBER_OF_POINTS)
        output = {}

        for respFun in self.LEARNING_RESPONSE_FUNCTIONS:
            response_function = hg.getResponseFunction(respFun)
            output[respFun] = []
            for i in x:
                output[respFun].append(response_function.getResponse(i))

        output['x'] = x.astype(float)/float(hp.heart_period)
        return output

    def getResults(self, responseFunction):
        measure = MeasureModel()
        measure.where([('measure_type', MeasureModel.TYPE_ANALYZE_EXTORTION, '='), ('response_function', responseFunction, '=')])
        measure.load()
        measure.loadResults()
        inp = np.array(measure.results.stdev)
        return self.network.sim(inp.reshape(1, len(measure.results.stdev)))