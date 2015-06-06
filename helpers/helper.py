# default values overridden in init file

number_of_breaths = 10
take_breath_in_phase = 1  # notice: phase is float not integer
T_to_T0 = 1
heart_period = 0
breath_period = 1000
# for extortion spectrum:
min_breath_period = 100
max_breath_period = 200
response_function = 'sinus'
map_fitting_degree = 10
show_plots = False


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


def set_heart_period(default):
    global heart_period
    global breath_period
    global T_to_T0
    if not default:
        heart_period = int(breath_period * T_to_T0)
    else:
        heart_period = default


def set_breath_period(newVal):
    global breath_period
    breath_period = int(newVal)


def set_min_breath_period(newVal):
    global min_breath_period
    min_breath_period = int(newVal)


def set_max_breath_period(newVal):
    global max_breath_period
    max_breath_period = int(newVal)


def calculateTtoT0():
    """
    Recalculated T to To based on current periods of heart and breath
    :return:
    """
    global T_to_T0
    T_to_T0 = heart_period / breath_period


def set_response_function(name):
    """

    :param name:
    :return:
    """
    global response_function
    response_function = name


def set_map_fitting_degree(value):
    global map_fitting_degree
    map_fitting_degree = int(value)


def set_show_plots(value):
    global show_plots
    show_plots = bool(value)
