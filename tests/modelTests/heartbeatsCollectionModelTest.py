# test if distances between breaths are equal
import unittest

from model.HeartbeatsCollectionModel import HeartbeatsCollectionModel
import helpers.helper as hp


class HeartbeatsCollectionModelTest(unittest.TestCase):
    def test_insert_sql(self):
        obj = HeartbeatsCollectionModel()
        obj.setMeasureId(1)
        obj.setHeartPhase(20)
        obj.setBreathPhase(21)

        sql = obj._insertSQL()
        testSQL = "INSERT INTO mgr.heartbeats (measure_id, heart_phase, breath_phase) VALUES (1, 20, 21)"
        self.assertEqual(testSQL, sql, "SQL one row insert error")

    def test_multiple_insert_sql(self):
        obj = HeartbeatsCollectionModel()
        obj.setMeasureId(1)
        obj.setHeartPhase([1, 9, 11])
        obj.setBreathPhase([1, 2, 3])

        sql = obj._insertSQL()
        testSQL = "INSERT INTO mgr.heartbeats (measure_id, heart_phase, breath_phase) VALUES (1, 1, 1), (1, 9, 2), (1, 11, 3)";
        self.assertEqual(testSQL, sql, "SQL multi row insert error")


if __name__ == '__main__':
    unittest.main()


