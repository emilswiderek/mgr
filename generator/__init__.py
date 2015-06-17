import generator.breath_gen
#wszystko zaimportować

import configparser
cp = configparser.ConfigParser()
cp.read("config.ini")

import helpers.helper as hp
hp.setTtoT0(cp['generator']['T_to_T0'])
hp.set_number_of_breaths(cp['generator']['breath_number'])
hp.set_breath_period(cp['generator']['breath_period'])
hp.set_map_fitting_degree(cp['generator']['map_fitting_degree'])
hp.set_heart_period(False)

hp.set_min_breath_period(cp['generator']['min_breath_period'])
hp.set_max_breath_period(cp['generator']['max_breath_period'])
#hp.set_heart_period(300) # @todo ??

hp.set_response_function('akselrod')
hp.set_show_plots(False)

import helpers.storageHelper as shp

shp.init_results_subfolder()


