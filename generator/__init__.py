import generator.breath_gen
#wszystko zaimportować

import configparser
cp = configparser.ConfigParser()
cp.read("generator/config.ini")

import generator.helper as hp
hp.set_steps_in_phase(cp['generator']['steps_in_phase'])
hp.set_number_of_breaths(cp['generator']['breath_number'])


from responseFunction.forwardingFunction import ForwardingFunction
