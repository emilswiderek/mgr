from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from helpers import helper as hp


def main():
    BreathGen = BreathGenerator()
    HeartGen = HeartGenerator()

    breathFunction = BreathGen.generateProcess()
    HeartGen.setBreathFunction(breathFunction)
    HeartGen.setResponseFunction(HeartGen.getResponseFunction(hp.response_function))
    heartFunction = HeartGen.generateProcess()

    return breathFunction, heartFunction

if __name__ == "__main__":
    main()