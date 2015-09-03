from responseFunction.forwardingFunction import ForwardingFunction


class ForwardingBisFunction(ForwardingFunction):

    def __init__(self):
        """
            Only parameters differ from original function
        :return:
        """
        super(ForwardingBisFunction, self).__init__()
        self.forward_step = 0.1