from responseFunction.Akselrod import Akselrod


class Akselrodian(Akselrod):

    def __init__(self):
        """
            Only parameters differ from original function
        :return:
        """
        super(Akselrodian, self).__init__()
        self.d = 0.12
        self.omega = 0.55
        self.a = 0.43