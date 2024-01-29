import time
import random
import pickle
import os.path
from Player import Player
from Score import Score
from ShowBinaryMatrix import ShowBinary

class Game:
  def __init__(self, name: str = "Player", levelMax: int = 5):
    self.__player = Player(name)
    self.__level = 1
    self.__levelMax = levelMax
    self.__previousNumber = -1
    self.__display = ShowBinary()

  def start(self):
    self.__display.showCorrect()

    time.sleep(1)
    while self.__player.getLifes() > 0:
      num = self.__previousNumber

      while num == self.__previousNumber:
        num = random.randint((2 ** (self.__level)), (2 ** (2 + self.__level)) - 1)

      self.__previousNumber = num

      print("Look at the matrix!")

      self.__display.out(num)

      time.sleep(1 + (self.__level / 2))

      self.__display.clear()
      self.__display.showQuestion()

      guess = self.__player.guess()

      if guess is num:
        self.__player.incrementScore()
        self.__player.incrementStreak()
        self.__display.showCorrect()
        print("Correct! You have " + self.__player.scoreString() + "!")

      if guess is not num:
        self.__player.removeLife()
        self.__player.resetStreak()
        self.__display.showWrong()
        print("False! You have " + self.__player.lifeString() + " left!")

      if self.__player.getStreak() == 5:
        self.__player.addLife()
        self.__display.showLifeUp()
        print("Player gained a life")

        if (self.__level != self.__levelMax):
          time.sleep(0.25)
          print("Levelup")
          self.__display.showLevelUp()
          self.__level += 1

        self.__player.resetStreak()

      print("The player has", self.__player.lifeString(), "and", self.__player.scoreString())
      print("The game is level", str(self.__level))

      time.sleep(0.5)

    print("Game ended!")
    self.__display.showScore(self.__player.getScore())

    scores = self.__getScores()

    scores.append(Score(self.__player.getName(), self.__player.getScore()))

    scores.sort(key=lambda score: score.points, reverse=True)

    for score in scores:
      print(score.name, score.points)

    self.__saveScores(scores)

  def __createFile(self):
    if os.path.isfile("./high_scores.pkl"):
      return

    f = open("./high_scores.pkl", "a")
    f.close()

    self.__saveScores([])

  def __getScores(self):
    self.__createFile()
    with open('./high_scores.pkl', 'rb') as inp:
      return pickle.load(inp)

  def __saveScores(self, scores):
    self.__createFile()
    with open('./high_scores.pkl', 'wb') as outp:
      pickle.dump(scores, outp, pickle.HIGHEST_PROTOCOL)