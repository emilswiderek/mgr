from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from responseFunction.forwardingFunction import ForwardingFunction
from responseFunction.sinusFunction import SinusFunction


def main():
    BreathGen = BreathGenerator()
    HeartGen = HeartGenerator()

    breathFunction = BreathGen.generateProcess()
    HeartGen.setBreathFunction(breathFunction)
    HeartGen.setResponseFunction(getResponseFunction('forwarding'))
    heartFunction = HeartGen.generateProcess()
    print("Breath phase:".ljust(20), "Heart phase:".ljust(20))
    for x in range(0, len(breathFunction)):
        print(str(breathFunction[x]).ljust(20), str(heartFunction[x]).ljust(20))
# @todo make t/t0 for phase!!

def getResponseFunction(name):
    # @todo set as parameter name of response function
    return {
        'forwarding': ForwardingFunction(),
        'sinus': SinusFunction()
    }[name]


if __name__ == "__main__":
    main()