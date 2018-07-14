import os

# teamA = sys.argv[1]
# teamB = sys.argv[2]
# carte = sys.argv[3]

liste_classe = [
    'eca',
    'eni',
    'iop',
    'cra',
    'feca',
    'sacri',
    'sadi',
    'osa',
    'enu',
    'sram',
    'xel',
    'panda',
    'roub',
    'zobal',
    'elio',
    'steam',
    'ougi',
    'hupper',
]


class Team:
    def __init__(self):
        self.liste_pick = []
        self.liste_win = []
        self.liste_ban = []


    def winrate(self, teamA, teamB, carte):
        """ Méthode permettant de mettre a jour les winrate de chaque classe apres des drafts """

        team1, team2 = teamA[0], teamB[0]
        pickA, banA, winA = teamA[1], teamA[2], teamA[3]   #win = 1 si win 0 sinon
        pickB, banB, winB = teamB[1], teamB[2], teamB[3]
        listApick, listBpick = team1.liste_pick, team2.liste_pick #on recupere la liste des picks joues par la teamA et B avant la mise a jour de la draft
        listewinA = team1.liste_win, listewinB = team2.liste_win ##on recupere la liste des [picks,[nbr win, nbr pick]] pour un pick donné joues par la teamA et B avant la mise a jour de la draft
        #gere les erreurs
        if len(pickA) > 3 or len(banA) > 3:
            return "error draft, trop de pick ou ban pour la team A"
        elif len(pickB) > 3 or len(BanB) > 3:
            return "error draft, trop de pick ou ban pour la team B"
        elif carte != type(int) and carte > 25:
            return "mauvais numero de map"
        elif winA != 0 or winA !=1:
            return "victoire ou defaite de la team A incorrect"
        elif winB != 0 or winB !=1:
            return "victoire ou defaite de la team B incorrect"

        #Update liste des picks pour les team A et B
        for i in range(0, 3):
            if pickA[i] in listApick:
                for j in range(0,len(listewinA)):
                    elt = listewinA[j]
                    if pickA[i] == elt[0]:        #si le pick est deja dans la liste on va aumgenter de 1 son nombre de pick total et de 1* winA son total de win
                        nbr = elt[1]
                        nbr[0] += 1 * winA
                        nbr[1] += 1
                        elt[0], elt[1] = nbr[0], nbr[1]
            else:                               #si le pick n'a jamais ete joue on le rajoute avec 1 match joue et 1 * win win
                listApick.append(pickA[i])
                listwinA.append([pickA[i], [1 * winA, 1]])

        for i in range(0, 3):
            if pickB[i] in listBpick:
                for j in range(0,len(listewinB)):
                    elt2 = listewinB[j]
                    if pickB[i] == elt2[0]:        #si le pick est deja dans la liste on va aumgenter de 1 son nombre de pick total et de 1* winA son total de win
                        nbr2 = elt2[1]
                        nbr2[0] += 1 * winB
                        nbr2[1] += 1
                        elt2[0], elt2[1] = nbr2[0], nbr2[1]
            else:
                listBpick.append(pickB[i])
                listwinB.append([pickB[i], [1 * winB, 1]])



            #On remet bien a jour toutes les listes
        team1.liste_pick = listApick
        team2.liste_pick = listBpick
        team1.liste_win = listewinA
        team2.liste_win = listewinB



["ov",["osa","zobal","sadi"],["panda","xel","feca"],1]
ov = Team()
ov.list_pick = [""]
go = Team()
go.list_pick = [""]
ov.winrate(["ov",["osa","zobal","sadi"],["panda","xel","feca"],1],["go",["elio","cra","enu"],["iop","sram","eca"],0], 18)
print(ov.list_pick, go.list_pick)
