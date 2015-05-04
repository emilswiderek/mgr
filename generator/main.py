from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from responseFunction.forwardingFunction import ForwardingFunction
from responseFunction.sinusFunction import SinusFunction
from analysis.phaseDifferences import PhaseDifferences


def main():
    BreathGen = BreathGenerator()
    HeartGen = HeartGenerator()

    breathFunction = BreathGen.generateProcess()
    HeartGen.setBreathFunction(breathFunction)
    HeartGen.setResponseFunction(getResponseFunction('sinus'))
    heartFunction = HeartGen.generateProcess()

    breath_and_heart_printer(breathFunction, heartFunction)
    phaseAnalyzer = PhaseDifferences()
    indexes, results = phaseAnalyzer.analyze(breathFunction, heartFunction)
    print("Results: ")
    print(results)
    print(indexes)


def getResponseFunction(name):
    # @todo set as parameter name of response function
    return {
        'forwarding': ForwardingFunction(),
        'sinus': SinusFunction()
    }[name]

def breath_and_heart_printer(breathFunction, heartFunction):
    print("Iteration:".ljust(10),"Breath phase:".ljust(20), "Heart phase:".ljust(20))
    for x in range(0, len(breathFunction)):
        print(str(x).ljust(10), str(breathFunction[x]).ljust(20), str(heartFunction[x]).ljust(20))


if __name__ == "__main__":
    main()