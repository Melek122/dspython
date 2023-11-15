class Livre:
    def __init__(self, titre, auteur, prix, nombre_pages):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        self.nombre_pages = nombre_pages
        self.proprietaire = None

    def acheter(self, nouveau_proprietaire):
        if self.proprietaire is None:
            self.proprietaire = nouveau_proprietaire

    def __str__(self):
        return f"{self.titre} - {self.auteur} - {self.prix}€ - {self.nombre_pages} pages - Propriétaire: {self.proprietaire}"


class BD(Livre):
    def __init__(self, titre, auteur, prix, nombre_pages, enCouleur=False):
        super().__init__(titre, auteur, prix, nombre_pages)
        self.enCouleur = enCouleur

    def echanger(self, autre_bd):
        if self.proprietaire is not None and autre_bd.proprietaire is not None \
                and not self.proprietaire == autre_bd.proprietaire \
                and self.prix == autre_bd.prix:
            self.proprietaire, autre_bd.proprietaire = autre_bd.proprietaire, self.proprietaire

    def __str__(self):
        couleur_str = "En couleur" if self.enCouleur else "En noir et blanc"
        return super().__str__() + f" - {couleur_str}"


class BibDeClasse:
    def __init__(self):
        self.livres = []

    def ajouter(self, livre):
        if livre not in self.livres:
            self.livres.append(livre)

    def supprimer(self, livre):
        if livre in self.livres:
            self.livres.remove(livre)

    def afficher(self):
        for livre in self.livres:
            print(livre)


# Test
hp = Livre("Harry Potter", "J. K. Rowling", 79.9, 350)
print(hp)
print()
hp.acheter("Hatem")
hp.acheter("Hatem")
print(hp)
print()

tintin1 = BD("Tintin en Amérique", "Hergé", 40.0, 80, enCouleur=True)
tintin2 = BD("Tintin au Congo", "Hergé", 40.0, 80, enCouleur=True)
tintin1.echanger(tintin2)
print()
print(tintin2)
print()

bibrsi2 = BibDeClasse()
bibrsi2.ajouter(tintin1)
bibrsi2.ajouter(tintin2)
bibrsi2.ajouter(hp)
bibrsi2.ajouter(tintin1)
bibrsi2.supprimer(tintin1)
bibrsi2.supprimer(tintin1)
bibrsi2.ajouter(tintin1)
print()
bibrsi2.afficher()
