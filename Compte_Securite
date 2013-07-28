#-*-coding:Latin-1-*
from fonctions import *
import tkinter
from tkinter import *
from getpass import getpass
import hashlib




class Fenetre(tkinter.Frame):
    """Classe pour creer une fenetre d'affichage"""

    
    def __init__(self, master):
        """Constructeur de la fenetre"""
        
        tkinter.Frame.__init__(self, master)
        self.tableau = tkinter.Frame(self)

        
    def effacer(self):
        """vider la fenetre de tout contenu"""
        
        self.tableau.destroy()  #on enleve le tableau de la surface


    def ecrire(self):
        """reinitialiser la fenetre"""
        
        self.pack(anchor = CENTER)  #on affiche notre surface
        self.tableau = tkinter.Frame(self)  #on cree un tableau
        self.tableau.pack() #qu'on affiche sur notre surface



        
def accueil():
    """Affichage de la page d'accueil"""

    # on efface le tableau
    fenetrePrincipale.effacer()
    fenetrePrincipale.ecrire()

    # on place nos boutons connexion et inscription
    boutonConnecter = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                            text = "Connexion", command = connexion)
    infosConnecter = tkinter.Label(fenetrePrincipale.tableau, text = "Si vous \
deja un compte cliquez sur le bouton connexion", font = police3)
    boutonInscription = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                            text = "Inscription", command = inscription)
    infosInscription = tkinter.Label(fenetrePrincipale.tableau, text = "Si vous \
n'avez pas de compte, cliquez sur Inscription", font = police3)
    boutonConnecter.pack(pady = 50)
    boutonInscription.pack(pady = 50)
    infosConnecter.pack(before = boutonConnecter)
    infosInscription.pack(before = boutonInscription)



    
def inscription():
    """Page ou l'on entre les donnees pour l'inscription"""


    def valider():
        """Verification des donnees entrees"""
        
        #recuperation des donnees entrees
        pseudo = pseudoVar.get()
        passe = passeVar.get()
        passeConfirmation = passeConfirmationVar.get()
        nom = nomVar.get()
        prenom = prenomVar.get()
        
        #verification de la compatibilite des deux mots de passe

        #si les mots de passe ne sont pas compatibles
        if len(passe) < 4 or passe != passeConfirmation:
            
            #on affiche un message d'erreur
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            messageErreur = tkinter.Label(fenetrePrincipale.tableau,
                                font = police, text = "Erreur lors de \
l'enregistrement:", foreground = "red")
            informationsErreur = tkinter.Label(fenetrePrincipale.tableau,
                                     text = "Vos mots de passe ne sont\
pas compatibles", font = police2)
            messageErreur.pack(pady = 50)
            informationsErreur.pack(pady = 50)

            #on cree un bouton retour vers la page d'inscription
            boutonRetour = tkinter.Button(fenetrePrincipale.tableau,
                             font = police2, text = "Reessayer",
                                          command = inscription)
            boutonRetour.pack(pady = 50)
            
        #si les mots de passes sont compatibles
        else:
            
            # on encode le mot passe
            passe = passe.encode()
            passe = hashlib.sha1(passe).hexdigest()
            utilisateur = creerUtilisateur(pseudo, passe, nom, prenom)
            
            #puis on verifie si lexistence de l'utilisateur
            
            #Si cet utilisateur n'existe pas (pseudo non existant)
            if utilisateur:

                #on efface le tableau
                fenetrePrincipale.effacer()
                fenetrePrincipale.ecrire()
                #on affiche un message de suucces
                messageSucces = tkinter.Label(fenetrePrincipale.tableau,
                                    font = police, foreground = "green",
                                    text = "Inscription terminee avec succes")
                messageSucces.pack(pady = 50)
                infosCompte = "Pseudo : {}\nNom : {}\nPrenom : {}"\
                               .format(pseudo, nom, prenom)
                informationsCompte = tkinter.Label(fenetrePrincipale.tableau,
                                        font = police2, text = infosCompte)
                informationsCompte.pack()
                boutonAccueil = tkinter.Button(fenetrePrincipale.tableau,
                                    font = police2, text = "Accueil",
                                    command = accueil)
                boutonAccueil.pack(pady = 90)
                
            #si ce utilisateur existe deja
            else:
                
                #on affiche un message d'erreur
                fenetrePrincipale.effacer()
                fenetrePrincipale.ecrire()
                messageErreur = tkinter.Label(fenetrePrincipale.tableau,
                                    font = police, foreground = "red",
                                    text = "Erreur lors de l'enregistrement:")
                informationsErreur = tkinter.Label(fenetrePrincipale.tableau,
                                              text = "Ce pseudo existe deja",
                                                   font = police2)
                messageErreur.pack(pady = 150)
                informationsErreur.pack()
                
                #on cree un bouton retour vers la page d'inscription
                boutonRetour = tkinter.Button(fenetrePrincipale.tableau,
                                    text = "Reessayer", font = police2,
                                              command = inscription)
                boutonRetour.pack(pady = 50)

                
    #on fait le vide dans la fenetre
    fenetrePrincipale.effacer()
    fenetrePrincipale.ecrire()
    
    #on demande a l'utilisateur de choisir ses parametres
    texte = tkinter.Label(fenetrePrincipale.tableau, text = "Veuillez remplir \
les champs suivants pour continuer", font = police3)
    texte.pack(pady = 10)
    
    #choix du pseudo
    pseudoVar = tkinter.StringVar()
    pseudoSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = pseudoVar,
                                 relief = GROOVE, width = 35, font = police2)
    pseudoSaisie.pack(pady = 5)
    pseudoLabel=tkinter.Label(fenetrePrincipale, text = "Choisissez un Pseudo",
                              font = police2)
    pseudoLabel.pack(before = pseudoSaisie)
    
    #le mot de passe
    passeVar = tkinter.StringVar()
    passeSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = passeVar,
                                show = "#", relief = GROOVE, width = 35,
                                font = police2)
    passeSaisie.pack(pady = 5)
    passeLabel=tkinter.Label(fenetrePrincipale, text = "Choisissez \
un mot de passe", font = police2)
    passeLabel.pack(before = passeSaisie)

    #Confirmation du mot de passe
    passeConfirmationVar = tkinter.StringVar()
    passeConfirmationSaisie = tkinter.Entry(fenetrePrincipale.tableau,
                                    text = passeConfirmationVar, show = "#",
                                    relief = GROOVE, width = 35, font = police2)
    passeConfirmationSaisie.pack(pady = 5)
    passeCLabel=tkinter.Label(fenetrePrincipale, text = "Confirmez le mot \
de passe", font = police2)
    passeCLabel.pack(before = passeConfirmationSaisie)

    #Son nom
    nomVar = tkinter.StringVar()
    nomSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = nomVar,
                                 relief = GROOVE, width = 35, font = police2)
    nomSaisie.pack(pady = 5)
    nomLabel=tkinter.Label(fenetrePrincipale, text = "Entrez votre nom",
                           font = police2)
    nomLabel.pack(before = nomSaisie)
  
    #Son prenom
    prenomVar = tkinter.StringVar()
    prenomSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = prenomVar,
                                 relief = GROOVE, width = 35, font = police2)
    prenomSaisie.pack(pady = 5)
    prenomLabel=tkinter.Label(fenetrePrincipale, text = "Entrez votre prenom",
                              font = police2)
    prenomLabel.pack(before = prenomSaisie)
    
    #on cree un bouton executer
    boutonExecuter = tkinter.Button(fenetrePrincipale.tableau, text = "Valider",
                                    font = police2, command = valider)
    boutonExecuter.pack(side = LEFT, padx = 75, pady = 25)
    
    #on cree un bouton retour
    boutonRetour = tkinter.Button(fenetrePrincipale.tableau, text = "Accueil",
                                  font = police2,command = accueil)
    boutonRetour.pack(side = RIGHT, padx = 75, pady = 25)
            



def connexion():
    """Page de connexion"""


    def verifier():
        """verification du pseudo et mot de passe"""

        global utilisateur
        
        #on recupere le pseudo , le mot de passe et on l'encode
        pseudo = pseudoVar.get()
        passe = passeVar.get()
        passe = passe.encode()
        passe = hashlib.sha1(passe).hexdigest()

        # on tente la connexion
        utilisateur = connexionUtilisateur(pseudo, passe)

        #si la connexion est reussie
        if utilisateur:
            
            #on efface le tableau
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            
            #on affiche un message de succes
            messageSucces = tkinter.Label(fenetrePrincipale.tableau,
                                text = "Connexion Reussie", font = police2)
            messageSucces.pack(pady = 150)            
            
            #on cree le bouton accueil bouton accueil
            boutonOk = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                text = "Ok", command = action)
            boutonOk.pack(after = messageSucces)

        #si connexion non reussie
        else:
            
            #on efface le tableau
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            
            #on affiche un message d'erreur
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            messageErreur = tkinter.Label(fenetrePrincipale.tableau,
                                 font = police,text = "Erreur Connexion :",
                                          foreground = "red")
            informationsErreur = tkinter.Label(fenetrePrincipale.tableau,
                                     text = "Identifiant et/ou \
mot de passe incorrects", font = police2)
            messageErreur.pack(pady = 50)
            informationsErreur.pack(pady =50)

            #on cree un bouton retour vers la page d'inscription
            boutonRetour = tkinter.Button(fenetrePrincipale.tableau,
                                text = "Reessayer", font = police2,
                                          command = connexion)
            boutonRetour.pack(side = LEFT, pady = 30)

            #on cree un bouton inscription
            boutonInscription = tkinter.Button(fenetrePrincipale.tableau,
                                text = "Nouveau compte", font = police2,
                                               command = inscription)
            boutonInscription.pack(side = RIGHT, pady = 30)

            
    #on fait le vide dans la fenetre
    fenetrePrincipale.effacer()
    fenetrePrincipale.ecrire()

    #on demande a l'utilisateur d'entrer ses parametres d'identification
    infosConnecter = tkinter.Label(fenetrePrincipale.tableau, text = "Entrez vos \
informations de connexion", font = police3)
    infosConnecter.pack(pady = 50)
        
    #choix du pseudo
    pseudoVar = tkinter.StringVar()
    pseudoSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = pseudoVar,
                                 relief = GROOVE, width = 35, font = police2)
    pseudoSaisie.pack(pady = 5)
    pseudoLabel=tkinter.Label(fenetrePrincipale, text = "Votre Pseudo",
                              font = police2)
    pseudoLabel.pack(before = pseudoSaisie)
    
    #le mot de passe
    passeVar = tkinter.StringVar()
    passeSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = passeVar,
                                show = "#", relief = GROOVE, width = 35,
                                font = police2)
    passeSaisie.pack(pady = 5)
    passeLabel=tkinter.Label(fenetrePrincipale, text = "Votre mot de passe",
                             font = police2)
    passeLabel.pack(before = passeSaisie)
    

    #on place un bouton executer et un bouton retour
    boutonExecuter = tkinter.Button(fenetrePrincipale.tableau, text = "Connexion",
                                    font = police2, command = verifier)
    boutonExecuter.pack(side = LEFT, padx = 75, pady = 25)
    boutonRetour = tkinter.Button(fenetrePrincipale.tableau, text = "Accueil",
                                  font = police2, command = accueil)
    boutonRetour.pack(side = LEFT, padx = 75, pady = 25)

    


def action():
    """page pour choisir l'action a mener sur le compte d'utilisateur"""

    #on efface le tableau
    fenetrePrincipale.effacer()
    fenetrePrincipale.ecrire()
            
    #on affiche un message qui demande a l'utilisateur
    #l'action qu'il veut mener
    effectuerAction = tkinter.Label(fenetrePrincipale.tableau, font = police1,
                        text = "Que voulez-vous faire?")
    effectuerAction.pack(pady = 20)

    #on creer trois boutons d'actions et le bouton accueil
    boutonNouveau = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                   text = "Nouveau", command = nouveauCompte)
    nouveauLabel=tkinter.Label(fenetrePrincipale, text = "1. Ajouter un nouveau \
compte", font = police2)  
    boutonAfficher = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                   text = "Afficher", command = afficherCompte)
    afficherLabel=tkinter.Label(fenetrePrincipale, text = "2. Afficher les \
informations d'un compte", font = police2)
    boutonSupprimer = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                   text = "Supprimer", command = supprimerCompte)
    supprimerLabel=tkinter.Label(fenetrePrincipale, text = "3. Supprimer un \
compte", font = police2)
    boutonNouveau.pack(pady = 10)
    nouveauLabel.pack(before = boutonNouveau)
    boutonAfficher.pack(pady = 10)
    afficherLabel.pack(before = boutonAfficher)
    boutonSupprimer.pack(pady = 10)
    supprimerLabel.pack(before = boutonSupprimer)
    boutonAccueil = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                    text = "Accueil", command = accueil)
    boutonAccueil.pack(pady = 15)




def nouveauCompte():
    """page pour ajouter un nouveau compte"""


    def ajouterCompte():
        """ajout d'un nouveau compte"""

        global utilisateur

        #on recupere les parametre du nouveau compte
        siteweb = sitewebVar.get()
        pseudo = pseudoVar.get()
        passe = passeVar.get()
        email = emailVar.get()

        #et on l'enregistre
        utilisateur.nouveau(siteweb, pseudo, passe, email)

        #on efface letableau
        fenetrePrincipale.effacer()
        fenetrePrincipale.ecrire()
        
        #on affiche un message de succes
        messageSucces = tkinter.Label(fenetrePrincipale.tableau, font = police2,
                            text = "Votre compte a bien ete ajoute",
                                      foreground = "green")
        messageSucces.pack(pady = 90)            
        
        #on cree le bouton accueil bouton accueil
        boutonOk = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                            text = "Ok", command = action)
        boutonOk.pack(pady = 50)


    #on efface le tableau
    fenetrePrincipale.effacer()
    fenetrePrincipale.ecrire()
    
    #on demande a l'utilisateur d'entrer les parametres du nouveau compte
    infosNouveau = tkinter.Label(fenetrePrincipale.tableau, text = "Informations \
sue le compte a ajouter", font = police3)
    infosNouveau.pack(pady = 30)
    #siteweb
    sitewebVar = tkinter.StringVar()
    sitewebSaisie = tkinter.Entry(fenetrePrincipale.tableau,
                                    text = sitewebVar, relief = GROOVE, 
                                  width = 35, font = police2)
    sitewebSaisie.pack(pady = 5)
    sitewebLabel=tkinter.Label(fenetrePrincipale, text = "Entrez le siteweb \
d'inscription", font = police2)
    sitewebLabel.pack(before = sitewebSaisie)

    #pseudo
    pseudoVar = tkinter.StringVar()
    pseudoSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = pseudoVar,
                                 relief = GROOVE, width = 35, font = police2)
    pseudoSaisie.pack(pady = 5)
    pseudoLabel=tkinter.Label(fenetrePrincipale, text = "Entrez votre pseudo",
                              font = police2)
    pseudoLabel.pack(before = pseudoSaisie)
    
    #le mot de passe
    passeVar = tkinter.StringVar()
    passeSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = passeVar,
                                relief = GROOVE, width = 35, font = police2)
    passeSaisie.pack(pady = 5)
    passeLabel=tkinter.Label(fenetrePrincipale, text = "Entrez votre mot \
de passe", font = police2)
    passeLabel.pack(before = passeSaisie)

    #email
    emailVar = tkinter.StringVar()
    emailSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = emailVar,
                                 relief = GROOVE, width = 35, font = police2)
    emailSaisie.pack(pady = 5)
    emailLabel=tkinter.Label(fenetrePrincipale, text = "Entrez votre email",
                           font = police2)
    emailLabel.pack(before = emailSaisie)

    #on place un bouton ajouter et un bouton retour
    boutonAjouter = tkinter.Button(fenetrePrincipale.tableau, text = "Ajouter",
                                  command = ajouterCompte, font = police2)
    boutonAjouter.pack(side = LEFT, padx = 75, pady = 25)
    #on cree un bouton retour
    boutonRetour = tkinter.Button(fenetrePrincipale.tableau, text = "Accueil",
                                  font = police2,command = action)
    boutonRetour.pack(side = RIGHT, padx = 75, pady = 25)




def afficherCompte():
    """page pour afficher un compte"""


    def affichage():
        """affichage des informations sur  le compte"""

        global utilisateur

        #on recupere le nom du siteweb
        siteweb = sitewebVar.get()
        infosUtilisateur, existe = utilisateur.afficher(siteweb)

        #on verifie son existence dans les informations de l'utilisateur
        if existe:
            
            #on efface le tableau
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            
            #on affiche un message de succes
            messageSucces = tkinter.Label(fenetrePrincipale.tableau, font = police1,
                                text = "Vos informations de compte sur {}"\
                                .format(siteweb))
            messageSucces.pack(pady = 20)
            infosSucces = tkinter.Label(fenetrePrincipale.tableau,
                                text = infosUtilisateur, font = police2)
            infosSucces.pack(pady = 10)
            
            #on cree le bouton ok
            boutonOk = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                text = "Ok", command = action)
            boutonOk.pack(pady = 50)

        else:
            #on efface le tableau
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            
            #on affiche un message d'erreur
            messageErreur = tkinter.Label(fenetrePrincipale.tableau, font = police1,
                                text = "Le siteweb {} \
\nne se trouve pas dans votre base".format(siteweb), foreground = "red")
            messageErreur.pack(pady = 90)
            
            #on cree le bouton retour
            boutonRetour = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                text = "Retour", command = action)
            boutonRetour.pack(pady = 50)


    #on efface le tableau
    fenetrePrincipale.effacer()
    fenetrePrincipale.ecrire()
    
    #on demande a l'utilisateur d'entrer le nom du siteweb
    sitewebVar = tkinter.StringVar()
    sitewebSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = sitewebVar,
                                  font = police2)
    sitewebSaisie.pack(pady = 100)
    sitewebLabel=tkinter.Label(fenetrePrincipale, text = "Entrez le siteweb",
                               font = police2)
    sitewebLabel.pack(before = sitewebSaisie, pady = 20)
    
    #on place un bouton afficher et un bouton retour
    boutonAfficher = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                     text = "Afficher", command = affichage)
    boutonAfficher.pack(side = LEFT, padx = 60, pady = 10)
    boutonRetour = tkinter.Button(fenetrePrincipale.tableau, text = "Retour",
                                  font = police2, command = action)
    boutonRetour.pack(side = RIGHT, padx = 60, pady = 10)


    

def supprimerCompte():
    """page pour supprimer un compte"""


    def suppression():
        """suppresion d'un compte"""

        global utilisateur
        #on recupere le nom du siteweb
        siteweb = sitewebVar.get()
        supprime = utilisateur.supprimer(siteweb)

        #on verifie si le compte a ete supprimee
        if supprime:
            
            #on efface le tableau
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            
            #on affiche un message de succes
            messageSucces = tkinter.Label(fenetrePrincipale.tableau, font = police1,
                                text = "Votre compte sur {} a bien ete supprime"\
                                .format(siteweb), foreground = "green")
            messageSucces.pack(pady = 90)
            
            #on cree le bouton ok
            boutonOk = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                text = "Ok", command = action)
            boutonOk.pack(pady = 50)
            
        else:
            #on efface le tableau
            fenetrePrincipale.effacer()
            fenetrePrincipale.ecrire()
            
            #on affiche un message d'erreur
            messageErreur = tkinter.Label(fenetrePrincipale.tableau, font = police1,
                                text = "Le siteweb {} ne se trouve pas \
dans votre base".format(siteweb), foreground = "red")
            messageErreur.pack(pady = 90)
            
            #on cree le bouton retour
            boutonRetour = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                text = "Retour", command = action)
            boutonRetour.pack(pady = 50)


    #on efface le tableau
    fenetrePrincipale.effacer()
    fenetrePrincipale.ecrire()
    
    #on demande a l'utilisateur d'entrer le nom du siteweb
    sitewebVar = tkinter.StringVar()
    sitewebSaisie = tkinter.Entry(fenetrePrincipale.tableau, text = sitewebVar,
                                  font = police2)
    sitewebSaisie.pack(pady = 100)
    sitewebLabel=tkinter.Label(fenetrePrincipale, text = "Entrez le siteweb",
                               font = police2)
    sitewebLabel.pack(before = sitewebSaisie, pady = 20)
    
    #on place un bouton afficher et un bouton retour
    boutonSupprimer = tkinter.Button(fenetrePrincipale.tableau, font = police2,
                                     text = "Supprimer", command = suppression)
    boutonSupprimer.pack(side = LEFT, padx = 60, pady = 10)
    boutonRetour = tkinter.Button(fenetrePrincipale.tableau, text = "Retour",
                                  font = police2, command = action)
    boutonRetour.pack(side = RIGHT, padx = 60, pady = 10)




def fermerProgramme():
    """fermeture du programme"""

    global utilisateur

    try:
        if (utilisateur):
            enregistrerModifications(utilisateur)
    except NameError:
        pass

    fenetreBase.destroy()




fenetreBase = tkinter.Tk()
fenetreBase.wm_maxsize(530, 450)
fenetreBase.wm_minsize(530, 450)
fenetreBase.title("SauvePasse")
fenetreBase.iconbitmap("icone.ico")
fenetreBase.protocol("WM_DELETE_WINDOW", fermerProgramme)
police = "TrebuchetMS 16"
police3 = "TrebuchetMS 13"
police1 = "Verdana 14"
police2 = "Cambria 14"
fenetrePrincipale = Fenetre(fenetreBase)
fenetrePrincipale.ecrire()
messageAccueil = tkinter.Label(fenetrePrincipale.tableau, text = "Bienvenu !\
\nCe petit logiciel vous permet de\n sauvegarder vos informations de compte \n\
sur les siteweb en toute securité\n et de les recuperer plus tard.\n J'espere qu'il vous sera bien \
utile.\n Pour commencer, cliquez sur Ok", font = police)
messageAccueil.pack(pady = 20)
boutonOk = tkinter.Button(fenetrePrincipale.tableau, text = "Ok", height = 1,
                width = 4, font = police1, command = accueil)
boutonOk.pack()
fenetreBase.mainloop()
