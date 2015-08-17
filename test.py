__author__ = 'emil'
import os
from tests import breath_gen_test as bgt
from tests import heart_gen_test as hgt
from tests.responseFunctionTests import run_tests as response_function_tests
from tests.modelTests.spectrumCollectionModelTest import TestSpectrumCollectionModel

print("-----------\nTests begin")
print("--- \nModels testing:")
spectrumModelTest = TestSpectrumCollectionModel()
spectrumModelTest.test_insert_sql()
spectrumModelTest.test_multiple_insert_sql()
os._exit(1)
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