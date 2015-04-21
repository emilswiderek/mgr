from generator.breath_gen import BreathGenerator
from generator.heart_gen import HeartGenerator
from responseFunction.forwardingFunction import ForwardingFunction
def main() :
    BreathGen = BreathGenerator()
    HeartGen = HeartGenerator()

    breathFunction = BreathGen.generateProcess()
    HeartGen.setBreathFunction(breathFunction)
    HeartGen.setResponseFunction(getResponseFunction('forwarding'))
    heartFunction = HeartGen.generateProcess()
    print(heartFunction)

def getResponseFunction(name) :
    # @todo set as parameter name of response function
    return {'forwarding': ForwardingFunction() }[name]

if __name__ == "__main__":
   main()