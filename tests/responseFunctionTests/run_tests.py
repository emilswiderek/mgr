__author__ = 'emil'
import tests.responseFunctionTests.forwardingFunctionTest as fftest
import tests.responseFunctionTests.sinusFunctionTest as sintest
import tests.responseFunctionTests.AkselrodFunctionTest as AkselrodTest


def run_tests():
    print("--- \nResponse functions tests: ")
    print("Forwarding function test: \n---")
    test1 = fftest.TestForwardingFunction()
    test1.test_response()
    test1.test_entireSpectrumResponseShow()
    print("OK! \n---")

    print("Sinus function test: \n---")
    test1 = sintest.TestSinusFunction()
    test1.test_response()
    test1.test_entireSpectrumResponseShow()
    print("OK! \n---")
    #print("Omitted \n")

    print("Akselrod function test: \n---")
    test1 = AkselrodTest.TestAkselrodFunction()
    test1.test_response()
    test1.test_entireSpectrumResponseShow()
    print("OK! \n---")

    print("Response function tests finished! \n---")
