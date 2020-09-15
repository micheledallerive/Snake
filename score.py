import pickle

loaded=False
score=0

def loadScore():
    global loaded
    global score
    if not loaded:
        try:
            with open("Score.dat", "rb") as file:
                score = pickle.load(file)
        except:
            score=0
        loaded=True
    return score

def saveScore(score):
    with open("Score.dat", "wb") as file:
        pickle.dump(score, file)
