__author__ = 'emil'
from model.model import Model


class SpectrumModel(Model):

    def __init__(self):
        super(SpectrumModel, self).__init__()
        # model:

        self.measure_type = None
        self.breath_period = None
        self.heart_period = None
        self.min_breath_period = None
        self.max_breath_period = None
        self.breath_number = None
        self.updated_at = None

    def load(self):
        result = super(SpectrumModel, self).load()

    def _insertSQL(self):
        return ""

    def _updateSQL(self):
        return ""

    def _removeSQL(self):
        return ""

    def _loadSQL(self):
        return ""