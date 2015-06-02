import json as js
import os


class DataStorage():
    """
     Saves the data to the hard drive
     and retrieves it from there
    """

    def __init__(self):
        self.filename = "dataStorage.json"

    def store(self, data):
        """
        Saves the provided data to the data storage file.

        :param data:
        :return:
        """
        file = open(self.filename, 'w+')
        js.dump(data, file)
        file.close()

    def load(self):
        """
        Loads data from storage

        :return:
        """
        file = open(self.filename, 'r')
        data = js.load(file)
        file.close()
        return data

    def clear(self):
        """
        Clears data storage

        :return:
        """
        if os.path.isfile(self.filename):
            os.remove(self.filename)
