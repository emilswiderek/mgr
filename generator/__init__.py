import generator.breath_gen
#wszystko zaimportować

import configparser
cp = configparser.ConfigParser()
cp.read("generator/config.ini")

import generator.helper as hp
hp.setTtoT0(cp['generator']['T_to_T0'])
hp.set_number_of_breaths(cp['generator']['breath_number'])
hp.set_breath_period(cp['generator']['breath_period'])
hp.set_heart_period()

from responseFunction.forwardingFunction import ForwardingFunction
