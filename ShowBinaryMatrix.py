from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import  show_message
from luma.core.legacy.font import proportional, CP437_FONT

class ShowBinary:
  def __init__(self):
    self.__device = max7219(spi(port=0, device=1, gpio=noop()), cascaded=1, block_orientation=90, rotate=0)

  def out(self, num):
    self.clear()
    stateArray = self.__convertBinaryString(bin(num))

    self.__draw(stateArray)

  def clear(self):
    with canvas(self.__device) as draw:
      draw.rectangle([0, 0, 7, 7], fill="black")

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
    stateArray.reverse()
    x = 7
    y = 7

    with canvas(self.__device) as draw:
      for state in stateArray:
        draw.point((x, y), fill="white" if state else "black")

        if x == 0:
          y -= 1
          x = 7
          continue

        x -= 1

  def showPixel(self, pixelArray):
    x = 0
    y = 0

    with canvas(self.__device) as draw:
      x, y = 0, 0
      for row in pixelArray:
        for col in row:
          draw.point((x, y), fill="white" if col else "black")

          x += 1
        y += 1
        x = 0

  def showCorrect(self):
    self.showPixel([
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0]
    ])

  def showWrong(self):
    self.showPixel([
      [1, 0, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0],
      [0, 1, 0, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 0, 0, 1]
    ])

  def showLifeUp(self):
    self.showPixel([
      [0, 1, 1, 0, 0, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0]
    ])

  def showLevelUp(self):
    self.showPixel([
      [1, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 1, 1, 0, 0, 1],
      [1, 1, 0, 1, 1, 0, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1]
    ])

  def showQuestion(self):
    self.showPixel([
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0]
    ])

  def showScore(self, score):
    msg = "Score: " + str(score)
    show_message(self.__device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)