from generator.BreathGenerator import BreathGenerator
from generator.HeartGenerator import HeartGenerator
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