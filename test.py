__author__ = 'emil'
from tests import breath_gen_test as bgt
from tests import heart_gen_test as hgt
from tests.responseFunctionTests import run_tests as response_function_tests
from tests.modelTests.spectrumCollectionModelTest import TestSpectrumCollectionModel
from tests.modelTests.measureModelTest import TestMeasureModel
from tests.modelTests.heartbeatsCollectionModelTest import HeartbeatsCollectionModelTest
from tests.networkTest import NetworkTest

print("-----------\nTests begin")
print("--- \nNetwork testing:")
netT = NetworkTest()
netT.test_learning()


print("--- \nModels testing:")
spectrumModelTest = TestSpectrumCollectionModel()
spectrumModelTest.test_insert_sql()
spectrumModelTest.test_multiple_insert_sql()
measureModelTest = TestMeasureModel()
measureModelTest.test_insert_sql()
heartbeatModelTest = HeartbeatsCollectionModelTest()
heartbeatModelTest.test_insert_sql()
heartbeatModelTest.test_multiple_insert_sql()
print("--- \nBreath generator testing: ")
breathTest = bgt.TestBreathGen()
breathTest.test_generate()
breathTest.test_generateProcess()
print("OK! \n---")
print("--- \nHeart generator testing: ")
heartTest = hgt.TestHeartGen()
heartTest.test_generate()

print("OK! \n---")

response_function_tests.run_tests()

print("\n-----------\nTests finished")