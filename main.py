import api
import squadro
import argparse




if __name__ == '__main__':
    COMMANDE = squadro.analyser_la_ligne_de_commande()

    #print(COMMANDE.IDUL[0])
    iduls = COMMANDE.IDUL
    if COMMANDE.parties:
        #print(api.lister_parties(COMMANDE.idul))
        squadro.afficher_parties()
    # Mofe automatique (commande : python main.py -a idul)
    
    # elif COMMANDE.a:
        #DEBUTER = api.dÃ©buter_partie(COMMANDE.idul)
        #JEU = squadro

    else:
        
        DEBUTER = api.dÃ©buter_partie(iduls)
        #print(DEBUTER[2][0]['pions'])
        #print(DEBUTER[2][1]['pions'])
        
        id_partie = DEBUTER[0]
        etat_j1 = DEBUTER[2][0]['pions']
        etat_j2 = DEBUTER[2][1]['pions']
        joueur_1 = DEBUTER[2][0]['nom']
        joueur_2 = DEBUTER[2][1]['nom']
        prochain_joueur = joueur_1
        etat_finale = [12, 12, 12, 12, 12]
