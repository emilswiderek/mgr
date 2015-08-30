from responseFunction.forwardingFunction import ForwardingFunction


class ForwardingFunction2(ForwardingFunction):

    def __init__(self):
        """
            Only parameters differ from original function
        :return:
        """
        super(ForwardingFunction2, self).__init__()
        self.forward_step = 0.3