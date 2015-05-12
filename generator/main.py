from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from responseFunction.forwardingFunction import ForwardingFunction
from responseFunction.sinusFunction import SinusFunction
from analysis.phaseDifferences import PhaseDifferences
from responseFunction.Akselrod import Akselrod
import matplotlib.pyplot as plt
import numpy as np
import generator.helper as hp


def main():
    BreathGen = BreathGenerator()
    HeartGen = HeartGenerator()

    breathFunction = BreathGen.generateProcess()
    HeartGen.setBreathFunction(breathFunction)
    HeartGen.setResponseFunction(getResponseFunction('forwarding'))
    heartFunction = HeartGen.generateProcess()

    bind = bind_breath_and_heart(breathFunction, heartFunction)
    phaseAnalyzer = PhaseDifferences()
    indexes, results, previous_step = phaseAnalyzer.analyze(breathFunction, heartFunction)
    #print("Results: ")
    #print(results)
    #print(indexes)

    plt.suptitle("Mapa powrotu")
    plt.title("Faza serca po oddechu od fazy przed oddechem")
    plt.grid(True)
    plt.ylabel("Faza po oddechu")
    plt.xlabel("Faza przed oddechem")
    plt.plot(previous_step, results, 'g^')
    plt.show()

    plt.suptitle("Faza serca")
    plt.title("T/T0: "+str(hp.T_to_T0))
    plt.xlabel("Czas 1 = 1 okres bicia serca")
    plt.ylabel("Faza")
    plt.grid(True)
    plt.plot(bind[0], bind[2], 'b')
    plt.show()

    plt.suptitle("Faza serca oraz oddechu")
    plt.title("T/T0: "+str(hp.T_to_T0))
    plt.xlabel("Czas 1 = 1 okres bicia serca")
    plt.ylabel("Faza")
    plt.ylim(-0.00001, 0.00001)
    plt.grid(True)
    plt.plot(bind[0], bind[1], 'b|', bind[0], bind[2], 'g|', markersize=300)
    plt.show()

    plt.suptitle("Faza serca")
    plt.title("W momencie wystąpienia oddechu")
    plt.grid(True)
    plt.xlabel("Czas 1 = 1 okres bicia serca")
    plt.ylabel("Faza")
    plt.plot(indexes/hp.breath_period, previous_step, 'b')
    plt.show()



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