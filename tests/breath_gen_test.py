# test if distances between breaths are equal
import unittest
import generator.breath_gen as bg
import generator.helper as hp

class TestBreathGen(unittest.TestCase):
    def test_generate(self):
        val = 1
        breathgen = bg.BreathGenerator()
        breathgen.setPhaseIterator(val)
        self.assertEqual(val+1, breathgen.generate(), "Breath generator function failed")

    def test_generateProcess(self):
        breathgen = bg.BreathGenerator()
        breathFunction = breathgen.generateProcess()
        self.assertEqual(breathFunction[0], breathFunction[hp.steps_in_phase], "Breafth function has incorrect intervals")
        self.assertEqual(len(breathFunction), hp.steps_in_phase*hp.number_of_breaths, "Lenghts doesnt match")
if __name__ == '__main__':
    unittest.main()


