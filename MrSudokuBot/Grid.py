import numpy as np
class Grid:
    def __init__(self, newList):
        # print(newList)
        self.newList = (list(map(lambda n: list(map(lambda m: [m], n)), newList)))
        for i in range(len(self.newList)):
            for j in range(len(self.newList[i])):
                if self.newList[i][j][0] > 0:
                    self.newList[i][j].append(True)
                elif self.newList[i][j][0] == 0:
                    self.newList[i][j].append(False)
        # print(self.newList)
    def __str__(self):
        strFacade = ""
        for i in range(9):
            strFacade += "    "
            for j in range(9):
                if j == 3 or j == 6:
                    strFacade += "|"
                if self.newList[i][j][0] == 0:
                    strFacade += "_ "
                else:
                    strFacade += str(self.newList[i][j][0]) + " "
            # strFacade += "|"
            if (i+1) % 3 == 0 and i != 8:
                strFacade += "\n    ------+------+------\n"
            else:
                strFacade += "\n"
        return strFacade
    def __getitem__(self, key):
        return self.newList[key]

class GridSet:
    gridV = Grid(np.zeros((9,9), dtype=np.int))
    gridS = Grid(np.zeros((9,9), dtype=np.int))
    def __init__(self, gridH):
        self.gridH = gridH
        for i in range(9):
            for j in range(9):
                GridSet.gridV[i][j] = self.gridH[j][i]
                GridSet.gridS[i][j] = self.gridH[3*(i%3) + int(j/3)][j%3 + int(i/3)*3]
    def noMatches(listA):
        listA = list(map(lambda x: x[0], listA))
        listA = list(filter(lambda x: x != 0, listA))
        return not any(listA[i] in (listA[0:i] + listA[i+1:len(listA)]) for i in range(len(listA)))

    def checkH(self, y):
        return GridSet.noMatches(self.gridH[y])
    def checkV(self, x):
        return GridSet.noMatches(GridSet.gridV[x])
    def checkS(self, y, x):
        sectNum = int(y/3) + int(x/3)*3
        return GridSet.noMatches(GridSet.gridS[sectNum])
    def checkGrid(self, y, x):
        return all([GridSet.checkH(self, y), GridSet.checkV(self, x), GridSet.checkS(self, y,x)])
