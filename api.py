import random
import httpx
URL = 'https://pax.ulaval.ca/squadro/api2/'

def lister_les_parties(liste_idul): 
    rep = httpx.get(URL+'parties', params={'iduls': liste_idul})
    if rep.status_code == 200:
       rep = rep.json()
       return rep.get("parties")
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])

def récupérer_une_partie(id_partie):
    liste = [id_partie,]
    rep = httpx.get(URL+'partie', params={'id' : liste})
    if rep.status_code == 200:
        tup = (rep.json()['id'], rep.json()['prochain_joueur'], rep.json()['état'])
        return tup
    elif rep.status_code ==406:
        raise RuntimeError(rep.json()['message'])

def créer_une_partie(liste_iduls):
    rep = httpx.post(URL+'partie', json={'iduls': liste_iduls})
    if rep.status_code == 200:
        rep = rep.json()
        tup = (rep.get('id'), rep.get('prochain_joueur'), rep.get('état'))
        return tup
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])

def jouer_un_coup(id_partie, idul, pion):
    rep = httpx.put(URL+'jouer', json= {'id' : id_partie, 'idul':idul, 'pion' : pion})
    if rep.status_code == 200:
        rep = rep.json()
        if rep['gagnant'] is not None:
           raise StopIteration(rep['gagnant'])
        else:
             tup = (rep['id'], rep['prochain_joueur'], rep['état'])
             return tup
    elif rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
print(créer_une_partie(['maagr2','meagr']))
print(jouer_un_coup(créer_une_partie(['maagr2','meagr'])[0], 'maagr2',3))
print(récupérer_une_partie(jouer_un_coup(créer_une_partie(['maagr2','meagr'])[0], 'maagr2',3)[0]))