__author__ = 'emil'
from model.model import Model


class MeasureModel(Model):
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
        super(MeasureModel, self).__init__()
        # measure table model:
        self.measure_type = None
        self.heart_period = None
        self.min_breath_period = None
        self.breath_period = None
        self.max_breath_period = None
        self.breath_number = None
        self.updated_at = None

    def load(self):
        result = super(MeasureModel, self).load()

    def _insertSQL(self):
        self._validate(self.ACTION_INSERT)
        # due to the validation, we know that every parameter has to be the same type and not None:
        sql = "INSERT INTO mgr.measure (measure_type, breath_period, heart_period, min_breath_period, max_breath_period, breath_number) VALUES "
        sql += "('"+str(self.measure_type)+"', "+str(self.breath_period)+", "+str(self.heart_period)+", "+str(self.min_breath_period)+", "+str(self.max_breath_period)+", "+str(self.breath_number)+")"

        return self._prepareMysqlString(sql)

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
        if self.breath_period is None and self.measure_type is None and self.heart_period is None and self.min_breath_period is None and self.id is None:
            raise Exception("DB_EXCEPTION: Tried to "+str(action)+" without any parameters set in model")

    def _validateInsert(self):
        # check if object is not empty, everything except for id must be set:
        if self.breath_number is None or self.measure_type is None or self.heart_period is None :
            raise Exception("DB_EXCEPTION: Tried to insert incomplete object")

    def setId(self, id):
        self.id = id

    def setMeasureType(self, type):
        self.measure_type = type

    def setHeartPeriod(self, heartPeriod):
        self.heart_period = heartPeriod

    def setMinBreathPeriod(self, minBreathPeriod):
        self.min_breath_period = minBreathPeriod

    def setMaxBreathPeriod(self, maxBreathPeriod):
        self.max_breath_period = maxBreathPeriod

    def setBreathPeriod(self, breath_period):
        self.breath_period = breath_period

    def setBreathNumber(self, breathNumber):
        self.breath_number = breathNumber
