__author__ = 'emil'
import neurolab as nl
import helpers.helper as hp
import numpy as np
from generator.HeartGenerator import HeartGenerator
from analysis.plotter import Plotter
from model.MeasureModel import MeasureModel
import math


class Network():
    OUTPUT_NUMBER_OF_POINTS = 10
    NUMBER_OF_NEURONS = 50
    LEARNING_RESPONSE_FUNCTIONS = ['sinus', 'forwarding', 'akselrod', 'halfSinus','forwardingBis', 'cosinus', 'akselrodBis', 'halfSinusBis']
    TESTING_RESPONSE_FUNCTIONS = ['sinus2', 'akselrodian', 'halfSinus2', 'forwarding2']
    NETWORK_SAVE_FILENAME = "network.net"
    NETWORK_BEST_FILENAME = "results/network_best.net"
    NETWORK_RETRAINING_CYCLES = 1
    NETWORK_TRAINING_EPSILON = 9.25

    def __init__(self):
        """
        inicjalizacja sieci...
        :return:
        """
        self.network = None
        #self.NUMBER_OF_NEURONS = int(math.sqrt(math.pow(1190, 2) + math.pow(self.OUTPUT_NUMBER_OF_POINTS, 2)))

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
        self.network.trainf = nl.train.train_gda
        for x in range(0, self.NETWORK_RETRAINING_CYCLES):
            error = self.network.train(trainingSample, target, goal=hp.train_goal, lr=hp.train_lr, adapt=hp.train_adapt, lr_inc=hp.train_lr_inc, lr_dec=hp.train_lr_dec, max_perf_inc=hp.train_max_perf_inc, show=hp.train_show)
            if error[-1] < self.NETWORK_TRAINING_EPSILON:
                break

        return True

    def prepareExpectedOutput(self, learning=True):
        # remember to normalise

        hg = HeartGenerator()
        #  points of x axis (not normalised!)
        x = np.linspace(0, hp.heart_period, self.OUTPUT_NUMBER_OF_POINTS)
        output = {}

        if learning:
            response_functions = self.LEARNING_RESPONSE_FUNCTIONS
        else:
            response_functions = self.TESTING_RESPONSE_FUNCTIONS

        for respFun in response_functions:
            response_function = hg.getResponseFunction(respFun)
            output[respFun] = []
            for i in x:
                output[respFun].append(response_function.getResponse(i))

        output['x'] = x.astype(float)/float(hp.heart_period)
        return output

    def getResults(self, responseFunction):
        """
        Gets the network results for provided responseFunction(name)

        NOTICE: Remember to train network first
        :param responseFunction:
        :return:
        """
        measure = MeasureModel()
        measure.where([('measure_type', MeasureModel.TYPE_ANALYZE_EXTORTION, '='), ('response_function', responseFunction, '=')])
        measure.load()
        measure.loadResults()
        inp = np.array(measure.results.stdev)
        return self.network.sim(inp.reshape(1, len(measure.results.stdev)))

    def saveNetwork(self, filename=None):
        """
        Saves network to file
        :return:
        """
        if filename is None:
            filename = self.NETWORK_SAVE_FILENAME

        self.network.save(filename)

    def loadNetwork(self, best=False, filename=None):
        """
        Loads network from file, best network is stored in other directory and is only readable
        :return:
        """
        if filename is None and best:
            filename = self.NETWORK_BEST_FILENAME
        elif filename is None and not best:
            filename = self.NETWORK_SAVE_FILENAME


        self.network = nl.load(filename)

    def setNumberOfNeurons(self, val):
        self.NUMBER_OF_NEURONS = val
        hp.network_number_of_neurons = val