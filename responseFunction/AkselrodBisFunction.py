from responseFunction.Akselrod import Akselrod


class AkselrodBisFunction(Akselrod):

    def __init__(self):
        """
            Only parameters differ from original function
        :return:
        """
        super(AkselrodBisFunction, self).__init__()
        self.d = 0.15
        self.omega = 0.20
        self.a = 0.2