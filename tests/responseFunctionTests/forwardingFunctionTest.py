# test if distances between breaths are equal
import unittest

import matplotlib.pyplot as plt

import helpers.helper as hp
from responseFunction.forwardingFunction import ForwardingFunction


class TestForwardingFunction(unittest.TestCase):
    def test_response(self):
        val = 1
        response_function = ForwardingFunction()
        self.assertEqual(response_function.forward_step, response_function.getResponse(val),"Forwarding function failed")

    def test_entireSpectrumResponseShow(self):
        response_function = ForwardingFunction()
        spectrum = list(range(0, hp.heart_period))
        spectrum_response = []
        spectrum_normalised = []
        for x in spectrum:
            spectrum_response.append(response_function.getResponse(x))
            spectrum_normalised.append(x/hp.heart_period)

        plt.title("Funkcja przyrostu fazy")
        plt.xlabel("Faza rytmu serca")
        plt.ylabel("Zmiana fazy rytmu serca")
        plt.plot(spectrum_normalised, spectrum_response)
        plt.show()


if __name__ == '__main__':
    unittest.main()


