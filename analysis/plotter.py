import matplotlib.pyplot as plt
import generator.helper as hp


class Plotter():


    def map(self, previous_step, results):
        """
        Plots fi(n+1)(fi(n))
        :param previous_step:
        :param results:
        :return:
        """
        plt.suptitle("Mapa powrotu")
        plt.title("Faza rytmu serca po oddechu od fazy przed oddechem")
        plt.grid(True)
        plt.ylabel("Faza rytmu serca po oddechu")
        plt.xlabel("Faza rytmu serca przed oddechem")
        plt.plot(previous_step, results, 'g^')
        plt.show()

    def heart_rate(self, timesteps, heart_rate):
        """
        Plots a graph for heart rate in time
        :param timesteps:
        :param heart_rate:
        :return:
        """
        plt.suptitle("Faza rytmu serca")
        plt.title("T/T0: " + str(hp.T_to_T0))
        plt.xlabel("Czas 1 = 1 okres rytmu serca")
        plt.ylabel("Faza")
        plt.grid(True)
        plt.plot(timesteps, heart_rate, 'b')
        plt.show()

    def heart_and_breath_rate(self, timesteps, breath_rate, heart_rate):
        """
        Plots graph for changes in heart rate by breath
        :param timesteps:
        :param breath_rate:
        :param heart_rate:
        :return:
        """
        plt.suptitle("Faza rytmu serca oraz faza rytmu oddechu")
        plt.title("T/T0: "+str(hp.T_to_T0))
        plt.xlabel("Czas 1 = 1 okres rytmu serca")
        plt.ylabel("Faza")
        plt.ylim(-0.00001, 0.00001)
        plt.grid(True)
        plt.plot(timesteps, breath_rate, 'b|', timesteps, heart_rate, 'g|', markersize=300)
        plt.show()

    def heart_when_breath(self, timesteps, phase):

        plt.suptitle("Faza rytmu serca")
        plt.title("W momencie wystąpienia oddechu")
        plt.grid(True)
        plt.xlabel("Czas 1 = 1 okres bicia serca")
        plt.ylabel("Faza")
        plt.plot(timesteps, phase, 'b')
        plt.show()