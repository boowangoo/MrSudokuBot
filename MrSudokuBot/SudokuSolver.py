import numpy as np
import Grid as g

def solve(sGrid, ny, nx):
    # print("solve(sGrid, " + str(ny) + ", " + str(nx) + ")")
    sGridSet = g.GridSet(sGrid)
    # print(sGridSet.gridH[ny][nx])
    # print(sGridSet.gridH)
    while sGridSet.gridH[ny][nx][1] == True:
        if nx+1 == 9:
            ny += 1
            nx = 0
        else:
            nx += 1

    # if ny == 9 and ny == 0:
    #     return True
    for i in range(1,10):
        sGridSet.gridH[ny][nx][0] = i
        sGridSet.gridH
        # print(sGridSet.gridH)
        result = sGridSet.checkGrid(ny, nx)
        # print("result: " + str(result))
        if result == True:
            if ny == 8 and nx == 8:
                return True
            elif nx+1 == 9:
                if solve(sGrid, ny+1, 0):
                    return True
            else:
                if solve(sGrid, ny, nx+1):
                    return True
    sGrid[ny][nx][0] = 0
    return False
