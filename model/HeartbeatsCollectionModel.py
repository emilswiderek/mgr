__author__ = 'emil'
from model.model import Model
import time

class HeartbeatsCollectionModel(Model):
    TABLE_NAME = 'heartbeats'
    """
        Model for spectrum table in database
        variables:
        :var id list|int id of the point
        :var measure_id list|int id of the measurement in the 'measure' table
        :var mean_rr list|float
        :var stdev list|float
        :var breath_period int|list

    """
    def __init__(self, db=None):
        super(HeartbeatsCollectionModel, self).__init__(db)
        # heartbeats table model:
        self.measure_id = None     # id of the measure in the measure table
        self.heart_phase = None        # collection of the measure results
        self.breath_phase = None

    def load(self):
        """
        Loads data from database

        :return:
        """
        result = super(HeartbeatsCollectionModel, self).load()

        self.id = []
        self.measure_id = []
        self.heart_phase = []
        self.breath_phase = []
        for res in result:
            self.id.append(res['id'])
            self.measure_id.append(res['measure_id'])
            self.heart_phase.append(res['heart_phase'])
            self.breath_phase.append(res['breath_phase'])

        return result

    def _insertSQL(self):
        self._validateInsert()
        # due to the validation, we know that every parameter has to be the same type and not None:
        sql = "INSERT INTO `"+self.db.db_name+"`.`"+self.TABLE_NAME+"` (measure_id, heart_phase, breath_phase) VALUES "
        if(isinstance(self.heart_phase, list)):
            for i in range(0, len(self.heart_phase)):
                sql += "("+str(self.measure_id)+", "+str(self.heart_phase[i])+", "+str(self.breath_phase[i])+")"
                if i <len(self.heart_phase)-1:
                    sql += ", "
        else:
            sql += "("+str(self.measure_id)+", "+str(self.heart_phase)+", "+str(self.breath_phase)+")"

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
        if self.measure_id is None and self.id is None and self.heart_phase is None and self.breath_phase is None and self.sql_where == "":
            raise Exception("DB_EXCEPTION: Tried to "+str(action)+" without any parameters set in model")

    def _validateInsert(self):
        # check if object is not empty, everything except for id must be set:
        if self.measure_id is None or self.heart_phase is None or self.breath_phase is None:
            raise Exception("DB_EXCEPTION: Tried to insert incomplete object")
        self._compareAllTypes(list(["heart_phase", "breath_phase"]))

    def _validateLoad(self):
        pass

    def setMeasureId(self, measure_id):
        self.measure_id = measure_id

    def setHeartPhase(self, heart_phase):
        self.heart_phase = heart_phase

    def setBreathPhase(self, breath_phase):
        self.breath_phase = breath_phase