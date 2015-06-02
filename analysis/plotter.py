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
        plt.scatter(previous_step, results, c=results, s=70)
        plt.gray()
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
        plt.xlabel("Czas 1 = 1 okres rytmu oddechu")
        plt.ylabel("Faza")
        plt.xlim(0, 15)
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
        plt.xlabel("Czas 1 = 1 okres rytmu oddechu")
        plt.ylabel("Faza")
        plt.xlim(0, 15)
        plt.ylim(-0.00001, 0.00001)
        plt.grid(True)
        plt.plot(timesteps, breath_rate, 'b|', timesteps, heart_rate, 'g|', markersize=300)
        plt.show()

    def heart_when_breath(self, timesteps, phase):

        plt.suptitle("Faza rytmu serca")
        plt.title("W momencie wystąpienia oddechu")
        plt.grid(True)
        plt.xlabel("Czas 1 = 1 okres rytmu oddechu")
        plt.ylabel("Faza")
        plt.plot(timesteps, phase, 'b')
        plt.show()

    def plot_rr_sd(self, breath, av, sd):

        plt.figure(1)

        plt.subplot(211)
        plt.suptitle("Odchylenie std")
        plt.title("Dla okresu rytmu serca: "+str(hp.heart_period))
        plt.grid(True)
        plt.xlabel("Okres oddechu")
        plt.ylabel("Średnie RR")
        plt.errorbar(breath, av, sd, linestyle='None', marker='^')

        plt.subplot(212)
        plt.grid(True)
        plt.xlabel("Okres oddechu")
        plt.ylabel("Odchylenie std")
        plt.bar(breath, sd)

        plt.show()