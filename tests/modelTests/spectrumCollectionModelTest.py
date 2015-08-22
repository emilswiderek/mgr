# test if distances between breaths are equal
import unittest

from model.spectrumCollectionModel import SpectrumCollectionModel
import helpers.helper as hp


class TestSpectrumCollectionModel(unittest.TestCase):
    def test_insert_sql(self):
        obj = SpectrumCollectionModel()
        obj.setMeasureId(1)
        obj.setMeanRR(0.01)
        obj.setBreathPeriod(100)
        obj.setStDev(10.0)

        sql = obj._insertSQL()
        testSQL = "INSERT INTO mgr.spectrum (measure_id, mean_rr, stdev, breath_period) VALUES (1, 0.01, 10.0, 100)"
        self.assertEqual(testSQL, sql, "SQL one row insert error")

    def test_multiple_insert_sql(self):
        obj = SpectrumCollectionModel()
        obj.setMeasureId(1)
        obj.setMeanRR([0.01, 0.02, 0.03])
        obj.setBreathPeriod([100, 101, 102])
        obj.setStDev([10.0, 11.2, 11.3])

        sql = obj._insertSQL()
        testSQL = "INSERT INTO mgr.spectrum (measure_id, mean_rr, stdev, breath_period) VALUES (1, 0.01, 10.0, 100), (1, 0.02, 11.2, 101), (1, 0.03, 11.3, 102)";
        self.assertEqual(testSQL, sql, "SQL multi row insert error")


if __name__ == '__main__':
    unittest.main()


