# dichiaro la classe tramite la keyword class
# Studente è il nome della classe
class Studente:
    # attributo uguale per tutti all'interno della classe
    ruolo = "Studente UNITS"

    # init ha due trattini bassi davanti e dietro, funzione che viene chiamata al momento in cui si deve inizializzare un oggetto della classe. init è il costruttore della classe
    def __init__ (self, nome, cognome):
        # assegnamento all'interno della funzione
        self.nome = nome    # prendi il nome che ti è stato passato tramite la funzione e associalo al campo nome
        self.cognome = cognome  # prendi il cognome che ti è stato passato tramite la funzione e associalo al campo cognome

        # stiamo dichiarando che ogni stuudente all'interno di questa classe contiene un nome e un cognome, specifici dello studente e il ruolo comune a tutti

    # non prende nessun parametro solo self
    def hullooo(self):
        print(self.ruolo, ":", self. nome, self.cognome)
pass

# ora creiamo l'oggetto e chiamiamo la funzione hullooo() non inserisco nulla tra parentesi siccome la funzione non prende nessun parametro
obj_Angie = Studente("Angie", "Rota")
obj_Angie.hullooo()

# posso accedere al campo nome e cognome e modificare l'oggetto
print("Campo nome di Angelica: ", obj_Angie.nome)

obj_Angie.nome = "Angelica"

print("Campo nome di Angelica: ", obj_Angie.nome)