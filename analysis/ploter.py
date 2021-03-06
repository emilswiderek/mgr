import matplotlib.pyplot as plt

import helpers.helper as hp
import helpers.storageHelper as shp
import helpers.networkStorageHelper as nshp
import numpy as np


class Plotter():

    def __init__(self):
        self.show = hp.show_plots
        shp.init_results_subfolder()

    def map(self, previous_step, results):
        """
        Plots fi(n+1)(fi(n))
        :param previous_step:
        :param results:
        :return:
        """
        plt.clf()
        plt.suptitle("Mapa powrotu")
        plt.title("Faza rytmu serca po oddechu od fazy przed oddechem")
        plt.grid(True)
        plt.ylabel("Faza rytmu serca po oddechu")
        plt.xlabel("Faza rytmu serca przed oddechem")
        plt.scatter(previous_step, results, c=results, s=70)
        plt.gray()

        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/map.png")
            print("Zapis w: "+shp.get_storage_path())

    def heart_rate(self, timesteps, heart_rate):
        """
        Plots a graph for heart rate in time
        :param timesteps:
        :param heart_rate:
        :return:
        """
        plt.clf()
        plt.suptitle("Faza rytmu serca")
        plt.title("T/T0: " + str(hp.T_to_T0))
        plt.xlabel("Czas 1 = 1 okres rytmu oddechu")
        plt.ylabel("Faza rytmu serca")
        plt.xlim(0, 15)
        plt.grid(True)
        plt.plot(timesteps, heart_rate, 'b')
        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/heart_rate.png")

    def heart_and_breath_rate(self, timesteps, breath_rate, heart_rate):
        """
        Plots graph for changes in heart rate by breath
        :param timesteps:
        :param breath_rate:
        :param heart_rate:
        :return:
        """
        plt.clf()
        plt.figure(1)
        plt.suptitle("Faza rytmu serca oraz faza rytmu oddechu")

        plt.subplot(211)
        plt.title("Oddech T/T0: "+str(hp.T_to_T0))
        plt.ylabel("Faza rytmu oddechu")
        plt.xlim(0, 15)
        plt.ylim(-0.00001, 0.00001)
        plt.grid(True)
        plt.plot(timesteps, breath_rate, 'b|', markersize=30)

        plt.subplot(212)
        plt.title("Serce T/T0: "+str(hp.T_to_T0))
        plt.xlabel("Czas 1 = 1 okres rytmu oddechu")
        plt.ylabel("Faza rytmu serca")
        plt.xlim(0, 15)
        plt.ylim(-0.00001, 0.00001)
        plt.grid(True)
        plt.plot(timesteps, heart_rate, 'g|', markersize=30)

        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/heart_and_breath.png")

    def heart_when_breath(self, timesteps, phase):

        plt.clf()
        plt.suptitle("Faza rytmu serca")
        plt.title("W momencie wystąpienia oddechu")
        plt.grid(True)
        plt.xlim(len(timesteps)/10)
        plt.xlabel("Czas 1 = 1 okres rytmu oddechu")
        plt.ylabel("Faza")
        plt.plot(timesteps, phase, 'b.')
        plt.gca().invert_xaxis()
        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/heart_when_breath.png")

    def plot_rr_sd(self, breath, av, sd):
        shp.init_results_subfolder()
        plt.clf()
        plt.figure(1)

        plt.subplot(211)
        plt.ylim(0, max(av) + max(sd))
        plt.suptitle("Odchylenie std")
        plt.title("Dla okresu rytmu serca: "+str(hp.heart_period))
        plt.grid(True)
        plt.ylabel("Średnie RR")
        plt.errorbar(breath, av, sd, linestyle='None', marker='^')

        plt.subplot(212)
        plt.grid(True)
        plt.ylim(0, 50)
        plt.xlabel("Okres oddechu")
        plt.ylabel("Odchylenie std")
        plt.bar(breath, sd)

        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/rr_sd.png")

    def plot_map_and_fit(self, map, fit):
        plt.clf()
        #plt.figure(1)

        #plt.subplot(211)
        plt.grid(True)
        plt.xlabel("Faza rytmu serca przed oddechem")
        plt.ylabel("Faza rytmu serca po oddechu")
        plt.plot(map['previous_step'], map['next_step'], 'b^')

        #plt.subplot(212)
        #plt.grid(True)
        #plt.xlabel("Faza rytmu serca przed oddechem")
        #plt.ylabel("Dopasowanie")
        plt.plot(fit[0], fit[1], 'g*')

        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/map_and_fit.png")

    def plot_map_and_response_func(self, x, y, sX, sY):
        """

        :param x: X values
        :param y: Y fitting curve divided by x
        :param sX: original response function X
        :param sY: original response function Y
        :param vX: X values
        :param vY: Y map Y values divided by X
        :return:
        """
        newY = np.array(sY) - np.array(sX)
        plt.clf()
        plt.title(hp.response_function)
        line2, = plt.plot(x, y, 'g*', label="Krzywa odpowiedzi fazowej")
        line3, = plt.plot(sX, newY, 'r+', markersize=30, label="Mapa - X")
        plt.xlabel("Faza rytmu serca")
        plt.ylabel("Zmiana fazy rytmu serca")
        plt.legend([line2, line3])

        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/map_substraction.png")

    def plot_response_function_from_map(self,substraction, map, responseResult):
        """

        :param substraction:
        :param map:
        :param responseResult:
        :return:
        """
        plt.clf()
        plt.plot(map['previous_step'], substraction, 'g+')
        plt.plot(map['previous_step'], responseResult, 'b*')

        if self.show:
            plt.show()
        else:
            plt.savefig(shp.get_storage_path()+"/division_by_x.png")

    def plot_learning_output(self, data, functionName):
        plt.clf()
        plt.plot(data['x'], data[functionName])

        plt.show()

    def test_plot_network_result(self, netOut, target, x, dist, respF):
        plt.clf()
        plt.xlim(0, 1)
        plt.ylim(-1, 1)

        line1, = plt.plot(x, netOut, 'r-', label="Odpowiedź sieci neuronowej")
        line2, = plt.plot(x, target, 'b-', label="Krzywa odpowiedzi fazowej")
        plt.legend([line1, line2])
        plt.xlabel("Faza rytmu serca "+dist)
        plt.ylabel("Przyrost fazy")
        if self.show:
            plt.show()
        else:
            filename = "test_net_ep"+str(hp.train_epochs)+"_g"+str(hp.train_goal)+"_lr"+str(hp.train_lr)+"_a"+str(hp.train_adapt)+"_lr_inc"+str(hp.train_lr_inc)+"_lr_dec"+str(hp.train_lr_dec)+"_mxpi"+str(hp.train_max_perf_inc)+".png"
            plt.savefig("results/tests/"+respF+filename)