from analysis.MapAnalysis import MapAnalysis
from generator import main
from analysis.oneExtortionPeriodAnalysis import Analyzer
from generator.extortionSpectrum import ExtortionSpectrumGenerator
from analysis.extortionSpectrumAnalysis import ExtortionSpectrumAnalyzer
from generator.dataStorage import DataStorage
import generator.helper as hp

import gc

# options:
# 'gen_ext' - generate extortion spectrum and save it in the storage file
# 'one_period' - generate and analyze data for one breath period
# else - read from data storage and analyze spectrum

option = 'one_period_analyze'

if option == 'one_period':

    print("Generowanie i analiza dla 1 okresu oddechu")

    # one period results:
    breath, heart = main.main()

    onePeriodAnalyzer = Analyzer(breath, heart)

    onePeriodAnalyzer.analyze()

elif option == 'one_period_analyze':

    print("Analiza dla 1 okresu oddechu")

    storage = DataStorage()

    #map analysis:
    storage.set_filename(str(hp.T_to_T0)+"_map.json")
    map = storage.load()

    mapAnalysis = MapAnalysis()
    mapAnalysis.analyze(map)

elif option == 'gen_ext':

    print("Generowanie")

    # results for different extortion periods:

    Generator = ExtortionSpectrumGenerator()

    results = Generator.generate()

    storage = DataStorage()

    storage.clear()

    storage.store(results)

else:

    print("Analiza wyników")

    ExtortionAnalyzer = ExtortionSpectrumAnalyzer()

    storage = DataStorage()

    results = storage.load()

    ExtortionAnalyzer.analyze(results)
