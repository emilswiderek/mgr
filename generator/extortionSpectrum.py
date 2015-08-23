__author__ = 'emil'
from helpers import helper as hp
from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from model.MeasureModel import MeasureModel
from model.HeartbeatsCollectionModel import HeartbeatsCollectionModel
import time  #  tqdm needs it
from vendor.tqdm.tqdm import *


class ExtortionSpectrumGenerator:

    def __init__(self):
        self.min_breath = hp.min_breath_period
        self.max_breath = hp.max_breath_period

    def generate(self):
        for breath_period in tqdm(range(self.min_breath, self.max_breath)):

            BreathGen = BreathGenerator()
            HeartGen = HeartGenerator()
            HeartGen.setResponseFunction(HeartGen.getResponseFunction(hp.response_function))

            hp.set_breath_period(breath_period)
            hp.calculateTtoT0()

            measure = MeasureModel()
            measure.setHeartPeriod(hp.heart_period)
            measure.setMinBreathPeriod(hp.min_breath_period)
            measure.setResponseFunction(hp.response_function)
            measure.setMaxBreathPeriod(hp.max_breath_period)
            measure.setBreathNumber(hp.number_of_breaths)
            measure.setMeasureType(MeasureModel.TYPE_GENERATE_EXTORTION)
            measure.setBreathPeriod(breath_period)
            measureId = measure.save()

            del measure

            breath = BreathGen.generateProcess()

            del BreathGen

            HeartGen.setBreathFunction(breath)

            heartbeats = HeartbeatsCollectionModel()
            heartbeats.setMeasureId(measureId)
            heartbeats.setHeartPhase(HeartGen.generateProcess())
            heartbeats.setBreathPhase(breath)
            heartbeats.save()

            del HeartGen
            del heartbeats
