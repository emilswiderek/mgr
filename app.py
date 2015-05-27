from generator import main
from analysis.oneExtortionPeriodAnalysis import Analyzer
from generator.extortionSpectrum import ExtortionSpectrumGenerator
from analysis.extortionSpectrumAnalysis import ExtortionSpectrumAnalyzer

# one period results:
#breath, heart = main.main()

#onePeriodAnalyzer = Analyzer(breath, heart)


#onePeriodAnalyzer.analyze()


# results for different extortion periods:

Generator = ExtortionSpectrumGenerator()

results = Generator.generate()

ExtortionAnalyzer = ExtortionSpectrumAnalyzer()

ExtortionAnalyzer.analyze(results)