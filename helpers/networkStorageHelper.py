import helpers.helper as hp
import os

storage_directory = 'results'
subfolder_name = 'uninitialised_subfolder_name'
main_subdir = "network"
dir = "uninitialised_subdir"


def set_storage_directory(new):
    global storage_directory
    storage_directory = new


def init_results_subfolder():
    global subfolder_name, storage_directory, dir

    if hp.one_period:
        dir = str(hp.network_number_of_neurons)
        subfolder_name = str(hp.response_function) \
                         + "_" + str(hp.T_to_T0) \
                         + "_len_" + str(hp.number_of_breaths)

    else:
        dir = extortion_spectrum_subdir
        subfolder_name = str(hp.response_function) \
                         + "_" + str(hp.min_breath_period) \
                         + "-" + str(hp.max_breath_period)

    if not os.path.isdir(storage_directory + "/" + dir):
        os.mkdir(storage_directory + "/" + dir)

    if not os.path.isdir(get_storage_path()):
        os.mkdir(get_storage_path(), 0o755)


def get_storage_path():
    return storage_directory + "/" + dir + "/" + subfolder_name