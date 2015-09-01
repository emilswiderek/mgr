__author__ = 'emil'
import neurolab as nl
import helpers.helper as hp
import numpy as np
from generator.heart_gen import HeartGenerator
from analysis.plotter import Plotter
from model.MeasureModel import MeasureModel


class Network():
    OUTPUT_NUMBER_OF_POINTS = 10
    LEARNING_RESPONSE_FUNCTIONS = ['sinus', 'forwarding', 'akselrod', 'halfSinus']
    TESTING_RESPONSE_FUNCTIONS = ['sinus2', 'akselrodian', 'halfSinus2', 'forwarding2']

    def __init__(self):
        """
        inicjalizacja sieci...
        :return:
        """
        self.network = None

    def trainNetwork(self, input):
        """
        Ćwiczenie sieci...
        :param input:
        :return:
        """
        output = self.prepareExpectedOutput()
        #print(output) # todo change library??? - check input as array
        #plt = Plotter()
        #plt.plot_learning_output(output, 'sinus')

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
            trainingSample[counter] = measure.results.stdev
            target[counter] = output[respF]
            counter += 1

        #print(trainingSample)
       # inp = trainingSample.reshape(len(trainingSample[0]), 1) # try without reshaping and then check
       # print(inp)
        mi = trainingSample.min()
        ma = trainingSample.max()
        self.network = nl.net.newff([[mi, ma]]*len(trainingSample[0]), [200, self.OUTPUT_NUMBER_OF_POINTS])
        self.network.trainf = nl.train.train_gd
        self.network.train(trainingSample, target)  #  @todo check what happens here?

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
                output[respFun].append(response_function.getResponse(i)/hp.heart_period)

        output['x'] = x.astype(float)/float(hp.heart_period)
        return output