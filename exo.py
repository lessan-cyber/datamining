class CompteBancaire:
    def __init__(self, numero_compte, nom_titulaire, solde_initial=0):
        """
        Constructeur de la classe CompteBancaire.
        
        :param numero_compte: Le numéro de compte (str ou int).
        :param nom_titulaire: Le nom du titulaire du compte (str).
        :param solde_initial: Le solde initial du compte (float, par défaut 0).
        """
        self.numero_compte = numero_compte  # Attribut : numéro de compte
        self.nom_titulaire = nom_titulaire  # Attribut : nom du titulaire
        self.solde = solde_initial  # Attribut : solde du compte

    def afficher_solde(self):
        """
        Affiche le solde actuel du compte.
        """
        print(f"Solde actuel : {self.solde} €")

    def deposer(self, montant):
        """
        Dépose un montant sur le compte.
        
        :param montant: Le montant à déposer (float).
        """
        if montant > 0:  # Vérifie que le montant est positif
            self.solde += montant
            print(f"{montant} € déposés. Nouveau solde : {self.solde} €")
        else:
            print("Erreur : Le montant doit être positif.")

    def retirer(self, montant):
        """
        Retire un montant du compte, si le solde est suffisant.
        
        :param montant: Le montant à retirer (float).
        """
        if montant > 0:  # Vérifie que le montant est positif
            if self.solde >= montant:  # Vérifie que le solde est suffisant
                self.solde -= montant
                print(f"{montant} € retirés. Nouveau solde : {self.solde} €")
            else:
                print("Erreur : Solde insuffisant.")
        else:
            print("Erreur : Le montant doit être positif.")

    def afficher_infos(self):
        """
        Affiche les informations du compte (numéro, titulaire, solde).
        """
        print("\nInformations du compte :")
        print(f"Numéro de compte : {self.numero_compte}")
        print(f"Titulaire : {self.nom_titulaire}")
        print(f"Solde : {self.solde} €")
        
# Création d'un compte bancaire
compte = CompteBancaire(numero_compte="123456", nom_titulaire="Alice Dupont", solde_initial=1000)

# Affichage des informations initiales
compte.afficher_infos()

# Dépôt d'argent
compte.deposer(500)

# Retrait d'argent
compte.retirer(200)

# Tentative de retrait avec solde insuffisant
compte.retirer(2000)

# Affichage des informations finales
compte.afficher_infos()