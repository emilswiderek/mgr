# test if distances between breaths are equal
import unittest

from model.MeasureModel import MeasureModel


class TestMeasureModel(unittest.TestCase):
    def test_insert_sql(self):
        obj = MeasureModel()
        obj.setMeasureType("test")
        obj.setBreathPeriod(100)
        obj.setBreathNumber(101)
        obj.setHeartPeriod(200)

        sql = obj._insertSQL()
        testSQL = "INSERT INTO `"+obj.db.db_name+"`.`"+obj.TABLE_NAME+"` (measure_type, breath_period, heart_period, min_breath_period, max_breath_period, breath_number, response_function) VALUES ('test', 100, 200, NULL, NULL, 101, 'NULL')"
        self.assertEqual(testSQL, sql, "SQL one row insert error")

if __name__ == '__main__':
    unittest.main()


