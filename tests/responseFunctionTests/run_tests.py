__author__ = 'emil'
import tests.responseFunctionTests.forwardingFunctionTest as fftest

def run_tests():
    print("--- \nResponse functions tests: ")
    print("Forwarding function test: \n---")
    test1 = fftest.TestForwardingFunction()
    test1.test_response()
    test1.test_entireSpectrumResponseShow()
    print("OK! \n---")

    print("Response function tests finished! \n---")
