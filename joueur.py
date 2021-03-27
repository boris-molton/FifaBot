import msignif
import re
import fifa_data

#fonction qui retourne le choix de l'utilisateur concernant le reseignement du joueur, on utilise msignif.py pour utiliser le regex
def JoueurChatbot(decision):
    liste_taille = msignif.taille
    liste_poids = msignif.poids
    liste_salaire = msignif.salaire
    liste_pieds = msignif.pied
    liste_note = msignif.note
    liste_photo = msignif.photo
    liste_age = msignif.age
    liste_club = msignif.club
    for obj in liste_taille: 
        if re.search(decision,obj) is not None: #detecte si le message de l'utilisateur correspond avec le pattern de regex pour la taille
            return "taille"
    for obj in liste_poids:
        if re.search(decision,obj) is not None:#detecte si le message de l'utilisateur correspond avec le pattern de regex pour le poids
            return "poids"
    for obj in liste_salaire:
        if re.search(decision,obj) is not None:#detecte si le message de l'utilisateur correspond avec le pattern de regex pour le salaire
            return "salaire"
    for obj in liste_age:
        if re.search(decision,obj) is not None:#detecte si le message de l'utilisateur correspond avec le pattern de regex pour l'age
            return "age"
    for obj in liste_note:
        if re.search(decision,obj) is not None:#detecte si le message de l'utilisateur correspond avec le pattern de regex pour la note
            return "note"
    for obj in liste_club:
        if re.search(decision,obj) is not None:#detecte si le message de l'utilisateur correspond avec le pattern de regex pour le club
            return "club"
    for obj in liste_photo:
        if re.search(decision,obj) is not None:#detecte si le message de l'utilisateur correspond avec le pattern de regex pour la photo
            return "photo"
    for obj in liste_pieds:
        if re.search(decision,obj) is not None:#detecte si le message de l'utilisateur correspond avec le pattern de regex pour la pieds
            return "pieds"
    
   
