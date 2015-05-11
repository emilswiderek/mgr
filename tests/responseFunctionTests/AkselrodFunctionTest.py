import unittest
import generator.helper as hp
from responseFunction.Akselrod import Akselrod
import matplotlib.pyplot as plt
import random

class TestAkselrodFunction(unittest.TestCase):
    def test_response(self):
        val = random.randrange(0, hp.heart_period/2)
        val2 = random.randrange(hp.heart_period/2, hp.heart_period)
        response_function = Akselrod()
        self.assertAlmostEquals(response_function.forward_percentage*val, response_function.getResponse(val), "Akselrod function first half failed")
        self.assertAlmostEquals(-response_function.backward_percentage*val2, response_function.getResponse(val2), "Akselrod function second half failed")


    def test_entireSpectrumResponseShow(self):
        response_function = Akselrod()
        spectrum = list(range(0, hp.heart_period))
        spectrum_response = []
        spectrum_normalised = []

        for x in spectrum:
            spectrum_response.append(response_function.getResponse(x)/hp.heart_period)
            spectrum_normalised.append(x/hp.heart_period)

        plt.plot(spectrum_normalised, spectrum_response)
        plt.show()

if __name__ == '__main__':
    unittest.main()


