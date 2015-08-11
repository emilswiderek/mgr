import json as js
import os
import helpers.storageHelper as shp
import helpers.helper as hp


class DataStorage():
    """
     Saves the data to the hard drive
     and retrieves it from there
    """

    def __init__(self):
        self.filename = str(hp.response_function)+"_"+str(hp.min_breath_period)+"_"+str(hp.max_breath_period)+"_dataStorage.json"

    def store(self, data):
        """
        Saves the provided data to the data storage file.

        :param data:
        :return:
        """
        self.clear()
        file = open(shp.get_storage_path()+"/"+self.filename, 'w+')
        print("Zapisywanie w "+self.filename)
        js.dump(data, file)
        print("Zapisano")
        return file.close()

    def load(self):
        """
        Loads data from storage

        :return:
        """
        file = open(shp.get_storage_path()+"/"+self.filename, 'r')
        data = js.load(file)
        file.close()
        return data

    def clear(self):
        """
        Clears data storage

        :return:
        """
        if os.path.isfile((shp.get_storage_path()+"/"+self.filename)):
            os.remove((shp.get_storage_path()+"/"+self.filename))

    def set_filename(self, name):
        self.filename = name