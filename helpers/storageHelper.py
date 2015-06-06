import helpers.helper as hp
import os
storage_directory = 'results'
subfolder_name = 'uninitialised_subfolder_name'


def set_storage_directory(new):
    global storage_directory
    storage_directory = new


def init_results_subfolder():
    global subfolder_name, storage_directory
    subfolder_name = str(hp.response_function) + "_" + str(hp.T_to_T0) + "_len_" + str(hp.number_of_breaths)

    if not os.path.isdir(get_storage_path()):
        os.mkdir(get_storage_path(), 0o755)


def get_storage_path():
    return storage_directory + "/" + subfolder_name