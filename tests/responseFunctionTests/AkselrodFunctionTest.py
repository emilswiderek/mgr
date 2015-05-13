import unittest
import generator.helper as hp
from responseFunction.Akselrod import Akselrod
import matplotlib.pyplot as plt
import random

class TestAkselrodFunction(unittest.TestCase):
    def test_response(self):
        #val2 = random.randrange(hp.heart_period/2, hp.heart_period)
        response_function = Akselrod()
        self.assertAlmostEquals(0, response_function.getResponse(0), "Akselrod function zero test failed")


    def test_entireSpectrumResponseShow(self):
        response_function = Akselrod()
        spectrum = list(range(0, hp.heart_period))
        spectrum_response = []
        spectrum_normalised = []

        for x in spectrum:
            spectrum_response.append(response_function.getResponse(x)/hp.heart_period)
            spectrum_normalised.append(x/hp.heart_period)

        plt.title("Akselrod")
        plt.xlabel("Faza rytmu serca")
        plt.ylabel("Zmiana fazy rytmu serca")
        plt.plot(spectrum_normalised, spectrum_response)
        plt.show()

if __name__ == '__main__':
    unittest.main()


