import random
import httpx

URL = 'http://www.ulaval.ca/api/'
URL2 = 'http://www.ulaval.ca/api/partie'
URL3 = 'http://www.ulaval.ca/api/jouer'


def lister_les_parties(iduls):
    rep = httpx.get(f'{URL}parties/', params={'iduls': iduls})
    if rep.status_code == 200:
        liste_parties = []
        parties = rep.json()
        parties = parties['parties']
        print(parties)
        for partie in range (20):
            if parties[partie]['joueurs'][0] == iduls[0] or parties[partie]['joueurs'][1] == iduls[0]:
                if parties[partie]['joueurs'][0] == iduls[1] or parties[partie]['joueurs'][1] == iduls[1]:
                    liste_parties.append(parties[partie])
        return(liste_parties)
    else:
        print(f"Le GET sur '{URL}parties/' a produit le code d'erreur {rep.status_code}.")


def récupérer_une_partie(id_partie):
    rep = httpx.get(URL2)
    if rep.status_code == 200:
        rep = rep.json()
        prochain_joueur = rep['partie'][0]['prochain_joueur']
        état = rep['partie'][0]['état']
        gagnant = None
        for i in range(20):
            if rep['partie'][i]['id'] == id_partie :
                prochain_joueur = rep['partie'][i]['prochain_joueur']
                état = rep['partie'][i]['état']
                if rep['partie'][i]['gagnant'] != None:
                    gagnant = rep['partie'][i]['gagnant']
        partie = (id_partie, prochain_joueur, état, gagnant)
        return partie
    else:
        print(f"Le GET sur '{URL2}' a produit le code d'erreur {rep.status_code}.")


def créer_une_partie(iduls):
    id = "2021"
    partie = récupérer_une_partie(id)
    rep = httpx.post(URL2, data={'iduls': iduls})
    if rep.status_code == 200:
        rep = rep.json()
        if iduls[0] == rep['partie'][0]['prochain_joueur']:
            prochain_joueur = rep['partie'][1]['prochain_joueur']
        else:
            prochain_joueur = rep['partie'][0]['prochain_joueur']
        état = rep['partie'][0]['état']
        for i in range(20):
            if rep['partie'][i]['id'] == id :
                prochain_joueur = rep['partie'][i]['prochain_joueur']
                état = rep['partie'][i]['état']
                if rep['partie'][i]['gagnant'] != None:
                    gagnant = rep['partie'][i]['gagnant']   
        partie = (id, prochain_joueur, état, gagnant)
        return partie
    else:
        print(f"Le GET sur '{URL2}' a produit le code d'erreur {rep.status_code}.")

def jouer_un_coup(id_partie, idul, pion):
    partie = récupérer_une_partie(id_partie)
    if idul == partie[2][0]['nom']:
            prochain_joueur = partie[2][1]['nom']
            if pion == 1:
                partie[2][0]['pions'][0] += 3
            elif pion == 2:
                partie[2][0]['pions'][1] += 1
            elif pion == 3:
                partie[2][0]['pions'][2] += 2
            elif pion == 4:
                partie[2][0]['pions'][3] += 1
            else:
                partie[2][0]['pions'][4] += 3
    else:
        prochain_joueur = partie[2][0]['nom']
        if pion == 1:
            partie[2][1]['pions'][0] += 1
        elif pion == 2:
            partie[2][1]['pions'][1] += 3
        elif pion == 3:
            partie[2][1]['pions'][2] += 2
        elif pion == 4:
            partie[2][1]['pions'][3] += 3
        else:
            partie[2][1]['pions'][4] += 1
    état = partie[2]
    return (id_partie, prochain_joueur, état)