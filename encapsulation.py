class car:
    def __init__(self):
        self.__updateSoftware()
    def drive(self):
        print("driving")
    def __updateSoftware(self):
        print("updating software")
redcar=car()
redcar.drive()
