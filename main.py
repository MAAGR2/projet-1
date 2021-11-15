import argparse

def traiter_la_ligne_de_commande():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('IDUL',type = str,metavar='IDUL',help = 'IDUL du ou des joueur(s)')
    parser.add_argument('-p','--parties',metavar='',type = list,help = 'Lister les 20 dernières parties')
   

    return parser.parse_args()
traiter_la_ligne_de_commande() 