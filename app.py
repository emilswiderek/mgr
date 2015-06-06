from analysis.MapAnalysis import MapAnalysis
from generator import main
from analysis.oneExtortionPeriodAnalysis import Analyzer
from generator.extortionSpectrum import ExtortionSpectrumGenerator
from analysis.extortionSpectrumAnalysis import ExtortionSpectrumAnalyzer
from helpers.dataStorage import DataStorage
import helpers.helper as hp

# options:
# 'gen_ext' - generate extortion spectrum and save it in the storage file
# 'one_period' - generate and analyze data for one breath period
# else - read from data storage and analyze spectrum

option = 'one_period'

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

elif option == 'gen_ext':

    hp.set_one_period(False)

    print("Generowanie")

    # results for different extortion periods:

    Generator = ExtortionSpectrumGenerator()

    results = Generator.generate()

    storage = DataStorage()

    storage.store(results)

else:

    hp.set_one_period(False)

    print("Analiza wyników")

    ExtortionAnalyzer = ExtortionSpectrumAnalyzer()

    storage = DataStorage()

    results = storage.load()

    ExtortionAnalyzer.analyze(results)
