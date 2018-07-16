import os
import matplotlib.pyplot as plt
import numpy as np
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

# draft = ["osa","zobal","sadi"],["panda","xel","feca"],1], [["elio","cra","enu"],["iop","sram","eca"],0]



class Team:
    def __init__(self):
        self.liste_pick = []
        self.liste_win = []
        self.liste_ban = []


    def winrate(self, teamA):                               #teamA = [["osa","zobal","sadi"],["panda","xel","feca"],1]
        """ Méthode permettant de mettre a jour les winrate de chaque classe apres des drafts """

        pickA, banA, winA = teamA[0], teamA[1], teamA[2]   #win = 1 si win 0 sinon
        listApick = self.liste_pick                        #on recupere la liste des picks joues par la teamA  avant la mise a jour de la draft
        listewinA = self.liste_win                         ##on recupere la liste des [picks,[nbr win, nbr pick]] pour un pick donné joues par la teamA et B avant la mise a jour de la draft

        #gere les erreurs
        if len(pickA) != 3 or len(banA) != 4:
            return "error draft, trop de pick ou ban pour la team A"
        elif winA not in [0,1]:
            return "victoire ou defaite de la team A incorrect"


        #Update liste des picks pour les team A et B
        for i in range(0, 3):
            if pickA[i] in listApick:
                for j in range(0,len(listewinA)):
                    elt = listewinA[j]
                    if pickA[i] == elt[0]:        #si le pick est deja dans la liste on va aumgenter de 1 son nombre de pick total et de 1* winA son total de win
                        nbr = elt[1]
                        nbr[0] += 1 * winA
                        nbr[1] += 1
                        elt[1] = nbr
            else:                               #si le pick n'a jamais ete joue on le rajoute avec 1 match joue et 1 * win win
                listApick.append(pickA[i])
                listewinA.append([pickA[i], [1 * winA, 1]])

            #On remet bien a jour toutes les listes
            #win de la forme [...[classe, [nbr win, nbr pick]]....]
        self.liste_pick = listApick
        self.liste_win = listewinA
        # print("attribut de la classe : {} {} \n".format(self.liste_pick, self.liste_win))
        # print("liste que je modifie : {} {}\n".format(listApick, listewinA))
        return 0


    def display_win(self, t):
        """ Méthode permettant d'afficher le pourcentage de win de chaque classe pour une team """

        l = self.liste_win
        N = len(l)
        classe = []
        taux_win = []
        ind = np.arange(N)
        for elt in l:
            nbr1 = elt[1]
            nbr0 = elt[0]
            taux_win.append((float(nbr1[0]) / float(nbr1[1])) * 100)
            classe.append(nbr0)
        p1 = plt.bar(ind, taux_win, width = 0.35, color = 'blue')
        plt.xticks(ind, classe)
        plt.yticks(np.arange(0, 110, 10))
        plt.title("winrate draft de {}".format(t))
        plt.ylabel('pourcentage win')
        # plt.legend(p1[0], ('winrate'))
        plt.savefig("winrate {}".format(t))
    #    plt.show()
        return 0


#On affiche le déroulé complet d'une draft
def display_draft(teamA, teamB, carte):
    pickA, pickB = teamA[1], teamB[1]
    banA, banB = teamA[2], teamB[2]
    t1, t2 = teamA[0], teamB[0]
    draft = ""
    if teamA[3] == 1:
        draft += "Draft : {} vs {} sur map {}-> win {} \n\n".format(t1, t2, carte, t1)
    else:
        draft += "Draft : {} vs {} -> win {} \n\n".format(t1, t2, t2)
    draft += " {} ban {} \n {} ban {} \n".format(t1, banA[0], t2, banB[0]) + " \n {} pick {} \n {} pick {} \n\n".format(t1, pickA[0], t2, pickB[0])
    for i in range(1,3):
        draft += " {} ban {} \n {} ban {} \n".format(t2, banA[i], t1, banB[i])
    draft += " \n {} pick {} \n {} pick {} \n".format(t1, pickA[1], t1, pickB[1]) + "\n {} ban {} \n {} ban {} \n".format(t1, banA[3], t2, banB[3]) + " \n {} pick {} \n {} pick {} \n".format(t1, pickA[0], t2, pickB[0])
    return draft



ov = Team()
go = Team()
bg = Team()
ooc = Team()
millenium = Team()
orks = Team()
exodia = Team()
free_bowisse = Team()


draft_winter = [
        [["bg",["xel","sadi","iop"],["osa","panda","ougi","eca"],1], ["millenium",["eni","feca","steam"],["sacri","zobal","enu","roub"],0], 12],
        [["go",["osa","steam","roub"],["eni","xel","enu","eca"],1], ["bg",["sacri","sadi","panda"],["feca","zobal","iop","ougi"],0], 12],
        [["bg",["sacri","iop","ougi"],["xel","panda","steam","feca"],0], ["free_bowisse",["eni","sadi","eca"],["osa","zobal","enu","roub"],1], 12],
        [["bg",["eni","ougi","steam"],["iop","zobal","sacri","enu"],0], ["orks",["osa","sadi","sram"],["xel","panda","feca","eca"],1], 12],
        [["bg",["sacri","ougi","sadi"],["feca","panda","iop","steam"],1], ["exodia",["eni","hupper","eca"],["xel","osa","enu","zobal"],0], 12],
        [["free_bowisse",["eni","panda","sadi"],["sacri","zobal","eca","enu"],0], ["ooc",["osa","ougi","steam"],["feca","xel","iop","roub"],1], 12],
        [["ov",["sacri","iop","roub"],["osa","eni","sadi","eca"],1], ["go",["xel","cra","enu"],["feca","panda","zobal","steam"],0], 12],
        [["exodia",["eni","enu","sadi"],["sacri","zobal","eca","steam"],1], ["orks",["osa","iop","elio"],["xel","panda","feca","ougi"],0], 12],
        [["millenium",["osa","feca","ougi"],["eni","zobal","eca","iop"],1], ["ov",["sacri","xel","roub"],["steam","enu","panda","sadi"],0], 12],
        [["free_bowisse",["xel","zob","roub"],["sacri","panda","osa","iop"],0], ["exodia",["eni","iop","hupper"],["feca","sadi","steam","eca"],1], 12],
        [["ooc",["eni","ougi","eca"],["osa","zobal","xel","steam"],1], ["millenium",["sacri","iop","elio"],["sadi","panda","feca","enu"],0], 12],
        [["orks",["osa","sadi","ougi"],["xel","panda","sacri","roub"],0], ["ov",["eni","iop","hupper"],["feca","enu","steam","eca"],0], 12],
]

for elt in draft_winter:
    d = elt[0]
    d1 = elt[1]
    t1 = d[0]
    t2 = d1[0]
    print("team : {} {}".format(t1, t2))
    f = open("draft_{}.txt".format(t1), "a")
    g = open("draft_{}.txt".format(t2), "a")
    f.write(display_draft(d, d1, 12) + "\n\n")
    g.write(display_draft(d, d1, 12) + "\n\n")
    f.close()
    g.close()
    del d[0]
    del d1[0]
    if t1 == "bg":
        bg.winrate(d)
    if t1 == "ov":
        ov.winrate(d)
    if t1 == "ooc":
        ooc.winrate(d)
    if t1 == "go":
        go.winrate(d)
    if t1 == "exodia":
        exodia.winrate(d)
    if t1 == "free_bowisse":
        free_bowisse.winrate(d)
    if t1 == "millenium":
        millenium.winrate(d)
    if t1 == "orks":
        orks.winrate(d)
    if t2 == "bg":
        bg.winrate(d1)
    if t2 == "ov":
        ov.winrate(d1)
    if t2 == "ooc":
        ooc.winrate(d1)
    if t2 == "go":
        go.winrate(d1)
    if t2 == "exodia":
        exodia.winrate(d1)
    if t2 == "free_bowisse":
        free_bowisse.winrate(d1)
    if t2 == "millenium":
        millenium.winrate(d1)
    if t2 == "orks":
        orks.winrate(d)
bg.display_win("bg")
ov.display_win("ov")
ooc.display_win("ooc")
exodia.display_win("exodia")
orks.display_win("orks")
millenium.display_win("millenium")
free_bowisse.display_win("free bowisse")
go.display_win("go")

# ov.winrate([["osa","zobal","sadi"],["panda","xel","feca"],1])
# go.winrate([["elio","cra","enu"],["iop","sram","eca"],0])
#
# ov.display_win()
# print(display_draft(["ov",["osa","zobal","sadi"],["panda","xel","feca","steam"],1], ["go",["elio","cra","enu"],["iop","sram","eca","sacri"],0], 12))
