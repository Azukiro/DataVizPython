currentTitle = ""

class Console:

    _instance = None

    def __init__(self):
        """
            On utilise aussi un singleton.
            Ne pas utiliser ce constructeur.
        """
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        """
            Récupérer l'unique instance de Console
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__currentTitle = ""

        return cls._instance

    def startBlock(self, title):
        """
            Ecrire sur la console un bloc avec un titre
        """

        self.__currentTitle = title
        print(" # ---------------------- # ")
        print(" # => " + str(self.__currentTitle) + " : Start")

    def printIteration(self, actualLine, totalLines):
        """
            Afficher l'avancement en pourcentage du parcours d'une boucle
        """

        if (totalLines <= 0):
            raise Exception("Invalid parameters!")
        
        displayLine = actualLine + 1
        percentage = round(displayLine * 100 / totalLines) 
        endLine = "\r" if displayLine != totalLines else "\n" 
        
        print(" Done : ~" + str(percentage) + "% (line " + str(displayLine) + " / " + str(totalLines) + ")", end=endLine)

    def endBlock(self):
        """
            Fermer le dernier bloc ouvert
        """
        
        print(" # => " + str(self.__currentTitle) + " : End")
        print(" # ---------------------- # \n")
        self.__currentTitle = ""

