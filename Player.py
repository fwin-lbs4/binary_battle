class Player:
  def __init__(self, name: str, lifes: int = 3):
    self.__name = name
    self.__lifes = lifes
    self.__score = 0
    self.__streak = 0

  def getName(self):
    return self.__name

  def getLifes(self):
    return self.__lifes

  def getScore(self):
    return self.__score

  def incrementScore(self):
    self.__score += 1

  def addLife(self):
    self.__lifes += 1

  def removeLife(self):
    self.__lifes -= 1

  def getStreak(self):
    return self.__streak
  
  def incrementStreak(self):
    self.__streak += 1
  
  def resetStreak(self):
    self.__streak = 0

  def lifeString(self):
    lifes = self.__lifes
    return str(lifes) + " " + ("life" if lifes == 1 else "lifes")

  def scoreString(self):
    points = self.__score
    return str(points) + " " + ("point" if points == 1 else "points")

  def guess(self):
    try:
      return int(input("What is your guess, " + self.__name + "? "))
    except ValueError:
      print("Please enter an Integer!")
      return self.guess()