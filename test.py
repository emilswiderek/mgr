__author__ = 'emil'

from tests import breath_gen_test as bgt
from tests import heart_gen_test as hgt

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

print("\n-----------\nTests finished")