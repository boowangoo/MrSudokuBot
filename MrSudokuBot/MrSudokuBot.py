import praw
import time
import numpy as np
import SudokuSolver as ss
import Grid as g
import os

r = praw.Reddit('MrSudokuBot')
match = ["u/mrsudokubot"]
cachedComments = []
grid = np.zeros((9,9), dtype=np.int).tolist()

def isDigit(d):
    if d >= '0' and d <= '9':
        return True
    return False

def runBot():
    if not os.path.isfile("cachedComments.txt"):
        cachedComments = []
    else:
        with open("cachedComments.txt", "r") as f:
            cachedComments = f.read()
            cachedComments = cachedComments.split("\n")
            cachedComments = list(filter(None, cachedComments))
    print("grabbing subreddit")
    subreddit = r.subreddit("test")
    print("grabbing comments")
    comments = subreddit.comments(limit = 5)
    for cmt in comments:
        cmtTxt = cmt.body.lower()
        isMatch = any(string in cmtTxt for string in match)
        if cmt.id not in cachedComments and isMatch:
            print("match fount! cmt id : ", cmt.id)
            digitList = list(filter(isDigit, list(cmtTxt)))
            if len(digitList) == 81:
                ctr = 0
                for y in range(9):
                    for x in range(9):
                        grid[y][x] = int(digitList[ctr])
                        ctr = ctr + 1
            mainGrid = g.Grid(grid)
            output = "Your Input:\n\n" + str(mainGrid)
            if ss.solve(mainGrid, 0, 0):
                output = output + "\n\nSolved:\n\n" + str(mainGrid)
            else:
                output = output + "\n\nSolved:\n\n" + str(mainGrid) + "    The puzzle could not be solved :("
            print(output)
            cmt.reply(output)
            time.sleep(550)

while True:
    runBot()
    time.sleep(10)
