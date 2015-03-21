import generator.breth_gen
#wszystko zaimportować



import configparser
cp = configparser.ConfigParser()
cp.read("config.ini")

import generator.helper as hp
hp.Helper.steps_in_phase = cp['steps_in_phase']
