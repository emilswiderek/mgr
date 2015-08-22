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

    elif option == 'gen_ext':

        hp.set_one_period(False)

        print("Generowanie "+str(hp.response_function)+" min: "+str(hp.min_breath_period)+" max: "+str(hp.max_breath_period))

        # results for different extortion periods:

        Generator = ExtortionSpectrumGenerator()

        results = Generator.generate()

        # @todo for results start here

        for i in range(0, len(results)):
            pprint.pprint(results)
            os._exit(1)
            measure = MeasureModel()
            measure.setHeartPeriod(hp.heart_period)
            measure.setMinBreathPeriod(hp.min_breath_period)
            measure.setResponseFunction(hp.response_function)
            measure.setMaxBreathPeriod(hp.max_breath_period)
            measure.setBreathNumber(hp.number_of_breaths)
            measure.setMeasureType('gen_ext')
            measureId = measure.save()

            heartbeats = HeartbeatsCollectionModel()
            heartbeats.setMeasureId(measureId)
            heartbeats.setHeartPhase(results[i]['heart'])
            id = heartbeats.save()

            print("Saved to database, measurement id:"+str(measureId)+" ")

        print("Zakończono")
        return

    else:  # analyze_ext

        hp.set_one_period(False)

        print("Analiza wyników")

        ExtortionAnalyzer = ExtortionSpectrumAnalyzer()

        storage = DataStorage()

        results = storage.load()

        ExtortionAnalyzer.analyze(results)

        return

#tutaj odpalamy wszystko w pętli

responseFunctions = ['akselrod', 'sinus', 'halfSinus', 'forwarding']
heartRateBoundaries = [[100, 110], [111, 120]]

for resp in responseFunctions:
    for heartRate in heartRateBoundaries:

        hp.set_show_plots(False)
        hp.set_min_breath_period(heartRate[0])
        hp.set_max_breath_period(heartRate[1])
        hp.set_response_function(resp)

        run("gen_ext")