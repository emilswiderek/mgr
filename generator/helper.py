
steps_in_phase = 1000
number_of_breaths = 100

def set_steps_in_phase(new):
    """
    Sets global value for number of steps in phase
    :param new: Integer
    :return:
    """
    global steps_in_phase
    steps_in_phase = new

def set_number_of_breaths(new):
    """
    Set number of breaths to be simulated
    :param new:
    :return:
    """
    global number_of_breaths
    number_of_breaths = new
