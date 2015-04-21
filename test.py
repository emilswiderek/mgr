__author__ = 'emil'

from tests import breath_gen_test as bgt

print("-----------\nTests begin")
print("--- \nBreath generator testing: ")
breathTest = bgt.TestBreathGen()
breathTest.test_generate()
breathTest.test_generateProcess()
print("OK! \n---")

print("\n-----------\nTests finished")