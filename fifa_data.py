import re #module du regex
import pandas as pd # pour gerer le dataframe de base


dataset_top_50=pd.read_csv(r'C:\Users\boris\Documents\fifabot\data.csv', sep=',')
dataset_top_50.drop(dataset_top_50.index[51:18208],0,inplace=True)

#retourne du nom des 50 joueurs pour le message d'introduction du bot
def affichage_50_joueurs():
    string=""
    for i in range(0,50):
        string+="\n"+str(dataset_top_50.loc[i]['Name'])
    return string

        
#retourne du nom du club du joueur souhaité
def affichage_club_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Club']])
    return string

#retourne du poids du joueur souhaité
def affichage_poids_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Weight']])
    return string

#retourne de la taille du joueur souhaité
def affichage_taille_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Height']])
    return string

#retourne le salaire par mois du joueur souhaité
def affichage_salaire_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Wage']])
    return string

#retourne l'age du joueur souhaité
def affichage_age_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Age']])
    return string

#retourne la photo d'un du joueur souhaité
def affichage_photo_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Photo']])
    return string

#retourne la note generale d'un joueur souhaité
def affichage_overall_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Overall']])
    return string

#retourne le pieds fort d'un joueur souhaité
def affichage_pieds_joueur(nom_joueur):
    string=""
    string+=str(dataset_top_50.loc[dataset_top_50['Name']==nom_joueur,['Preferred Foot']])
    return string

#retourne la note generale d'un joueur souhaité
def liste_nom():
    l=[]
    for i in range(0,50):
        l.append(str(dataset_top_50.loc[i]['Name']))
    return l


liste_nom_joueur=liste_nom()
