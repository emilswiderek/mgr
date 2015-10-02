from analysis.MapAnalysis import MapAnalysis
from generator import main
from analysis.oneExtortionPeriodAnalysis import Analyzer
from generator.extortionSpectrum import ExtortionSpectrumGenerator
from analysis.extortionSpectrumAnalysis import ExtortionSpectrumAnalyzer
from helpers.dataStorage import DataStorage
from model.spectrumCollectionModel import SpectrumCollectionModel
from model.MeasureModel import MeasureModel
import helpers.helper as hp
import os
from model.HeartbeatsCollectionModel import HeartbeatsCollectionModel
from analysis.network import Network
from analysis.ploter import Plotter
from model.database import Database
import pprint
from vendor.tqdm.tqdm import *
import helpers.networkStorageHelper as nshp


# options:
# 'gen_ext' - generate extortion spectrum and save it in the storage file
# 'one_period' - generate and analyze data for one breath period


def run(option):

    if option == 'one_period':

        hp.set_one_period(True)

        print("Generowanie i analiza dla 1 okresu oddechu")

        # one period results:
        breath, heart = main.main()

        onePeriodAnalyzer = Analyzer(breath, heart)

        onePeriodAnalyzer.analyze()

        print("Analiza dla 1 okresu oddechu")

        storage = DataStorage()

        #map analysis:
        storage.set_filename("map.json")
        map = storage.load()

        mapAnalysis = MapAnalysis()
        mapAnalysis.analyze(map)

        return

    elif option == MeasureModel.TYPE_GENERATE_EXTORTION:

        hp.set_one_period(False)

        print("---- Generating "+str(hp.response_function)+" min: "+str(hp.min_breath_period)+" max: "+str(hp.max_breath_period)+"---- \n\r")

        # results for different extortion periods:

        Generator = ExtortionSpectrumGenerator()

        Generator.generate()

        return

    elif option == MeasureModel.TYPE_ANALYZE_EXTORTION:  # analyze_ext

        hp.set_one_period(False)

        # we are selecting one measure in db:
        analysis = MeasureModel()  # 1 analysis measure = many generation measures
        analysis.setMaxBreathPeriod(hp.max_breath_period)
        analysis.setMinBreathPeriod(hp.min_breath_period)
        analysis.setResponseFunction(hp.response_function)
        analysis.setBreathNumber(hp.number_of_breaths)
        analysis.setMeasureType(MeasureModel.TYPE_ANALYZE_EXTORTION)
        analysis.setHeartPeriod(hp.heart_period)
        analysis.setResultsModel()

        print("Results analysis for "+str(hp.response_function))

        ExtortionAnalyzer = ExtortionSpectrumAnalyzer()

        ExtortionAnalyzer.analyze(analysis)
        del analysis
        del ExtortionAnalyzer

        return

    elif option == "analyze_one_measure":
        hp.set_one_period(True)
        analysis = MeasureModel()  # 1 analysis measure = many generation measures
        analysis.where([('id', 15185, '=')]) # id 9532
        analysis.load()
        analysis.results.order("id", "ASC")
        analysis.loadResults()
        # for plotter:
        hp.set_breath_period(analysis.breath_period)
        hp.set_heart_period(analysis.heart_period)
        hp.set_response_function(analysis.response_function)
        hp.set_show_plots(False)
        hp.calculateTtoT0()

        print("Okres oddechu: "+str(hp.breath_period))
        print("Okres rytmu serca: "+str(hp.heart_period))
        print("Results analysis for "+str(analysis.response_function))

        onePeriodAnalyzer = Analyzer(analysis.results.breath_phase, analysis.results.heart_phase)

        onePeriodAnalyzer.analyze()

        return

def multiGen():
    #multi generation happens here:

    responseFunctions = ['sinus', 'forwarding', 'akselrod', 'halfSinus', 'forwardingBis', 'cosinus', 'akselrodBis', 'halfSinusBis']
    # test cases: 'sinus2', 'forwarding2', 'akselrodian', 'halfSinus2'
    # learning cases: 'sinus', 'forwarding', 'akselrod', 'halfSinus','forwardingBis', 'cosinus','akselrodBis','halfSinusBis'
    hp.set_show_plots(False)
    hp.set_min_breath_period(10)
    hp.set_max_breath_period(1200)
    hp.set_heart_period(200)

    for resp in responseFunctions:
        hp.set_response_function(resp)
        run(MeasureModel.TYPE_GENERATE_EXTORTION)

    for resp in responseFunctions:
        hp.set_response_function(resp)
        run(MeasureModel.TYPE_ANALYZE_EXTORTION)


def networkTest(best=False, learningSample=False, filename=None):
    """
    Performs a network simulation for testing results
    :param best:
    :param learningSample:
    :return:
    """
    net = Network()
    net.loadNetwork(best, filename)  # load best network

    plt = Plotter()
    plt.show = False
    output = net.prepareExpectedOutput(learningSample)  # learning = True

    if learningSample:
        sample = Network.LEARNING_RESPONSE_FUNCTIONS
    else:
        sample = Network.TESTING_RESPONSE_FUNCTIONS

    for respF in sample:
        out = net.getResults(respF)
        plt.test_plot_network_result(out[0], output[respF], output['x'], "", respF)


def networkLearnAndTest(neurons):
    net = Network()
    net.setNumberOfNeurons(neurons)
    #print("Network number of neurons: "+str(net.NUMBER_OF_NEURONS))

    net.trainNetwork()

    #plt = Plotter()
    #output = net.prepareExpectedOutput()  # expected output for testing series

    for respF in Network.LEARNING_RESPONSE_FUNCTIONS:
        out = net.getResults(respF)
        #plt.test_plot_network_result(out[0], output[respF], output['x'])


    #print("Test results:")
    output = net.prepareExpectedOutput(False)

    dist = 0.0
    dist_from_prev = 0.0
    prev_out = None
    for respFunc in Network.TESTING_RESPONSE_FUNCTIONS:
        out = net.getResults(respFunc)

        for i in range(0, net.OUTPUT_NUMBER_OF_POINTS):
            dist += abs(out[0][i] - output['sinus2'][i])
            if prev_out is not None:
                dist_from_prev += abs(out[0][i] - prev_out[0][i])
            prev_out = out

    print("Result distance from test results: "+str(dist)+" prv: "+str(dist_from_prev))

    return dist, dist_from_prev, net


def runNetwork(neurons):
    print("net_ep"+str(hp.train_epochs)+"_g"+str(hp.train_goal)+"_lr"+str(hp.train_lr)+"_a"+str(hp.train_adapt)+"_lr_inc"+str(hp.train_lr_inc)+"_lr_dec"+str(hp.train_lr_dec)+"_mxpi"+str(hp.train_max_perf_inc))
    counter = 0
    bestResults = []

    while counter < 10:
        dist, dist_from_prev, net = networkLearnAndTest(neurons)
        if dist <= 8.0 and dist_from_prev > 0.13:
            print('Added: dist: '+str(dist)+" dist prev: "+str(dist_from_prev)+" neur: "+str(neurons))
            bestResults.append({'dist': dist, 'dist_from_prev': dist_from_prev, 'net': net, 'neurons': neurons})
        counter += 1

    print(bestResults)

    print("Ready, analysing results...")
    bestId = 0
    bestDist = 999999999
    bestDistPrv = 0.0

    cc = 0
    for result in tqdm(bestResults):
        if bestDist > result['dist'] and bestDistPrv < result['dist_from_prev']:
            bestDist = result['dist']
            bestId = cc
        cc += 1

    if bestId == 0:
        return False

    net = bestResults[bestId]['net']
    filename = "net_ep"+str(hp.train_epochs)+"_g"+str(hp.train_goal)+"_lr"+str(hp.train_lr)+"_a"+str(hp.train_adapt)+"_lr_inc"+str(hp.train_lr_inc)+"_lr_dec"+str(hp.train_lr_dec)+"_mxpi"+str(hp.train_max_perf_inc)+".net"
    nshp.init_results_subfolder()
    net.saveNetwork(nshp.get_storage_path()+filename)

    networkTest(False, False, nshp.get_storage_path()+filename)


run("analyze_one_measure")
exit(1)

#v3

hp.train_show = 0
for goal in tqdm([0.000001]):
    hp.train_goal = goal
    for lr in [0.01, 0.001, 0.0001, 0.00001, 0.000001]:
        hp.train_lr = lr
        for lr_inc in [1.01, 1.001, 1.0001, 1.02, 1.021, 1.25, 1.3, 1.4, 1.5]:
            hp.train_lr_inc = lr_inc
            for lr_dec in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                hp.train_lr_dec = lr_dec
                for max_perf_inc in [1.0, 1.01, 1.02, 1.03, 1.04, 1.045, 1.05, 1.06, 1.1, 1.4, 1.5]:
                    hp.train_max_perf_inc = max_perf_inc
                    for neurons in range(40, 60):
                        runNetwork(neurons)
exit(1)
    # v1
hp.train_show = 0
for goal in tqdm([0.01]):
    hp.train_goal = goal
    for lr in [0.01, 0.001, 0.0001, 0.00001, 0.000001]:
        hp.train_lr = lr
        for lr_inc in [1.01, 1.001, 1.0001, 1.02, 1.021, 1.25, 1.3, 1.4, 1.5]:
            hp.train_lr_inc = lr_inc
            for lr_dec in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                hp.train_lr_dec = lr_dec
                for max_perf_inc in [1.02, 1.03, 1.04, 1.045, 1.05, 1.06, 1.1, 1.4, 1.5]:
                    hp.train_max_perf_inc = max_perf_inc
                    for neurons in range(40, 60):
                        runNetwork(neurons)
# v1
hp.train_show = 0
for goal in tqdm([0.001]):
    hp.train_goal = goal
    for lr in [0.01, 0.001, 0.0001, 0.00001, 0.000001]:
        hp.train_lr = lr
        for lr_inc in [1.01, 1.001, 1.0001, 1.02, 1.021, 1.25, 1.3, 1.4, 1.5]:
            hp.train_lr_inc = lr_inc
            for lr_dec in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                hp.train_lr_dec = lr_dec
                for max_perf_inc in [1.02, 1.03, 1.04, 1.045, 1.05, 1.06, 1.1, 1.4, 1.5]:
                    hp.train_max_perf_inc = max_perf_inc
                    for neurons in range(40, 60):
                        runNetwork(neurons)
exit(1)