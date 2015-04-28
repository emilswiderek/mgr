__author__ = 'emil'

from tests import breath_gen_test as bgt
from tests import heart_gen_test as hgt
from tests.responseFunctionTests import run_tests as response_function_tests


print("-----------\nTests begin")
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