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
        analysis.setResultsModel()

        print("Restults analysis for "+str(hp.response_function))

        ExtortionAnalyzer = ExtortionSpectrumAnalyzer()

        ExtortionAnalyzer.analyze(analysis)
        del analysis
        del ExtortionAnalyzer

        return

#multi generation happens here:

responseFunctions = ['sinus', 'forwarding', 'akselrod', 'halfSinus']  # halfSinus

hp.set_show_plots(False)
hp.set_min_breath_period(10)
hp.set_max_breath_period(700)

for resp in responseFunctions:
    hp.set_response_function(resp)
    #for bp in [[100, 300], [300, 600], [600, 900], [900, 1200], [1200, 1500]]:
    #hp.set_min_breath_period(bp[0])
    #hp.set_max_breath_period(bp[1])
    #hp.set_min_breath_period(100)
    #hp.set_max_breath_period(1200)
    run(MeasureModel.TYPE_ANALYZE_EXTORTION)
    #hp.set_min_breath_period(10)
    #hp.set_max_breath_period(700)
