__author__ = 'emil'
from model.model import Model
from model.HeartbeatsCollectionModel import HeartbeatsCollectionModel
from model.spectrumCollectionModel import SpectrumCollectionModel


class MeasureModel(Model):
    TYPE_GENERATE_EXTORTION = 'gen_ext'
    TYPE_ANALYZE_EXTORTION = 'analyze_ext'
    TABLE_NAME = 'measure'
    """
        Model for measure table in database,
        one instance of object represents one row in the table
        with reference to the heartbeats and spectrum tables

        variables:
        :var: id int
        :var: measure_type string
        :var: heart_period int
        :var: min_breath_period int
        :var: breath_period int
        :var: max_breath_period int
        :var: breath_number int
        :var: updated_at datetime
        :var: response_function string

    """
    def __init__(self, db=None):
        super(MeasureModel, self).__init__(db)
        # measure table model:
        self.measure_type = None
        self.heart_period = None
        self.min_breath_period = None
        self.breath_period = None
        self.max_breath_period = None
        self.breath_number = None
        self.updated_at = None
        self.response_function = None
        self.results = None

    def load(self):
        """
        Selects data from db with consideration of set constraints,
        then sets the first row's values as objects properties,
        and returns entire result

        WARNING: this method works different in other models

        :return:
        """
        result = super(MeasureModel, self).load()
        self.id = result[0]['id']
        self.max_breath_period = result[0]['max_breath_period']
        self.min_breath_period = result[0]['min_breath_period']
        self.measure_type = result[0]['measure_type']
        self.breath_number = result[0]['breath_number']
        self.heart_period = result[0]['heart_period']
        self.breath_period = result[0]['breath_period']
        self.response_function = result[0]['response_function']
        self.updated_at = result[0]['updated_at']
        self.setResultsModel()
        return result

    def _insertSQL(self):
        self._validateInsert()
        # due to the validation, we know that every parameter has to be the same type and not None:
        sql = "INSERT INTO `"+self.db.db_name+"`.`"+self.TABLE_NAME+"` (measure_type, breath_period, heart_period, min_breath_period, max_breath_period, breath_number, response_function) VALUES "
        sql += "(\'"+str(self.measure_type)+"\', "+str(self.breath_period)+", "+str(self.heart_period)+", "+str(self.min_breath_period)+", "+str(self.max_breath_period)+", "+str(self.breath_number)+", \'"+str(self.response_function)+"\')"

        return self._prepareMysqlString(sql)

    def _updateSQL(self):
        self._validateUpdate()
        return ""

    def _removeSQL(self):
        self._validateRemove()
        return ""

    def _loadSQL(self):
        self._validateLoad()
        return "SELECT * FROM `"+self.db.db_name+"`.`"+self.TABLE_NAME+"` "+self.sql_where+self.sql_order+self.sql_limit+self.sql_offset

    def _basicValidation(self, action):
        if self.breath_period is None and self.measure_type is None and self.heart_period is None and self.min_breath_period is None and self.id is None:
            raise Exception("DB_EXCEPTION: Tried to "+str(action)+" without any parameters set in model")

    def _validateInsert(self):
        # check if object is not empty, everything except for id must be set:
        if self.breath_number is None or self.measure_type is None or self.heart_period is None :
            raise Exception("DB_EXCEPTION: Tried to insert incomplete object")

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

    def setResponseFunction(self, responseFunction):
        self.response_function = responseFunction

    def loadResults(self):
        if self.id is None or self.measure_type is None:
            raise Exception("DB_EXCEPTION: Incomplete object, id or measure_type missing")

        if self.results is None:
            self.setResultsModel()

        self.results.where([('measure_id', self.id, '=')])
        self.results.load()

    def setResultsModel(self):
        """
        Based on the type of measurement, sets proper model for results

        :return:
        """
        if self.measure_type == self.TYPE_GENERATE_EXTORTION:
            self.results = HeartbeatsCollectionModel()
        elif self.measure_type == self.TYPE_ANALYZE_EXTORTION:
            self.results = SpectrumCollectionModel()

    def getMeasureResults(self, reload=False):
        """
        Gets the results for this measurement from other table

        :return:
        """
        if reload:
            self.loadResults()
        return self.results

    def saveAll(self):
        """
        Saves both object and results into database
        :return:
        """
        if self.id is None:
            self.id = self.save()
        else:
            self.save()
        if self.results is not None:
            self.results.setMeasureId(self.id)
            self.results.save()
