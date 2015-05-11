# test if distances between breaths are equal
import unittest
import generator.helper as hp
from responseFunction.forwardingFunction import ForwardingFunction
import matplotlib.pyplot as plt


class TestForwardingFunction(unittest.TestCase):
    def test_response(self):
        val = 1
        response_function = ForwardingFunction()
        self.assertEqual(response_function.forward_step, response_function.getResponse(val),
                         "Forwarding function failed")

    def test_entireSpectrumResponseShow(self):
        response_function = ForwardingFunction()
        spectrum = list(range(0, hp.heart_period))
        spectrum_response = []
        spectrum_normalised = []
        for x in spectrum:
            spectrum_response.append(response_function.getResponse(x))
            spectrum_normalised.append(x/hp.heart_period)
        plt.plot(spectrum_normalised, spectrum_response)
        plt.show()


if __name__ == '__main__':
    unittest.main()


