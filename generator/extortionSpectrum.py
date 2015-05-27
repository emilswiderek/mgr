__author__ = 'emil'
from generator import helper as hp
from generator import main

class ExtortionSpectrumGenerator:

    def __init__(self):
        self.min_breath = hp.min_breath_period
        self.max_breath = hp.max_breath_period

    def generate(self):
        results = {}

        for x in range(self.min_breath, self.max_breath):
            hp.set_breath_period(x)
            hp.calculateTtoT0()
            breath, heart = main.main()
            results[x] = {'breath': breath, 'heart': heart}

            print("Generating "+str(x)+"/"+str(self.max_breath-1))

        return results