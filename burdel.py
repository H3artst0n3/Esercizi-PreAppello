# questa è una superclasse
class Persona:
    def __init__(self, ruolo, nome, cognome, age):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
        self.age = age
    
    def hullooo(self):
        print(self.ruolo, ":", self.nome, self.cognome, self.age)

# ora creo la sottoclasse studente
class Studente(Persona):
    # per definire la classe studente necessito delle informazioni anche che appartengono alla superclasse "Persona" (che come informazioni contiene il ruolo, il nome e il cognome) 

    # scrivo la funzione init prendendo come compi il nome, il cognome e il corso che lo studente segue
    def __init__(self, nome, cognome, age, corso):
        # chiamo la superclasse mettendo come parametri: in modo esplicito il ruolo che sarà fissato per tutti gli studenti e poi il campo nome e cognome presi come parametri dalla funzione costruttore della superclasse
        super().__init__("\nStudente UNITS", nome, cognome, age)
        self.corso = corso
    
    # posso ridefinire il metodo hullooo così che per lo studente venga indicato anche il corso che frequenta
    def hullooo(self):
        Persona.hullooo(self)
        print("Frequenta il corso:", self.corso)

class Docente(Persona):
    # seguo praticamente quello che ho fatto per la classe studente modificando solamente le parti dei print dove al posto di: "Studente UNITS" ci sarà: "Docente UNITS" e al posto di: ">>>Frequenta il corso:" ci sarà: ">>>Docente del corso:"

    def __init__(self, nome, cognome, age, corso):
        super().__init__("\nDocente UNITS", nome, cognome, age)
        self.corso = corso
    
    # posso ridefinire il metodo hullooo così che per lo studente venga indicato anche il corso che frequenta
    def hullooo(self):
        if (self.age > 40):
            self.age = ">40"
        Persona.hullooo(self)
        print(">>>Docente del corso:", self.corso)

class TecnicoAmministrativo(Persona):
    # seguo praticamente quello che ho fatto per la classe studente mettendo al posto del corso l'edificio dove sono operativi

    def __init__(self, nome, cognome, age, edificio):
        super().__init__("\nTecnico UNITS", nome, cognome, age)
        self.edificio = edificio
    
    # posso ridefinire il metodo hullooo così che per lo studente venga indicato anche il corso che frequenta
    def hullooo(self):
        Persona.hullooo(self)
        print(">>>Edificio:", self.edificio)



# creo un oggetto e chiamo la funzione hullooo()
obj_Angie = Studente("Angelica", "Rota", 20, "Programmazione")
obj_Angie.hullooo()

obj_Stef = Studente("Stefano", "Tumino", 19, "Analisi II")
obj_Stef.hullooo()

obj_Gio = Studente("Giovanni", "Pesaturo", 20, "Fisica")
obj_Gio.hullooo()

obj_otherStef = Docente("Stefano Alberto", "Russo", 35, "Laboratorio di Programmazione")
obj_otherStef.hullooo()

obj_Daniele = Docente("Daniele", "Del Santo", 50, "Analisi I")
obj_Daniele.hullooo()

obj_Giulio = TecnicoAmministrativo("Giulio", "Caravagna", 38, "H3")
obj_Giulio.hullooo()