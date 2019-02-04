class Direction:
    UP = 1
    DOWN = -1

class Counter:
    __current_value__ = 0

    def increment(self, dir):
        self.__current_value__ += dir
        if self.__current_value__ > 15:
            self.__current_value__ = 0
        elif self.__current_value__ < 0:
            self.__current_value__ = 15
        return self

    def toBin(self):
        return map(
            lambda x: True if x == '1' else False,
            list("{:04b}".format(self.__current_value__))
        )

    def __str__(self):
        return str(self.__current_value__) + "        " + "{:04b}".format(self.__current_value__)
