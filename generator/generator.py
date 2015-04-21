import generator.helper as hp

class Generator(object):

    def __init__(self):
        self.phase_iterator = -1 #only for initialisation
        self.process = []
        self.generation_step = 1 / hp.steps_in_phase

    def generate(self):
        pass

    def generateProcess(self):
        pass

    def setPhaseIterator(self, newVal):
        self.phase_iterator = newVal