import math

class ShowBinary:
  def __init__(self):
    pass

  def out(self, num):
    stateArray = self.__convertBinaryString(bin(num))

    self.__draw(stateArray)

  def clear(self):
    print("                                                        ", end='\r')

  def __convertBinaryString(self, string: str):
    chars = list(string)
    chars.reverse()

    state = []

    for char in chars:
      if char == "b":
        break

      state.append(True if char == "1" else False)

    state.reverse()
    return state

  def __draw(self, stateArray):
    messageArray = []

    for i in range(len(stateArray)):
      messageArray.append("1" if stateArray[i] is True else "0")

    arrLen = len(messageArray)

    for i in range(4 * math.ceil(float(arrLen) / 4) - arrLen):
      messageArray.insert(0, "0")

    messageArray.reverse()

    i = 4
    while i < len(messageArray):
      messageArray.insert(i, ' ')
      i += 5

    messageArray.reverse()
    message = "binary: " + ''.join(messageArray)

    print(message, end='\r')

  def showPixel(self, pixelArray):
    pass

  def showCorrect(self):
    pass

  def showWrong(self):
    pass

  def showLifeUp(self):
    pass

  def showLevelUp(self):
    pass

  def showQuestion(self):
    pass

  def showScore(self, score):
    print("Player scored", score, "points!")