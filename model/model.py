__author__ = 'emil'
from model.database import Database


class Model():

    def __init__(self, db=None):
        if db is None:
            self.db = Database()
        else:
            self.db = db
        self.id = None
        self.sql_limit = ""
        self.sql_offset = ""
        self.sql_order = ""
        self.sql_where = ""

    def save(self, last_row_id=False):
        if self.id is None:
            return self.db.execute(self._insertSQL())
        else:
            return self.db.execute(self._updateSQL())

    def remove(self):
        self._validateRemove()

        return self.db.execute(self._removeSQL())

    def load(self):
        """
        Selects data from db with consideration of set constraints, and returns result
        :return:
        """
        self._validateLoad()
        return self.db.execute(self._loadSQL())

    def _insertSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _updateSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _removeSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

    def _loadSQL(self):
        raise NotImplementedError("The main model object should be considered abstract and this method should be implemented in child")

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
            if not self._compareTypes(names[0], name):
                raise Exception("DB_EXCEPTION: Type of variable "+str(names[0])+":"+str(type(getattr(self, names[0])))+" and "+str(name)+":"+str(type(getattr(self, name)))+" doesnt match!")

            if hasattr(getattr(self, name), 'len') and len(getattr(self, name)) != len(getattr(self, names[0])):
                raise Exception("DB_EXCEPTION: Length of variable "+str(names[0])+" and "+str(name)+" doesnt match!")

    def _prepareMysqlString(self, query):
        return query.replace('None', 'NULL')

    def limit(self, limit):
        """
        Add limit clause to sql

        :param limit: string
        :return:
        """
        self.sql_limit = "LIMIT "+str(limit)+" "

    def offset(self, offset):
        """
        Add offset clause to sql
        :param offset:
        :return:
        """
        self.sql_offset = "OFFSET "+str(offset)+" "

    def order(self, field, direction):
        """
        Add order by clause to sql

        :param field:
        :param direction:
        :return:
        """
        if direction.upper() != "ASC" and direction.upper() != "DESC":
            raise Exception("DB_EXCEPTION: wrong 'direction' provided in 'order by' clause: "+direction)
        self.sql_order = "ORDER BY "+field+" "+direction+" "

    def where(self, constraints):
        """
        Add where clause to sql

        :param constraints: list of tuples [(field, value, comparator), (field, value, comparator)]
        :return: void
        """
        for constraint in constraints:
            if self.sql_where != "":
                self.sql_where += "AND "+constraint[0]+" "+constraint[2]+" '"+str(constraint[1])+"' "
            else:
                self.sql_where = "WHERE "+constraint[0]+" "+constraint[2]+" '"+str(constraint[1])+"' "

    def setId(self, id):
        self.id = id


