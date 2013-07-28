import os
import pickle

            
class Utilisateur():
    """class pour creer un nouvel utilisateur"""
    
    identifiant = 0
    
    def __init__(self, pseudo, passe, nom, prenom):
        """pseudo-> le pseudo a utiliser pour ce compte
passe -> le mot de passe unique a avoir et a ne pas oublier"""

        Utilisateur.identifiant += 1 #creation d'un numero d'ordre
        self.pseudo = pseudo
        self.passe = passe
        self.nom = nom
        self.prenom = prenom
        #on cree un dico qui va contenir les nom d'utilisateur, mot de passe,email
        self.donnees = {}


    def nouveau(self, *parametres):
        """ajouter de nouveaux comptes pour un utilisateur"""
        
        #on ajoute les nouveaux parametre avec le pseudo comme cle et une
        #liste pour les autres
        self.donnees[parametres[0]] = (parametres[1], parametres[2],
                                       parametres[3])
        enregistrerModifications(self)


    def supprimer(self, siteweb):
        """supprimer un compte de l'utilisateur"""
        
        if siteweb in self.donnees:
            del self.donnees[siteweb]
            return True
        else:
            return False     
        

    def afficher(self, siteweb):
        """afficher les donnees d'un compte specifique"""

        trouve = False
        if siteweb in self.donnees:
            informations = ("Siteweb : {}\n\nPseudo : {}\n\nMot de Passe : {}\
\n\nEmail : {}\n".format(siteweb, self.donnees[siteweb][0],
                       self.donnees[siteweb][1], self.donnees[siteweb][2]))
            trouve = True
        else:
            informations = "Vous n'avez pas enregistre ce siteweb"

        return informations, trouve



def chargerUtilisateurs():
    """chargement du dictionnaire des utilisateur
retourne -> liste des utilisateurs"""

    if os.path.exists('donnees'):
        with open('donnees', 'rb') as fichierUtilisateur:
            monDepickler = pickle.Unpickler(fichierUtilisateur)
            listeUtilisateur = monDepickler.load()
    else:
        listeUtilisateur = list()

    return listeUtilisateur



def enregistrerModifications(utilisateur):
    """enregistrement de l'utilisateur apres modification"""

    existe = False
    listeUtilisateur = chargerUtilisateurs()#chargement de la liste des utilisateurs
    #pour chaque utilisateur
    for cetUtilisateur in listeUtilisateur:
        #si l'utilisateur se trouve dans liste
        if cetUtilisateur.pseudo == utilisateur.pseudo:
            ancien = cetUtilisateur #on l'affecte a un temporaire
            existe = True
            break
        else:
            pass
        
    if existe: #si l'utilisateur existe
        index = listeUtilisateur.index(ancien) #on recupere sa position
        listeUtilisateur[index] = utilisateur  #et on l'ecrase
    else:   #s'il n'existe pas
        listeUtilisateur.append(utilisateur)    #on l'ajoute  
 
    with open('donnees', 'wb') as fichierUtilisateur:
        monPickler = pickle.Pickler(fichierUtilisateur)
        monPickler.dump(listeUtilisateur)



def connexionUtilisateur(pseudo, passe):
    """pour connecter un utilisateur"""

    listeUtilisateur = chargerUtilisateurs()
    for cetUtilisateur in listeUtilisateur:
        if ((cetUtilisateur.pseudo) == pseudo and
            (cetUtilisateur.passe == passe)):
            return cetUtilisateur

    return False



def creerUtilisateur(pseudo, passe, nom, prenom):
    """creation d'un nouvel utilisateur"""

    listeUtilisateur = chargerUtilisateurs()
    for cetUtilisateur in listeUtilisateur:
        if cetUtilisateur.pseudo == pseudo or len(pseudo) == 0:
            return False

    nouvelUtilisateur = Utilisateur(pseudo, passe, nom, prenom)
    enregistrerModifications(nouvelUtilisateur)
    return(nouvelUtilisateur)

            

    


    
