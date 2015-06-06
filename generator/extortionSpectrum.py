__author__ = 'emil'
from helpers import helper as hp
from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator


class ExtortionSpectrumGenerator:

    def __init__(self):
        self.min_breath = hp.min_breath_period
        self.max_breath = hp.max_breath_period

    def generate(self):
        results = {}
        BreathGen = BreathGenerator()
        HeartGen = HeartGenerator()
        HeartGen.setResponseFunction(HeartGen.getResponseFunction(hp.response_function))

        for x in range(self.min_breath, self.max_breath):
            hp.set_breath_period(x)
            hp.calculateTtoT0()

            breath = BreathGen.generateProcess()

            HeartGen.setBreathFunction(breath)

            results[x] = {'breath': breath, 'heart': HeartGen.generateProcess()}

            print("Generating "+str(x)+"/"+str(self.max_breath-1))

        return results