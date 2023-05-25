class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.tfe = None
        self.diplome = None

    def assigner_tfe(self, tfe):
        self.tfe = tfe

    def valider_diplome(self):
        if self.tfe is not None and self.tfe.note >= 12:
            self.diplome = f"{self.nom} {self.prenom} a valide son diplome"
        else:
            self.diplome = f"{self.nom} {self.prenom} n'a pas valide son diplome"


class TFE:
    def __init__(self, sujet, prof_encadrement=None):
        self.sujet = sujet
        self.etudiants = []
        self.prof_encadrement = prof_encadrement
        self.note = None

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
        etudiant.assigner_tfe(self)

    def definir_note(self, note):
        self.note = note
        for etudiant in self.etudiants:
            etudiant.valider_diplome()


class Professeur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.tfe_encadres = []

    def encadrer_tfe(self, tfe):
        self.tfe_encadres.append(tfe)
        tfe.prof_encadrement = self

# Création d'étudiants, de professeurs et de TFE
etudiant1 = Etudiant("Dupont", "Jean")
etudiant2 = Etudiant("Durand", "Marie")
prof1 = Professeur("Martin", "Pierre")
tfe1 = TFE("Le Machine Learning dans les applications mobiles")
tfe2 = TFE("L'impact des réseaux sociaux sur les relations interpersonnelles")

# Assignation d'un professeur à un TFE
prof1.encadrer_tfe(tfe1)

# Ajout d'étudiants à un TFE
tfe1.ajouter_etudiant(etudiant1)
tfe2.ajouter_etudiant(etudiant2)

# Définition de la note d'un TFE
tfe1.definir_note(14)
tfe2.definir_note(10)

# Vérification de la validation du diplôme des étudiants
print(etudiant1.diplome)
print(etudiant2.diplome)
