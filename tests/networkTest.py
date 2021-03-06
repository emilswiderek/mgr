__author__ = 'emil'
from analysis.network import Network
import unittest
from analysis.ploter import Plotter


class NetworkTest(unittest.TestCase):

    def test_learning(self):
        plt = Plotter()
        net = Network()
        output = net.prepareExpectedOutput()
        net.trainNetwork()  # training
        for respF in Network.LEARNING_RESPONSE_FUNCTIONS:
            out = net.getResults(respF)
            plt.test_plot_network_result(out[0], output[respF], output['x'], "", respF)
        net.saveNetwork()