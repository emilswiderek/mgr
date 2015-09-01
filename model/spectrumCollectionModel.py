__author__ = 'emil'
from model.model import Model


class SpectrumCollectionModel(Model):
    TABLE_NAME = 'spectrum'
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
        super(SpectrumCollectionModel, self).__init__(db)
        # spectrum table model:
        self.measure_id = None     # id of the measure in the measure table
        self.mean_rr = []        # collection of the measure results
        self.stdev = []          # collection of the measure results
        self.breath_period = []  # collection of the measure setting for each result

    def load(self):
        result = super(SpectrumCollectionModel, self).load()  # @todo this

        self.id = []
        self.measure_id = []
        self.mean_rr = []
        self.stdev = []
        for res in result:
            self.id.append(res['id'])
            self.measure_id.append(res['measure_id'])
            self.stdev.append(res['stdev'])
            self.mean_rr.append(res['mean_rr'])

        return result

    def _insertSQL(self):
        self._validateInsert()
        # due to the validation, we know that every parameter has to be the same type and not None:
        sql = "INSERT INTO `"+self.db.db_name+"`.`"+self.TABLE_NAME+"` (measure_id, mean_rr, stdev, breath_period) VALUES "
        if(isinstance(self.mean_rr, list)):
            for i in range(0, len(self.mean_rr)):
                sql += "("+str(self.measure_id)+", "+str(self.mean_rr[i])+", "+str(self.stdev[i])+", "+str(self.breath_period[i])+")"
                if i <len(self.mean_rr)-1:
                    sql += ", "
        else:
            sql += "("+str(self.measure_id)+", "+str(self.mean_rr)+", "+str(self.stdev)+", "+str(self.breath_period)+")"

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
        if self.breath_period is None and self.measure_id is None and self.mean_rr is None and self.stdev is None and self.id is None:
            raise Exception("DB_EXCEPTION: Tried to "+str(action)+" without any parameters set in model")

    def _validateInsert(self):
        # check if object is not empty, everything except for id must be set:
        if self.breath_period is None or self.measure_id is None or self.mean_rr is None or self.stdev is None:
            raise Exception("DB_EXCEPTION: Tried to insert incomplete object")
        # check if all parameters types are the same, because we either insert one row or many
        self._compareAllTypes(list(["mean_rr", "stdev"]))
        if isinstance(self.breath_period, list) and not isinstance(self.mean_rr, list):
            raise Exception("DB_EXCEPTION: breath_period:list has different type than mean_rr:"+str(type(self.mean_rr)))

    def setMeasureId(self, measure_id):
        self.measure_id = measure_id

    def setMeanRR(self, mean_rr):
        self.mean_rr = mean_rr

    def setStDev(self, stdev):
        self.stdev = stdev

    def setBreathPeriod(self, breath_period):
        self.breath_period = breath_period