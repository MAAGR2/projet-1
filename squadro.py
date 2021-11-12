import argparse
import httpx


URL = 'http://www.ulaval.ca/api/parties'

def analyser_la_ligne_de_commande():
    '''Analyseur de commande.'''
    parser = argparse.ArgumentParser(description = 'Squadro - Phase 1')

    parser.add_argument("IDUL", nargs='+', help = "IDUL du ou des joueur(s)")

    parser.add_argument("-p", '--parties', action='store_true',
                        help = "Lister les 20 derniÃ¨res parties")
    '''
    -a 
    parser.add_argument("a", action='store_true',
                        help = "Jouer en mode automatique avec le serveur.")
     -x
     parser.add_argument("-x", action='store_true',
                        help = "Jouer en mode manuel contre le serveur avec un affichage graphique.")
    -ax
    parser.add_argument("-ax", action='store_true',
                        help="Jouer en mode automatique contre le serveur avec un affichage graphique.")
    '''
    return parser.parse_args()

def afficher_damier_ascii(etat_j1, etat_j2):
    
    droite = 'â”€â–¡â–¡ â—‹'
    gauche = 'â—‹ â–¡â–¡â”€'
    verticale = 'â”€â”€â–ˆâ”€â”€'
    verticale2 = 'â–ˆ'
    verticale3 = '|'
    verticale4 = 'â—'
    verticale6 = 'â”€â”€â”¼â”€â”€'

    depart_1 = 'â”€â–¡â–¡ â—‹â”€â”¼â”€â”€'
    depart_2 = 'â”€â”€â”€â”€â”€â”€â”¼â”€â”€'
    depart_3 = 'â”€â—‹ â–¡â–¡â”€â”¼â”€â”€'
    depart_4 = 'â”€â–¡â–¡ â—‹â”€â–ˆâ”€â”€'
    depart_5 = 'â”€â”€â”€â”€â”€â”€â–ˆâ”€â”€'
    depart_6 = 'â”€â—‹ â–¡â–¡â”€â–ˆâ”€â”€'
    depart_7 = 'â”€â”€â”€â”€â—‹ â–¡â–¡â”€'

    retournement_1 = 'â”€â”€â”€â”¼â”€â—‹ â–¡â–¡â”€'
    retournement_2 = 'â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€'
    retournement_3 = 'â”€â”€â”€â–ˆâ”€â—‹ â–¡â–¡â”€'
    retournement_4 = 'â”€â”€â”€â–ˆâ”€â”€â”€â”€â”€â”€'

    depart = ['d1','d2','d3','d4','d5']
    for i in range(5):
        if etat_j1[i] == 0:
            if etat_j2[0] == i+1 or etat_j2[0] == 12-i:
                depart[i] = depart_4
            else: depart[i] = depart_1
        elif  etat_j1[i] == 12:
            if etat_j2[0] == i+1 or etat_j2[0] == 12-i:
                depart[i] = depart_6
            else: depart[i] = depart_3    
        elif  etat_j1[i] == 11:
            depart[i] = depart_7
        else:
            if etat_j2[0] == i+1 or etat_j2[0] == 12-i:
                depart[i] = depart_5
            else: depart[i] = depart_2

    retournement = ['r1','r2','r3','r4','r5']
    for i in range(5):
        if etat_j1[i] == 6:
            if etat_j2[4] == i+1 or etat_j2[4] == 11-i:
                retournement[i] = retournement_3
            else : retournement[i] = retournement_1
        else:
            if etat_j2[4] == i+1 or etat_j2[4] == 11-i:
                retournement[i] = retournement_4
            else : retournement[i] = retournement_2

    ligne_1 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_2 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_3 = ['c1' ,'c2','c3']
    ligne_4 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_5 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_6 = ['c1' ,'c2','c3']
    ligne_7 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_8 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_9 = ['c1' ,'c2','c3']
    ligne_10 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_11 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_12 = ['c1' ,'c2','c3']
    ligne_13 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_14 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_15 = ['c1' ,'c2','c3']
    ligne_16 = ['c1' ,'c2','c3','c4' ,'c5']
    ligne_17 = ['c1' ,'c2','c3','c4' ,'c5']

    for i in range(5): 

        if etat_j2[i] == 0:
            ligne_1[i] = verticale2
        elif etat_j2[i] == 12:
            ligne_1[i] = verticale4
        else:
            ligne_1[i] = verticale3
    
    for i in range(5): 

        if etat_j2[i] == 12:
            ligne_2[i] = verticale2
        elif etat_j2[i] == 0 or etat_j2[i] == 11:
            ligne_2[i] = verticale4
        else:
            ligne_2[i] = verticale3

    for i in range(3): 

        if etat_j1[0]==i+2:
            ligne_3[i]=droite
        elif etat_j1[0]==10-i:
            ligne_3[i]=gauche
        elif etat_j2[i+1]==1 or etat_j2[i+1]==11:
            ligne_3[i]=verticale
        else:
            ligne_3[i]=verticale6

    for i in range(5): 

        if etat_j2[i]==1:
            ligne_4[i]=verticale4
        else:
            ligne_4[i]=verticale3 

    for i in range(5): 

        if etat_j2[i]==10:
            ligne_5[i]=verticale4
        else:
            ligne_5[i]=verticale3   
        
    for i in range(3): 

        if etat_j1[1]==i+2:
            ligne_6[i]=droite
        elif etat_j1[1]==10-i:
            ligne_6[i]=gauche
        elif etat_j2[i+1]==2 or etat_j2[i+1]==10:
            ligne_6[i]=verticale
        else:
            ligne_6[i]=verticale6

    for i in range(5): 

        if etat_j2[i]==2:
            ligne_7[i]=verticale4
        else:
            ligne_7[i]=verticale3

    for i in range(5): 

        if etat_j2[i]==9:
            ligne_8[i]=verticale4
        else:
            ligne_8[i]=verticale3

    for i in range(3): 

        if etat_j1[2]==i+2:
            ligne_9[i]=droite
        elif etat_j1[2]==10-i:
            ligne_9[i]=gauche
        elif etat_j2[i+1]==3 or etat_j2[i+1]==9:
            ligne_9[i]=verticale
        else:
            ligne_9[i]=verticale6

    for i in range(5): 

        if etat_j2[i]==3:
            ligne_10[i]=verticale4
        else:
            ligne_10[i]=verticale3

    for i in range(5): 

        if etat_j2[i]==8:
            ligne_11[i]=verticale4
        else:
            ligne_11[i]=verticale3

    for i in range(3): 

        if etat_j1[3]==i+2:
            ligne_12[i]=droite
        elif etat_j1[3]==10-i:
            ligne_12[i]=gauche
        elif etat_j2[i+1]==4 or etat_j2[i+1]==8:
            ligne_12[i]=verticale
        else:
            ligne_12[i]=verticale6

    for i in range(5): 

        if etat_j2[i]==4:
            ligne_13[i]=verticale4
        else:
            ligne_13[i]=verticale3

    for i in range(5): 

        if etat_j2[i]==7:
            ligne_14[i]=verticale4
        else:
            ligne_14[i]=verticale3

    for i in range(3): 

        if etat_j1[4]==i+2:
            ligne_15[i]=droite
        elif etat_j1[4]==10-i:
            ligne_15[i]=gauche
        elif etat_j2[i+1]==5 or etat_j2[i+1]==7:
            ligne_15[i]=verticale
        else:
            ligne_15[i]=verticale6

    for i in range(5): 

        if etat_j2[i]==5 or etat_j2[i]==6:
            ligne_16[i]=verticale4
        else:
            ligne_16[i]=verticale3

    for i in range(5): 

        if etat_j2[i]==6:
            ligne_17[i]=verticale2
        else:
            ligne_17[i]=verticale3

    print('       . | . : | : : | : : | : . | .     ')
    print('         '+ligne_1[0]+'   . '+ligne_1[1]+' .   '+ligne_1[2]+'   . '+ligne_1[3]+' .   '+ligne_1[4]+'       ')
    print('  ...    '+ligne_2[0]+'     '+ligne_2[1]+'     '+ligne_2[2]+'     '+ligne_2[3]+'     '+ligne_2[4]+'      .')
    print('1 â”€'+depart[0]+'â”€'+ligne_3[0]+'â”€'+ligne_3[1]+'â”€'+ligne_3[2]+retournement[0]+'â”€')
    print('  ...    '+ligne_4[0]+'     '+ligne_4[1]+'     '+ligne_4[2]+'     '+ligne_4[3]+'     '+ligne_4[4]+'      .')
    print('  .      '+ligne_5[0]+'     '+ligne_5[1]+'     '+ligne_5[2]+'     '+ligne_5[3]+'     '+ligne_5[4]+'    ...')
    print('2 â”€'+depart[1]+'â”€'+ligne_6[0]+'â”€'+ligne_6[1]+'â”€'+ligne_6[2]+retournement[1]+'â”€')
    print('  .      '+ligne_7[0]+'     '+ligne_7[1]+'     '+ligne_7[2]+'     '+ligne_7[3]+'     '+ligne_7[4]+'    ...')
    print('  ..     '+ligne_8[0]+'     '+ligne_8[1]+'     '+ligne_8[2]+'     '+ligne_8[3]+'     '+ligne_8[4]+'     ..')
    print('3 â”€'+depart[2]+'â”€'+ligne_9[0]+'â”€'+ligne_9[1]+'â”€'+ligne_9[2]+retournement[2]+'â”€')
    print('  ..     '+ligne_10[0]+'     '+ligne_10[1]+'     '+ligne_10[2]+'     '+ligne_10[3]+'     '+ligne_10[4]+'     ..')
    print('  .      '+ligne_11[0]+'     '+ligne_11[1]+'     '+ligne_11[2]+'     '+ligne_11[3]+'     '+ligne_11[4]+'    ...')
    print('4 â”€'+depart[3]+'â”€'+ligne_12[0]+'â”€'+ligne_12[1]+'â”€'+ligne_12[2]+retournement[3]+'â”€')
    print('  .      '+ligne_13[0]+'     '+ligne_13[1]+'     '+ligne_13[2]+'     '+ligne_13[3]+'     '+ligne_13[4]+'    ...')
    print('  ...    '+ligne_14[0]+'     '+ligne_14[1]+'     '+ligne_14[2]+'     '+ligne_14[3]+'     '+ligne_14[4]+'      .')
    print('5 â”€'+depart[4]+'â”€'+ligne_15[0]+'â”€'+ligne_15[1]+'â”€'+ligne_15[2]+retournement[4]+'â”€')
    print('  ...    '+ligne_16[0]+'     '+ligne_16[1]+'     '+ligne_16[2]+'     '+ligne_16[3]+'     '+ligne_16[4]+'      .')
    print('       . '+ligne_17[0]+' .   '+ligne_17[1]+'     '+ligne_17[2]+'     '+ligne_17[3]+'   . '+ligne_17[4]+' .')
    print('       : | : . | . : | : . | . : | :')
    
    def afficher_parties():
        rep = httpx.get(URL)
        parties = rep.json()
        
        for partie in range (20):
            print(str(partie + 1) + ' : '+ parties['parties'][partie]['date'] +', '+ parties['parties'][partie]['joueurs'][0] +' vs '+ parties['parties'][partie]['joueurs'][1])