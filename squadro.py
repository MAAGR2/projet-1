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
