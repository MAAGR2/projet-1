import api
import squadro
import argparse

if __name__ == '__main__':
    COMMANDE = squadro.analyser_la_ligne_de_commande()

    #print(COMMANDE.IDUL[0])
    iduls = COMMANDE.IDUL
    if COMMANDE.parties:
        #print(api.lister_parties(COMMANDE.idul))
        squadro.afficher_le_plateau_de_jeu()
    # Mofe automatique (commande : python main.py -a idul)
    
    # elif COMMANDE.a:
        #DEBUTER = api.débuter_partie(COMMANDE.idul)
        #JEU = squadro
    else:
        
        DEBUTER = api.jouer_un_coup(iduls)
        #print(DEBUTER[2][0]['pions'])
        #print(DEBUTER[2][1]['pions'])
        
        id_partie = DEBUTER[0]
        etat_j1 = DEBUTER[2][0]['pions']
        etat_j2 = DEBUTER[2][1]['pions']
        joueur_1 = DEBUTER[2][0]['nom']
        joueur_2 = DEBUTER[2][1]['nom']
        prochain_joueur = joueur_1
        etat_finale = [12, 12, 12, 12, 12]

        while etat_j1 != etat_finale and etat_j2 != etat_finale:
            squadro.afficher_le_plateau_de_jeu(etat_j1, etat_j2)
            print(prochain_joueur + '! Merci de spécifier votre coup. choisissez parmi 1, 2, 3, 4, 5:')
            pion = int(input())
            
            if pion not in [1, 2, 3, 4, 5]:
                print('valeur invalide')
            else:
                #coup = api.jouer_coup(id_partie,prochain_joueur, pion)
                '''
                etat_j1 = coup[2][0]['pions']
                etat_j2 = coup[2][1]['pions']
                prochain_joueur = joueur_2
'''                #récupérer_partie()
        iduls = ['MAAGR2']
        api.lister_parties(iduls)
    