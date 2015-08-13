__author__ = 'emil'
from model.database import Database


class Model():

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

        if self.id is None:
            raise Exception("Tried to remove object without providing ID")

        return self.db.execute(self._removeSQL())

    def load(self):
        result = self.db.execute(self._loadSQL())
        self.id = result['id']
        return result

    def _insertSQL(self):
        raise NotImplementedError("The main model object should be considered abstract")

    def _updateSQL(self):
        raise NotImplementedError("The main model object should be considered abstract")

    def _removeSQL(self):
        raise NotImplementedError("The main model object should be considered abstract")

    def _loadSQL(self):
        raise NotImplementedError("The main model object should be considered abstract")
