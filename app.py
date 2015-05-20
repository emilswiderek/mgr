from generator import main
from analysis.oneExtortionPeriodAnalysis import Analyzer

# one period results:
breath, heart = main.main()

onePeriodAnalyzer = Analyzer(breath, heart)


onePeriodAnalyzer.analyze()
