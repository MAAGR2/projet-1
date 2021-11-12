import httpx
import random

URL = 'http://www.ulaval.ca/api/'
URL2 = 'http://www.ulaval.ca/hapi/partie'
URL3 = 'http://www.ulaval.ca/api/jouer'






def lister_parties(iduls):

    rep = httpx.get(f'{URL}parties/', params={'iduls': iduls})
    

    if rep.status_code == 200:
    # la rÃ©ponse est bonne, afficher son contenu
        liste_parties = []
        parties = rep.json()
        parties = parties['parties']
        print(parties)

        for partie in range (20):
            if parties[partie]['joueurs'][0] == iduls[0] or parties[partie]['joueurs'][1] == iduls[0] :
                if parties[partie]['joueurs'][0] == iduls[1] or parties[partie]['joueurs'][1] == iduls[1] :
                    liste_parties.append(parties[partie])
        return(liste_parties)

        #return parties
    else:
    # afficher un message d'erreur
        print(f"Le GET sur '{URL}parties/' a produit le code d'erreur {rep.status_code}.")
