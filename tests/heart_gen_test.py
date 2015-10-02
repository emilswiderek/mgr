# test if distances between breaths are equal
import unittest

import generator.HeartGenerator as hg
import helpers.helper as hp
import responseFunction.forwardingFunction as ff
import generator.BreathGenerator as bg
import analysis.oneExtortionPeriodAnalysis as oexpa
import analysis.ploter as plt


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
        heartGen = hg.HeartGenerator()
        breathGen = bg.BreathGenerator()
        breath = breathGen.generateProcess()
        heartGen.setBreathFunction(breath)
        heartGen.setResponseFunction(heartGen.getResponseFunction(hp.response_function))
        heart = heartGen.generateProcess()

        analysis = oexpa.Analyzer(breath, heart)
        indexes, results, previous_step = analysis.makeMap() # map: {'previous_step': previous_step, 'next_step': results}
        response = []
        responseFunction = heartGen.getResponseFunction(hp.response_function)
        for x in previous_step:
            response.append(responseFunction.getResponse(x*hp.heart_period))

        ploter = plt.Plotter()
        ploter.plot_map_and_response_func(previous_step, response, previous_step, results)

        pass

if __name__ == '__main__':
    unittest.main()


