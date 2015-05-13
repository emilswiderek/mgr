from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from responseFunction.forwardingFunction import ForwardingFunction
from responseFunction.sinusFunction import SinusFunction
from analysis.phaseDifferences import PhaseDifferences
from responseFunction.Akselrod import Akselrod
import numpy as np
import generator.helper as hp
from analysis.plotter import Plotter


def main():
    BreathGen = BreathGenerator()
    HeartGen = HeartGenerator()

    breathFunction = BreathGen.generateProcess()
    HeartGen.setBreathFunction(breathFunction)
    HeartGen.setResponseFunction(getResponseFunction('sinus'))
    heartFunction = HeartGen.generateProcess()

    bind = bind_breath_and_heart(breathFunction, heartFunction)
    phaseAnalyzer = PhaseDifferences()
    indexes, results, previous_step = phaseAnalyzer.analyze(breathFunction, heartFunction)
    #print("Results: ")
    #print(results)
    #print(indexes)

    plotter = Plotter()

    # Mapa powrotu:
    plotter.map(previous_step, results)

    #Faza rytmu serca:
    plotter.heart_rate(bind[0], bind[2])

    #Faza rytmu serca i oddechu:
    plotter.heart_and_breath_rate(bind[0], bind[1], bind[2])

    #Faza rytmu serca w momencie wystąpienia oddechu
    plotter.heart_when_breath(indexes, previous_step)




def getResponseFunction(name):
    # @todo set as parameter name of response function
    return {
        'forwarding': ForwardingFunction(),
        'sinus': SinusFunction(),
        'akselrod': Akselrod(),
    }[name]

def bind_breath_and_heart(breathFunction, heartFunction):
    #print("Iteration:".ljust(10),"Breath phase:".ljust(20), "Heart phase:".ljust(20))
    bind = np.ndarray(shape=(3, len(breathFunction)))
    for x in range(0, len(breathFunction)):
        #print(str(x).ljust(10), str(breathFunction[x]).ljust(20), str(heartFunction[x]).ljust(20))
        bind[0][x] = x/hp.breath_period
        bind[1][x] = breathFunction[x]/hp.breath_period
        bind[2][x] = heartFunction[x]/hp.heart_period
    return bind

if __name__ == "__main__":
    main()