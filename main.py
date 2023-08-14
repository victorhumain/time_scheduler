jours = ["lundi", "mardi", "mercredi","jeudi","vendredi"]

heures1 = ["07h00-07h55","07h55-8h50","8h50-9h45","10h05-11h00","11h55-12h00","15h-15h55","15h55-16h00"] 
heures2 = ["07h00-07h55","07h55-8h50","8h50-9h45","10h05-11h00","11h55-12h00"]

classes = []
enseignants = []
configuration_types = {"2ndeA" : {
                "Mathématiques":{"A":4,"B":0},
                "Français":{"A":4,"B":0},
                "Physique-chimie":{"A":3,"B":0},
                "Anglais":{"A":4,"B":0},
                "Histoire":{"A":2,"B":0},
                "ECM":{"A":2,"B":0},
                "EPS":{"A":3,"B":0},
                "SVT":{"A":3,"B":0},
            },"2ndeD":{
                "Mathématiques":{"A":5,"B":0},
                "Français":{"A":4,"B":0},
                "Physique-chimie":{"A":3,"B":0},
                "Anglais":{"A":3,"B":0},
                "Histoire":{"A":2,"B":0},
                "ECM":{"A":2,"B":0},
                "EPS":{"A":3,"B":0},
                "SVT":{"A":3,"B":0},
            },"1ereA":{
                "Mathématiques":{"A":5,"B":0},
                "Français":{"A":5,"B":0},
                "Physique-chimie":{"A":5,"B":0},
                "Anglais":{"A":5,"B":0},
                "Histoire":{"A":5,"B":0},
                "ECM":{"A":5,"B":0},
                "EPS":{"A":5,"B":0},
                "SVT":{"A":5,"B":0},
            },"1ereD":{
                "Mathématiques":{"A":5,"B":0},
                "Français":{"A":5,"B":0},
                "Physique-chimie":{"A":5,"B":0},
                "Anglais":{"A":5,"B":0},
                "Histoire":{"A":5,"B":0},
                "ECM":{"A":5,"B":0},
                "EPS":{"A":5,"B":0},
                "SVT":{"A":5,"B":0},
            },"1ereC":{
                "Mathématiques":{"A":5,"B":0},
                "Français":{"A":5,"B":0},
                "Physique-chimie":{"A":5,"B":0},
                "Anglais":{"A":5,"B":0},
                "Histoire":{"A":5,"B":0},
                "ECM":{"A":5,"B":0},
                "EPS":{"A":5,"B":0},
                "SVT":{"A":5,"B":0},
            },"TleA":{
                "Mathématiques":{"A":5,"B":0},
                "Français":{"A":5,"B":0},
                "Physique-chimie":{"A":5,"B":0},
                "Anglais":{"A":5,"B":0},
                "Histoire":{"A":5,"B":0},
                "ECM":{"A":5,"B":0},
                "EPS":{"A":5,"B":0},
                "SVT":{"A":5,"B":0},
            },
            "TleD":{
                "Mathématiques":{"A":5,"B":0},
                "Français":{"A":5,"B":0},
                "Physique-chimie":{"A":5,"B":0},
                "Anglais":{"A":5,"B":0},
                "Histoire":{"A":5,"B":0},
                "ECM":{"A":5,"B":0},
                "EPS":{"A":5,"B":0},
                "SVT":{"A":5,"B":0},
            },
            "TleC":{
                "Mathématiques":{"A":5,"B":0},
                "Français":{"A":5,"B":0},
                "Physique-chimie":{"A":5,"B":0},
                "Anglais":{"A":5,"B":0},
                "Histoire":{"A":5,"B":0},
                "ECM":{"A":5,"B":0},
                "EPS":{"A":5,"B":0},
                "SVT":{"A":5,"B":0},
            }
}

class Classe:
    def __init__(self,name,matiere):
        self.name = name
        self._matiere = matiere

nbre_classe = int(input("enter le nombre de classe"))

for _ in range(nbre_classe):
    name = input("rentrez le nom de la classe")
    type = input("Entrez le type de la clase 2ndeA, 2ndeD, 1ereA ...")
    matiere = configuration_types[type]
    classes.append(Classe(name,matiere))


class Enseignant:
    def __init__(self,name,matieres):
        self.name = name
        self.matieres_enseignees = matieres
        self._nbre_de_cours = 0

nbre_enseignant = int(input("enter le nombre d'enseignant"))
for _ in range(nbre_enseignant):
    name = input("rentrez le nom de l'enseignant")
    nbre_matiere = int(input("enter le nombre de matière fait par l'enseignant"))
    matieres = []
    for i in range(nbre_matiere):
        matieres.append(input("Entrez le nom de la matière"))
    classes.append(Classe(name,matieres))

def get_Enseignants_matiere(matiere, liste_enseignants):
    enseignants_matiere = []
    for enseignant in liste_enseignants:
        if matiere in enseignant.matieres_enseignees:
            enseignants_matiere.append(enseignant)
    return enseignants_matiere
#def select_matiere(matieres):
#    score = []
#    for mat in matieres:
#        heures_restantes = 


for classe in classes:
    emploi_du_temps = {
        "Lundi": {},
        "Mardi": {},
        "Mercredi": {},
        "Jeudi": {},
        "Vendredi": {},
    }
    for jour in jours:
        heures = []
        if jour == "mercredi":
            heures = heures2
        else:
            heures = heures1
        for heure in heures:
            matieres = []
            # On cherche quelles sont les matières qui peuvent occuper cette place
            # Les heures de cours par semaine max n'est pas encore atteint et il y a des enseignants disponibles pour le faire 
            for matiere in classe._matiere.items():
                enseignants = []
                for ens in get_Enseignants_matiere(matiere[0],enseignants):
                    if ens.nbre_de_cours < 20:
                        enseignants.append(ens)
                if(len(enseignants) and (matiere.duree_attribue >= matiere.duree_a_faire)):
                    matieres.append([matiere,enseignants])
            #on a la liste des matières qui peuvent occuper la place
            #il faut choisir celui qui choisit le plus de contraintes
            matiere_choisie = select_matiere(matieres)
            emploi_du_temps[jour][heure] = matiere_choisie
            Enseignant.nbre_de_cours += 1
            matiere.duree_attribue += 1
print(emploi_du_temps)