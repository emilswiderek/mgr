
#default values overriden in init file
steps_in_phase = 10
number_of_breaths = 10
take_breath_in_phase = 0 # notice: phase is float not integer

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
