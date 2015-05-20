from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from responseFunction.forwardingFunction import ForwardingFunction
from responseFunction.sinusFunction import SinusFunction
from responseFunction.Akselrod import Akselrod


def main():
    BreathGen = BreathGenerator()
    HeartGen = HeartGenerator()

    breathFunction = BreathGen.generateProcess()
    HeartGen.setBreathFunction(breathFunction)
    HeartGen.setResponseFunction(getResponseFunction('sinus'))
    heartFunction = HeartGen.generateProcess()

    return breathFunction, heartFunction

def getResponseFunction(name):
    # @todo set as parameter name of response function
    return {
        'forwarding': ForwardingFunction(),
        'sinus': SinusFunction(),
        'akselrod': Akselrod(),
    }[name]

if __name__ == "__main__":
    main()