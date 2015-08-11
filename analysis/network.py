__author__ = 'emil'
import neurolab as nl

class Network():

    def __init__(self):
        """
        inicjalizacja sieci...
        :return:
        """
        self.network = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5]], [3, 1])

    def trainNetwork(self, input):
        """
        Ćwiczenie sieci...
        :param input:
        :return:
        """
        self.network