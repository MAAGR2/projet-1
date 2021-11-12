import httpx
import random

URL='http://www.ulaval.ca/api/'
URL2='http://www.ulaval.ca/hapi/partie'
URL3='http://www.ulaval.ca/api/jouer'

def lister_parties(iduls):
    
    rep = httpx.get(f'{URL}parties/', params={'iduls': iduls})
    if rep.status_code==200:
    # la rÃ©ponse est bonne, afficher son contenu
        liste_parties=[]
        parties=rep.json()
        parties=parties['parties']
        print(parties)
        for partie in range (20):
            if parties[partie]['joueurs'][0]==iduls[0] or parties[partie]['joueurs'][1]==iduls[0] :
                if parties[partie]['joueurs'][0]==iduls[1] or parties[partie]['joueurs'][1]==iduls[1] :
                    liste_parties.append(parties[partie])
        return(liste_parties)
        #return parties
    else:
    # afficher un message d'erreur
        print(f"Le GET sur '{URL}parties/' a produit le code d'erreur {rep.status_code}.")


def récupérer_partie(id_partie):
    
    reponse = httpx.get(URL2)

    if reponse.status_code == 200:
    # la rÃ©ponse est bonne, afficher son contenu
        rep = reponse.text
        print(rep)
        try:
            for p in rep['partie']:
                if id_partie == p['id']:
                    prochain_joueur = p['prochain_joueur']
                    état = p['état']
                    gagnant = p['gagnant']
        except IOError as exc:
            raise RuntimeError('Impossible de rÃ©cupÃ©rer la partie') from exc

        
        partie = (id_partie, prochain_joueur, état, gagnant)

        return partie
        

    else:
    # afficher un message d'erreur
        print(f"Le GET sur '{URL2}' a produit le code d'erreur {reponse.status_code}.")


def débuter_partie(iduls, bot=None):

    #liste = lister_parties(iduls)

    #print(liste)

    id = "" + str(iduls.iduls(4)) + ""

    #partie = rÃ©cupÃ©rer_partie(id)

    if bot == None:
        rep = httpx.post(URL2, data={'iduls': iduls})
    else:
        rep = httpx.post(URL2, data={'iduls': iduls, 'bot': bot})
    
    if rep.status_code == 200:
    # la rÃ©ponse est bonne, afficher son contenu
        
        prochain_joueur = iduls[0]


        état = [{"nom": ""+iduls[0]+"","pions": [0, 0, 0, 0, 0]},{"nom": ""+iduls[1]+"","pions": [0, 0, 0, 0, 0]},]

        gagnant = None
                
        partie = (id, prochain_joueur, état, gagnant)

        

        return partie
        
        
    else:
    # afficher un message d'erreur
        print(f"Le GET sur '{URL2}' a produit le code d'erreur {rep.status_code}.")


def jouer_coup(id_partie, idul, pion):

    partie = récupérer_partie(id_partie)
    print(partie)
    
