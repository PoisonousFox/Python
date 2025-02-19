import math

class Kreis:
    def __init__(self, r, mx, my):
        self.__r = r
        self.__mx = mx
        self.__my = my

    def getMX(self):
        return self.__mx

    def getMY(self):
        return self.__my

    def getRadius(self):
        return self.__r

    def setRadius(self, r):
        self.__r = r

    def getUmfang(self):
        return (2 * math.pi * self.__r)
        
    def getInhalt(self):
        return (math.pi * (self.__r**2))


    def getAbstand(self, andererKreis):
        abmx = abs(self.__mx - andererKreis.getMX())
        abmy = abs(self.__my - andererKreis.getMY())
        abm = math.sqrt((abmx ** 2) + (abmy ** 2))
        abstand = abm - self.__r - andererKreis.getRadius()
        return abstand



    def berührt(self, andererKreis):
        if self.getAbstand(andererKreis) == 0:
            return True

        else:
            return False
        

#Test
kreis1 = Kreis(5, 0, 0)
kreis2 = Kreis(5, 10, 0)

print("Kreis 1 Radius: " + str(kreis1.getRadius()))
print("Kreis 2 Radius: " + str(kreis2.getRadius()))
print("Kreis 1 Umfang: " + str(kreis1.getUmfang()))
print("Kreis 1 Fläche: " + str(kreis1.getInhalt()))
print("Abstand zwischen Kreis 1 und Kreis 2: " + str(kreis1.getAbstand(kreis2)))
print("Berühren sich die Kreise?: " + str(kreis1.berührt(kreis2)))

