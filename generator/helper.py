
#default values overriden in init file
steps_in_phase = 10
number_of_breaths = 10
take_breath_in_phase = 0 # notice: phase is float not integer
T_to_T0 = 1
heart_period = 0
breath_period = 1000

def set_steps_in_phase(newVal):
    """
    Sets global value for number of steps in phase
    :param new: Integer
    :return:
    """
    global steps_in_phase
    steps_in_phase = int(newVal)

def set_number_of_breaths(newVal):
    """
    Set number of breaths to be simulated
    :param new:
    :return:
    """
    global number_of_breaths
    number_of_breaths = int(newVal)

def setTtoT0(newVal):
    """
    Set T of heartrate / T breath param
    :param newVal:
    :return:
    """
    global T_to_T0
    T_to_T0 = float(newVal)

def set_heart_period():
    global heart_period
    global breath_period
    global T_to_T0
    heart_period = int(breath_period*T_to_T0)

def set_breath_period(newVal):
    global breath_period
    breath_period = int(newVal)
