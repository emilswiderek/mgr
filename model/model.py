__author__ = 'emil'
from model.database import Database


class Model():

    ACTION_REMOVE = "remove"
    ACTION_INSERT = "insert"
    ACTION_UPDATE = "update"
    ACTION_LOAD = "load"

    def __init__(self):
        self.db = Database()
        self.id = None

    def save(self):

        if self.id is None:
            sql = self._insertSQL()
        else:
            sql = self._updateSQL()

        return self.db.execute(sql)

    def remove(self):
        self._validate(self.ACTION_REMOVE)

        return self.db.execute(self._removeSQL())

    def load(self):
        result = self.db.execute(self._loadSQL())
        self.id = result['id']
        return result

    def _insertSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _updateSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _removeSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _loadSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _validate(self, action):
        """
        Checks if parameters are correct
        :param action: Which action to validate?
        :return:
        """
        self._basicValidation(action)
        return {
            self.ACTION_REMOVE: self._validateRemove(),
            self.ACTION_INSERT: self._validateInsert(),
            self.ACTION_LOAD: self._validateLoad(),
            self.ACTION_UPDATE: self._validateUpdate(),
        }[action]

    def _validateRemove(self):
        pass

    def _validateInsert(self):
        pass

    def _validateLoad(self):
        pass

    def _validateUpdate(self):
        pass

    def _basicValidation(self, action):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _compareTypes(self, var1Name, var2Name):
        """
        Compares types of properties named as provided, and returns if they are the same

        :param var1Name:
        :param var2Name:
        :return: boolean
        """
        return isinstance(getattr(self, var1Name), type(getattr(self, var2Name)))

    def _compareAllTypes(self, names):
        """
        Checks if all params of provided names have the same type
        :param names: list
        :return:
        """
        for name in names:
            if self._compareTypes(names.first, name):
                raise Exception("DB_EXCEPTION: Type of variable "+str(names.first)+" and "+str(name)+" doesnt match!")

            if len(getattr(self, name)) != len(getattr(self, names.first)):
                raise Exception("DB_EXCEPTION: Length of variable"+str(names.first)+" and "+str(name)+" doesnt match!")


