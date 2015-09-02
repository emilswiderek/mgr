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
from analysis.plotter import Plotter


import pprint

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

        print("Restults analysis for "+str(hp.response_function))

        ExtortionAnalyzer = ExtortionSpectrumAnalyzer()

        ExtortionAnalyzer.analyze(analysis)
        del analysis
        del ExtortionAnalyzer

        return

    def multiGen():
        #multi generation happens here:

        responseFunctions = ['sinus2', 'forwarding2', 'akselrodian', 'halfSinus2']
        # test cases: 'sinus2', 'forwarding2', 'akselrodian', 'halfSinus2'
        # learning cases: 'sinus', 'forwarding', 'akselrod', 'halfSinus'
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

net = Network()
net.loadNetwork(True)  # load best network

plt = Plotter()
output = net.prepareExpectedOutput(False)  # expected output for testing series

for respF in Network.TESTING_RESPONSE_FUNCTIONS:
    out = net.getResults(respF)
    plt.test_plot_network_result(out[0], output[respF], output['x'])
net.saveNetwork()