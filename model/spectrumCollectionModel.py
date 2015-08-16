__author__ = 'emil'
from model.model import Model


class SpectrumCollectionModel(Model):
    """
        Model for spectrum table in database
        variables:
        :var id list|int id of the point
        :var measure_id list|int id of the measurement in the 'measure' table
        :var mean_rr list|float
        :var stdev list|float
        :var breath_period int|list

    """
    def __init__(self):
        super(SpectrumCollectionModel, self).__init__()
        # spectrum table model:
        self.measure_id = None     # id of the measure in the measure table
        self.mean_rr = None        # collection of the measure results
        self.stdev = None          # collection of the measure results
        self.breath_period = None  # collection of the measure setting for each result

    def load(self):
        result = super(SpectrumCollectionModel, self).load()

    def _insertSQL(self):
        self._validate(self.ACTION_INSERT)
        # due to the validation, we know that every parameter has to be the same type and not None:
        sql = "INSERT INTO mgr.spectrum (measure_id, mean_rr, stdev, breath_period) VALUES "
        if(isinstance(self.mean_rr, list)):
            sql = ", ".join(self.mean_rr)

        return ""

    def _updateSQL(self):
        self._validate(self.ACTION_UPDATE)
        return ""

    def _removeSQL(self):
        self._validate(self.ACTION_REMOVE)
        return ""

    def _loadSQL(self):
        self._validate(self.ACTION_LOAD)
        return ""

    def _basicValidation(self, action):
        if self.breath_period is None and self.measure_id is None and self.mean_rr is None and self.stdev is None and self.id is None:
            raise Exception("DB_EXCEPTION: Tried to "+str(action)+" without any parameters set in model")

    def _validateInsert(self):
        # check if object is not empty, everything except for id must be set:
        if self.breath_period is None or self.measure_id is None or self.mean_rr is None or self.stdev is None:
            raise Exception("DB_EXCEPTION: Tried to insert incomplete object")
        # check if all parameters types are the same, because we either insert one row or many
        self._compareAllTypes(list(["measure_id", "mean_rr", "stdev", "breath_period"]))
