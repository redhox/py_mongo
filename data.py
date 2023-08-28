class Element :
    def __init__(self, element_lu) :
        self.nom = element_lu["nom"]
        self.prenom = element_lu["prénom"]
    
    def set_discipline(self, discipline):
        self.discipline = discipline
    
    def set_titre(self,titre):
        self.titre = titre

    def to_json(self):
        element_json = {"nom":self.nom, "prénom":self.prenom, "titre":self.titre}
        return element_json
    