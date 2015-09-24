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

    dir = "N_"+str(hp.network_number_of_neurons)
    subfolder_name = "net_ep"+str(hp.train_epochs) \
                     +"_g"+str(hp.train_goal) \
                     +"_lr"+str(hp.train_lr) \
                     +"_a"+str(hp.train_adapt) \
                     +"_lr_inc"+str(hp.train_lr_inc) \
                     +"_lr_dec"+str(hp.train_lr_dec) \
                     +"_mxpi"+str(hp.train_max_perf_inc)

    if not os.path.isdir(storage_directory + "/"+main_subdir):
        os.mkdir(storage_directory + "/"+main_subdir)

    if not os.path.isdir(storage_directory + "/"+main_subdir + "/" + dir):
        os.mkdir(storage_directory + "/"+main_subdir + "/" + dir)

    if not os.path.isdir(get_storage_path()):
        os.mkdir(get_storage_path(), 0o755)


def get_storage_path():
    return storage_directory + "/"+main_subdir + "/" + dir + "/" + subfolder_name + "/"