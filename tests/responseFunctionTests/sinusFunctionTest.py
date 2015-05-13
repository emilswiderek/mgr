# test if distances between breaths are equal
import unittest
import math
import generator.helper as hp
from responseFunction.sinusFunction import SinusFunction
import matplotlib.pyplot as plt
import cmath
import random

class TestSinusFunction(unittest.TestCase):
    def test_response(self):
        val = random.randrange(0, hp.heart_period)
        response_function = SinusFunction()
        self.assertAlmostEquals(response_function.max_amplitude*cmath.sin(math.pi*val/hp.heart_period*2), response_function.getResponse(val), 5, "Sinus function failed")

    def test_entireSpectrumResponseShow(self):
        response_function = SinusFunction()
        spectrum = list(range(0, hp.heart_period))
        spectrum_response = []
        spectrum_normalised = []

        for x in spectrum:
            spectrum_response.append(response_function.getResponse(x))
            spectrum_normalised.append(x/hp.heart_period)

        plt.title("Sinus")
        plt.xlabel("Faza rytmu serca")
        plt.ylabel("Zmiana fazy rytmu serca")
        plt.plot(spectrum_normalised, spectrum_response)
        plt.show()

if __name__ == '__main__':
    unittest.main()


