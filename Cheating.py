from m5stack import *
from m5ui import *
from uiflow import *
import time
import imu
import unit

setScreenColor(0x222222)
rgb_1 = unit.get(unit.RGB, unit.PORTB)


Stage = None
End = None
PlayerX = None
Condition_OnTheGround = None
TIMELIMIT = None
CheatingScore = None
event = None
PlayerY = None
PlayerOfHeight = None
Get1 = None
Get2 = None
Get3 = None
Transfar = None
QuicklyX = None
PlayerOfSize = None
MovingDirection = None
QuicklyY = None
honeyX = None
time = None

imu0 = imu.IMU()

circle0 = M5Circle(160, 120, 15, 0xFFFFFF, 0xFFFFFF)
circle1 = M5Circle(101, 120, 15, 0xFFFFFF, 0xFFFFFF)
circle2 = M5Circle(300, 120, 15, 0xFFFFFF, 0xFFFFFF)
circle3 = M5Circle(300, 120, 15, 0xFFFFFF, 0xFFFFFF)
circle4 = M5Circle(300, 120, 15, 0xFFFFFF, 0xFFFFFF)

from numbers import Number
import math


# この関数の説明…
def TransfarStage():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  if Condition_OnTheGround == 1 and Transfar == 0 and 280 < int((PlayerX * 1)):
    if Stage == 2 and Get1 == 0:
      Get1 = 1
      CheatingScore = (CheatingScore if isinstance(CheatingScore, Number) else 0) + 1
      speaker.tone(550, 105)
      speaker.tone(600, 105)
      speaker.tone(650, 105)
    elif Stage == 3 and Get2 == 0:
      Get2 = 1
      CheatingScore = (CheatingScore if isinstance(CheatingScore, Number) else 0) + 1
      speaker.tone(625, 105)
      speaker.tone(675, 105)
      speaker.tone(725, 105)
    elif Stage == 4 and Get3 == 0:
      Get3 = 1
      CheatingScore = (CheatingScore if isinstance(CheatingScore, Number) else 0) + 1
      MovingDirection = 1
      speaker.tone(700, 105)
      speaker.tone(750, 105)
      speaker.tone(800, 105)
  if Condition_OnTheGround == 1 and 300 < int((PlayerX * 1)) and 0 < math.ceil(QuicklyX):
    Transfar = 1
    if Stage == 1:
      timerSch.run('Stage2', 0, 0x01)
    elif Stage == 2:
      timerSch.run('Stage3', 0, 0x01)
    elif Stage == 3:
      timerSch.run('Stage4', 0, 0x01)
  if Condition_OnTheGround == 1 and 20 > int((PlayerX * 1)) and 0 > math.ceil(QuicklyX):
    Transfar = 1
    if Stage == 1:
      timerSch.run('GOAL', 0, 0x01)
      wait(10000)
    elif Stage == 2:
      timerSch.run('Stage1', 0, 0x01)
    elif Stage == 3:
      timerSch.run('Stage2', 0, 0x01)
    elif Stage == 4:
      timerSch.run('Stage3', 0, 0x01)

# この関数の説明…
def StageCondition():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  if Condition_OnTheGround == 1 and Stage == 2 and MovingDirection == 1 and (60 < PlayerX and PlayerX < 260 and PlayerY < 30 or 60 < PlayerX and PlayerX < 260 and 50 < PlayerY):
    PlayerX = 290
    QuicklyX = 0
    PlayerY = 40
    QuicklyY = 0
  elif Condition_OnTheGround == 1 and Stage == 2 and MovingDirection == 0 and (60 < PlayerX and PlayerX < 260 and PlayerY < 30 or 60 < PlayerX and PlayerX < 260 and 50 < PlayerY):
    PlayerX = 30
    QuicklyX = 0
    PlayerY = 40
    QuicklyY = 0
  elif Condition_OnTheGround == 1 and Stage == 3 and MovingDirection == 1 and 90 < PlayerX and PlayerX < 230:
    PlayerX = 290
    QuicklyX = 0
    PlayerY = 40
    QuicklyY = 0
  elif Condition_OnTheGround == 1 and Stage == 3 and MovingDirection == 0 and 90 < PlayerX and PlayerX < 230:
    PlayerX = 30
    QuicklyX = 0
    PlayerY = 40
    QuicklyY = 0
  elif Condition_OnTheGround == 1 and Stage == 4 and MovingDirection == 1 and (60 < PlayerX and PlayerX < 260 and PlayerY < 30 or 60 < PlayerX and PlayerX < 260 and 50 < PlayerY or 90 < PlayerX and PlayerX < 230):
    PlayerX = 290
    QuicklyX = 0
    PlayerY = 40
    QuicklyY = 0
  elif Condition_OnTheGround == 1 and Stage == 4 and MovingDirection == 0 and (60 < PlayerX and PlayerX < 260 and PlayerY < 30 or 60 < PlayerX and PlayerX < 260 and 50 < PlayerY or 90 < PlayerX and PlayerX < 230):
    PlayerX = 30
    QuicklyX = 0
    PlayerY = 40
    QuicklyY = 0

# この関数の説明…
def Ending():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  timerSch.stop('TIMELIMIT')
  lcd.print('TIME', 0, 0, 0x000000)
  lcd.print((TIMELIMIT + 1), 60, 0, 0xffffff)
  lcd.print(TIMELIMIT, 60, 0, 0x000000)
  speaker.tone(550, 105)
  speaker.tone(600, 105)
  speaker.tone(650, 105)
  speaker.tone(625, 105)
  speaker.tone(675, 105)
  speaker.tone(725, 105)
  speaker.tone(700, 105)
  speaker.tone(750, 105)
  speaker.tone(800, 105)
  circle0.setPosition(30, 180)
  for count10 in range(10):
    lcd.fill(0x000000)
  wait(1)
  lcd.font(lcd.FONT_DejaVu40)

# この関数の説明…
def Moving():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  circle2.hide()
  circle3.hide()
  circle4.hide()
  if Stage == 1:
    lcd.print('<< GOAL', 10, 120, 0x000000)
    lcd.print('STAGE1>>', 200, 120, 0x000000)
    lcd.print('TIME', 0, 0, 0x000000)
    lcd.print((TIMELIMIT + 1), 60, 0, 0xffffff)
    lcd.print(TIMELIMIT, 60, 0, 0x000000)
  elif Stage == 2:
    if TIMELIMIT <= 20 and Get2 == 1:
      lcd.print('HURRY!', 0, 20, 0xffffff)
    lcd.rect(60, 0, 200, 90, fillcolor=0x000000)
    lcd.rect(60, 150, 200, 90, fillcolor=0x000000)
    lcd.rect(60, 0, 200, 90, color=0x000000)
    lcd.rect(60, 150, 200, 90, color=0x000000)
    lcd.print('TIME', 0, 0, 0x000000)
    lcd.print((TIMELIMIT + 1), 60, 0, 0x000000)
    lcd.print(TIMELIMIT, 60, 0, 0xffffff)
    if Get1 == 0:
      circle2.show()
      circle2.setPosition(y=(PlayerY * 3))
  elif Stage == 3:
    if Get3 == 1:
      lcd.print('<=GO GOAL!', 100, 20, 0x000000)
    lcd.rect(90, 0, 140, 240, fillcolor=0x000000)
    lcd.rect(90, 0, 140, 240, color=0x000000)
    lcd.print('TIME', 0, 0, 0x000000)
    lcd.print((TIMELIMIT + 1), 60, 0, 0xffffff)
    lcd.print(TIMELIMIT, 60, 0, 0x000000)
    if Get2 == 0:
      circle3.show()
      circle3.setPosition(y=(PlayerY * 3))
    if TIMELIMIT <= 20 and Get2 == 1:
      lcd.print('HURRY!', 0, 20, 0x000000)
  elif Stage == 4:
    if TIMELIMIT <= 20 and Get2 == 1:
      lcd.print('HURRY!', 0, 20, 0xffffff)
    lcd.rect(60, 0, 200, 90, fillcolor=0x000000)
    lcd.rect(60, 150, 200, 90, fillcolor=0x000000)
    lcd.rect(60, 0, 200, 90, color=0x000000)
    lcd.rect(60, 150, 200, 90, color=0x000000)
    lcd.rect(100, 90, 120, 60, fillcolor=0x000000)
    lcd.rect(100, 90, 120, 60, color=0x000000)
    lcd.print('TIME', 0, 0, 0x000000)
    lcd.print((TIMELIMIT + 1), 60, 0, 0x000000)
    lcd.print(TIMELIMIT, 60, 0, 0xffffff)
    if Get3 == 0:
      circle4.show()
      circle4.setPosition(y=(PlayerY * 3))
    if Get3 == 1:
      lcd.print('<=GO GOAL!', 100, 20, 0xffffff)
  QuicklyX = (QuicklyX if isinstance(QuicklyX, Number) else 0) + (imu0.ypr[2]) / 5
  QuicklyY = (QuicklyY if isinstance(QuicklyY, Number) else 0) + (imu0.ypr[1]) / 20
  if QuicklyX > 10:
    QuicklyX = 10
  if QuicklyX < -10:
    QuicklyX = -10
  if QuicklyY > 5:
    QuicklyY = 5
  if QuicklyY < -5:
    QuicklyY = -5
  PlayerX = int((PlayerX + QuicklyX))
  PlayerY = int((PlayerY + QuicklyY))
  if 320 < PlayerX:
    PlayerX = 80
  if 0 > PlayerX:
    PlayerX = 0
  if 80 < PlayerY:
    PlayerY = 80
  if 0 > PlayerY:
    PlayerY = 0
  StageCondition()
  circle0.setPosition((PlayerX * 1), (PlayerY * 3))
  wait_ms(30)


def buttonC_wasPressed():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  if event < 4:
    if event < 2:
      event = (event if isinstance(event, Number) else 0) + 1
    if event > 3:
      event = (event if isinstance(event, Number) else 0) + -1
    if event == 1:
      lcd.print('Push right button', 0, 0, 0xffffff)
      lcd.print('Good bye', 40, 80, 0xffffff)
      circle0.setPosition(160, 120)
      circle1.setPosition(100, 120)
      lcd.print('See you my honey', 60, 80, 0x000000)
    if event == 2:
      lcd.print('See you my honey', 60, 80, 0xffffff)
      honeyX = 0
      while -150 <= honeyX:
        honeyX = (honeyX if isinstance(honeyX, Number) else 0) + -10
        wait_ms(100)
        circle0.setPosition(160, 120)
        circle1.setPosition((100 + honeyX), 120)
      circle1.hide()
      event = (event if isinstance(event, Number) else 0) + 1
    if event == 3:
      circle0.setPosition(160, 120)
      circle0.setSize(50)
      circle0.setBgColor(0x339999)
      circle0.setBorderColor(0x00cccc)
      lcd.print('HEHEHE', 120, 50, 0x000000)
      lcd.print('I\'ll enjoy "HURIN"', 80, 190, 0x000000)
      wait(3)
      lcd.fill(0x000000)
      lcd.print('Get to the goal within time    limit and catch girls by going     right, but make attention that a round-trip is include. And note you can go to goal ANYTIME.    You can jump if you push center button.', 20, 50, 0xffffff)
      TIMELIMIT = 10
      for count in range(10):
        lcd.print('TIME', 0, 0, 0xffffff)
        lcd.print((TIMELIMIT + 1), 60, 0, 0x000000)
        lcd.print(TIMELIMIT, 60, 0, 0xffffff)
        wait(1)
        TIMELIMIT = (TIMELIMIT if isinstance(TIMELIMIT, Number) else 0) + -1
      lcd.fill(0xffffff)
      TIMELIMIT = 60
      circle0.setSize(15)
      circle0.setBgColor(0x33ccff)
      circle0.setBorderColor(0x99ffff)
      circle0.setPosition(160, 120)
      event = (event if isinstance(event, Number) else 0) + 1
      timerSch.run('Stage1', 0, 0x01)
      timerSch.run('START', 0, 0x01)
  pass
btnC.wasPressed(buttonC_wasPressed)

@timerSch.event('Stage4')
def tStage4():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  Stage = 4
  for count2 in range(10):
    lcd.rect(90, 0, 140, 240, fillcolor=0xffffff)
    lcd.rect(90, 0, 140, 240, color=0xffffff)
  if 160 < PlayerX:
    PlayerX = 30
    MovingDirection = 0
  else:
    PlayerX = 290
    MovingDirection = 1
  Transfar = 0
  pass

@timerSch.event('OVERDUE')
def tOVERDUE():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  timerSch.stop('OVERDUE')
  lcd.print('TIME', 0, 0, 0x000000)
  lcd.print((TIMELIMIT + 1), 60, 0, 0xffffff)
  lcd.print(TIMELIMIT, 60, 0, 0x000000)
  speaker.setVolume(1)
  for count3 in range(10):
    speaker.tone(700, 105)
    speaker.tone(900, 105)
  lcd.fill(0x000000)
  wait(1)
  lcd.font(lcd.FONT_DejaVu40)
  lcd.print('GAME OVER', 35, 90, 0xff0000)
  circle1.show()
  circle1.setPosition(30, 180)
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print('I mock you motherfucker.', 40, 142, 0xffffff)
  pass

@timerSch.event('Stage2')
def tStage2():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  Stage = 2
  for count4 in range(10):
    lcd.rect(90, 0, 140, 240, fillcolor=0xffffff)
    lcd.rect(90, 0, 140, 240, color=0xffffff)
    lcd.print('<< GOAL', 10, 120, 0xffffff)
    lcd.print('STAGE1>>', 200, 120, 0xffffff)
  if 160 < PlayerX:
    PlayerX = 30
    MovingDirection = 0
  else:
    PlayerX = 290
    MovingDirection = 1
  Transfar = 0
  pass

@timerSch.event('Stage3')
def tStage3():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  Stage = 3
  for count5 in range(10):
    lcd.rect(60, 0, 200, 90, fillcolor=0xffffff)
    lcd.rect(60, 150, 200, 90, fillcolor=0xffffff)
    lcd.rect(60, 0, 200, 90, color=0xffffff)
    lcd.rect(60, 150, 200, 90, color=0xffffff)
  if 160 < PlayerX:
    PlayerX = 30
    MovingDirection = 0
  else:
    PlayerX = 290
    MovingDirection = 1
  Transfar = 0
  pass

@timerSch.event('Stage1')
def tStage1():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  Stage = 1
  for count6 in range(10):
    lcd.rect(60, 0, 200, 90, fillcolor=0xffffff)
    lcd.rect(60, 150, 200, 90, fillcolor=0xffffff)
    lcd.rect(60, 0, 200, 90, color=0xffffff)
    lcd.rect(60, 150, 200, 90, color=0xffffff)
  if 160 < PlayerX:
    PlayerX = 30
    MovingDirection = 0
  else:
    PlayerX = 290
    MovingDirection = 1
  Transfar = 0
  pass

@timerSch.event('TIMELIMIT')
def tTIMELIMIT():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  if event == 4:
    TIMELIMIT = (TIMELIMIT if isinstance(TIMELIMIT, Number) else 0) + -1
    if TIMELIMIT <= 0:
      event = 5
      timerSch.run('OVERDUE', 100, 0x01)
  pass

def buttonB_wasPressed():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  if End == 0 and event == 4:
    Condition_OnTheGround = 0
    PlayerOfHeight = 7
    PlayerOfSize = 15
    for count7 in range(14):
      PlayerOfSize = (PlayerOfSize if isinstance(PlayerOfSize, Number) else 0) + PlayerOfHeight
      PlayerOfHeight = (PlayerOfHeight if isinstance(PlayerOfHeight, Number) else 0) + -1
      circle0.setSize(int((PlayerOfSize / 2)))
      Moving()
    circle0.setSize(15)
    Condition_OnTheGround = 1
  pass
btnB.wasPressed(buttonB_wasPressed)

@timerSch.event('GOAL')
def tGOAL():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  End = 1
  circle0.hide()
  if 0 == CheatingScore and 55 <= TIMELIMIT:
    Ending()
    lcd.print('TRUE END', 35, 90, 0xffffff)
    circle1.show()
    circle1.setPosition(30, 180)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('I defintely love you!', 40, 142, 0xffffff)
    rgb_1.setColor(1, 0xffffff)
    rgb_1.setColor(2, 0xffffff)
    rgb_1.setColor(3, 0xffffff)
  elif 0 == CheatingScore and 55 > TIMELIMIT or 1 == CheatingScore:
    Ending()
    lcd.print('LESS END', 35, 90, 0x66ffff)
    circle0.show()
    circle0.setPosition(30, 180)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('I wanna enjoy more...', 40, 142, 0xffffff)
    rgb_1.setColor(1, 0x33ffff)
    rgb_1.setColor(2, 0x33ffff)
    rgb_1.setColor(3, 0x33ffff)
  elif 2 == CheatingScore:
    Ending()
    lcd.print('NORMAL END', 35, 90, 0x33ff33)
    circle0.show()
    circle0.setPosition(30, 180)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print("I enjoyed! It's not pointless!", 40, 142, 0xffffff)
    rgb_1.setColor(1, 0x33ff33)
    rgb_1.setColor(2, 0x33ff33)
    rgb_1.setColor(3, 0x33ff33)
  elif 3 == CheatingScore:
    Ending()
    lcd.print('COMPLETED', 35, 90, 0xffff66)
    circle0.show()
    circle0.setPosition(30, 180)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('PERFECT! ARE YOU A GOD?', 40, 142, 0xffffff)
    rgb_1.setColor(1, 0xffff00)
    rgb_1.setColor(2, 0xffff00)
    rgb_1.setColor(3, 0xffff00)
    for count8 in range(100):
      rgb_1.setBrightness(int((math.sin(time / 180.0 * math.pi) * 100)))
  pass

@timerSch.event('START')
def tSTART():
  global Stage, End, TIMELIMIT, Condition_OnTheGround, PlayerX, CheatingScore, event, PlayerOfHeight, PlayerY, Get1, Get2, Get3, Transfar, QuicklyX, PlayerOfSize, MovingDirection, QuicklyY, honeyX, time
  for count9 in range(2):
    PlayerX = 160
    PlayerY = 40
    QuicklyX = 0
    QuicklyY = 0
  pass


lcd.clear()
CheatingScore = 0
Get1 = 0
Get2 = 0
Get3 = 0
PlayerX = 160
PlayerY = 120
QuicklyX = 0
QuicklyY = 0
event = 0
Condition_OnTheGround = 1
End = 0
time = 0
Transfar = 0
MovingDirection = 0
lcd.fill(0xffffff)
lcd.font(lcd.FONT_DejaVu18)
timerSch.run('TIMELIMIT', 1000, 0x00)
setScreenColor(0xffffff)
circle0.setSize(15)
circle1.setSize(15)
circle2.setSize(15)
circle3.setSize(15)
circle4.setSize(15)
circle0.show()
circle1.show()
circle0.setPosition(160, 120)
circle0.setBgColor(0x33ccff)
circle0.setBorderColor(0x99ffff)
circle1.setPosition(100, 120)
circle1.setBgColor(0xff0000)
circle1.setBorderColor(0xff6666)
circle2.setBgColor(0xcc66cc)
circle2.setBorderColor(0xff99ff)
circle3.setBgColor(0x33ff33)
circle3.setBorderColor(0x66ff99)
circle4.setBgColor(0xffff00)
circle4.setBorderColor(0xffff99)
TIMELIMIT = 0
circle2.hide()
circle3.hide()
circle4.hide()
lcd.print('Good bye', 40, 80, 0x000000)
lcd.print('Push right button', 0, 0, 0x000000)
while True:
  if End == 0 and Condition_OnTheGround == 1 and event == 4:
    Moving()
    TransfarStage()
  time = (time if isinstance(time, Number) else 0) + 1
  wait_ms(2)
