
import msignif #module du regex
import re # import du regex
import fifa_data # import du module fifa_data pour utiliser les fonction d'affichage
import joueur 


decision = [] #on initialise une liste vide avant d'appeler la fonction 
decision_joueur=[] # on utilise cette liste pour retenir les joueurs que l'utilisateur à choisi pour pouvoir les retourner dans choix(text) 

def rgx_search(rgx, string):
    for obj in rgx:
        if re.search(obj,str(string)) is not None:
            return True
    return None

def chatbot(text):
    if decision == []:#permet d'aller dans les fonctions de bases du bot
        if rgx_search(msignif.startbot,text) is not None: #message d'introduction, qui affiche les 50 joueurs du top 50
            return "Bonjour, je suis un Chatbot qui donne des infos sur les joueurs de football sur la version du jeu FIFA 19 !!\n"+fifa_data.affichage_50_joueurs()+"\nQuel joueur du top50 voulez-vous ? :)"

        elif rgx_search(msignif.stop,text) is not None:# pour mettre fin à la conversation avec le chatbot
            return "Merci d'avoir discuté avec moi !! J'espère vous avoir aidé !! :)"

        elif rgx_search(msignif.joueurs,text) is not None: # permet de choisir le joueur que l'on veut
            decision.append("choix nom")
            decision_joueur.append(text)
            return "Quelle caractéristique souhaitez vous avoir ? :)"

        else:
            return "Veuillez reformuler votre intention s'il vous plaît. " # au cas où le bot ne reconnait aucune situation possible

    else :
        del decision[len(decision)-1] #permet de repasser aux fonctions de base juste apres avoir donnée l'info sur le joueur 
        res = joueur.JoueurChatbot(text)# stocke le resultat du type de renseignement choisi par l'utilisateur
        if res =="taille":
            return decision_joueur[len(decision_joueur)-1] + " mesure " + fifa_data.affichage_taille_joueur(decision_joueur[len(decision_joueur)-1])
        elif res=="poids": 
            return decision_joueur[len(decision_joueur)-1] + " pèse " + fifa_data.affichage_poids_joueur((decision_joueur[len(decision_joueur)-1]))
        elif res=="salaire": 
            return decision_joueur[len(decision_joueur)-1] + " est payé " + fifa_data.affichage_salaire_joueur((decision_joueur[len(decision_joueur)-1])) + "par mois"
        elif res=="pieds": 
            return "le pieds fort de " +decision_joueur[len(decision_joueur)-1]+"est le pieds "+ fifa_data.affichage_pieds_joueur((decision_joueur[len(decision_joueur)-1]))
        elif res =="age":
            return decision_joueur[len(decision_joueur)-1] + " est agé de " + fifa_data.affichage_age_joueur((decision_joueur[len(decision_joueur)-1]))+" ans"
        elif res=="photo": 
            return "la photo de "+decision_joueur[len(decision_joueur)-1]+" est" +fifa_data.affichage_photo_joueur((decision_joueur[len(decision_joueur)-1]))
        elif res=="note": 
            return "la note general sur fifa de "+decision_joueur[len(decision_joueur)-1]+" est " +fifa_data.affichage_note_joueur((decision_joueur[len(decision_joueur)-1]))
        elif res=="club": 
            return "le club de " +decision_joueur[len(decision_joueur)-1]+ " est : " +fifa_data.affichage_club_joueur((decision_joueur[len(decision_joueur)-1]))
            
 

