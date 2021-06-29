#creiamo una classe

class primaclasse:
    "Ho creato la prima classe"
    pass

print(primaclasse.__doc__)


class secondaclasse:
    "Ho creato la seconda classe"
    
    def fun(self): #def lo usiamo per definire una funzione
        print('Stampa di prova')
    pass

print(secondaclasse.__doc__)