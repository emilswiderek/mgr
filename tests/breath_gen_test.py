# test if distances between breaths are equal
import unittest
import generator.BreathGenerator as bg
import helpers.helper as hp


class TestBreathGen(unittest.TestCase):
    def test_generate(self):
        val = 1
        breathgen = bg.BreathGenerator()
        breathgen.setPhaseIterator(val)
        self.assertEqual(val+1, breathgen.generate(), "Breath generator function failed")

    def test_generateProcess(self):
        breathgen = bg.BreathGenerator()
        breathFunction = breathgen.generateProcess()
        self.assertEqual(breathFunction[0], breathFunction[hp.breath_period], "Breath function has incorrect intervals")
        self.assertEqual(len(breathFunction), hp.breath_period*hp.number_of_breaths, "Lengths doesnt match")
if __name__ == '__main__':
    unittest.main()


