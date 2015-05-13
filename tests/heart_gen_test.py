# test if distances between breaths are equal
import unittest
import generator.heart_gen as hg
import generator.helper as hp
import responseFunction.forwardingFunction as ff


class TestHeartGen(unittest.TestCase):
    def test_generate(self):
        val = 1
        heartgen = hg.HeartGenerator()
        heartgen.setPhaseIterator(val)
        heartgen.breathPhase = hp.take_breath_in_phase
        response_function = ff.ForwardingFunction()
        heartgen.setResponseFunction(ff.ForwardingFunction())
        self.assertEqual(heartgen.generate(), val+response_function.getResponse(val)*hp.heart_period, "Heart generator doesnt call for response function when needed!")

    def test_generateProcess(self):
        pass

if __name__ == '__main__':
    unittest.main()


