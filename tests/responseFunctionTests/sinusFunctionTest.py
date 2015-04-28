# test if distances between breaths are equal
import unittest
import generator.helper as hp
from responseFunction.sinusFunction import SinusFunction
import matplotlib.pyplot as plt
import cmath
import random
import numpy as np

class TestSinusFunction(unittest.TestCase):
    def test_response(self):
        val = random.uniform(0.0, 1.0)
        response_function = SinusFunction()
        self.assertEqual(response_function.max_amplitude*cmath.sin(val), response_function.getResponse(val), "Sinus function failed")

    def test_entireSpectrumResponseShow(self):
        response_function = SinusFunction()
        spectrum = list(np.arange(0,1,1/hp.breath_period))
        spectrum_response = []
        for x in spectrum: # @todo check this test, add x scale to plots
            spectrum_response.append(response_function.getResponse(x))
        plt.plot(spectrum_response)
        plt.show()

if __name__ == '__main__':
    unittest.main()


