currentTitle = ""

class Console:

    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__currentTitle = ""

        return cls._instance

    def startBlock(self, title):

        self.__currentTitle = title
        print(" # ---------------------- # ")
        print(" # => " + str(self.__currentTitle) + " : Start")

    def printIteration(self, actualLine, totalLines):
        
        percentage = int(actualLine * 100 / totalLines)

        if (percentage % 5 == 0):
            print("Done : ~" + str(percentage) + "%", end="\r")

    def endBlock(self):

        print(" # => " + str(self.__currentTitle) + " : End")
        print(" # ---------------------- # \n")
        self.__currentTitle = ""

