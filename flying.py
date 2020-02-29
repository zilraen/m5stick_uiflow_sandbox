from m5stack import *
from m5ui import *
from uiflow import *
import imu
import hat

bgcolor = 0x111111
sensitivity = 10

screen_height = 180
screen_width = 80

class object:
   x = int(screen_width / 2)
   y = int(screen_height / 2)
   color = 0xffffff
   
   def checkBorders(self):
      if self.x < 0:
         self.x = 0
      if self.y < 0:
         self.y = 0
      if self.x > screen_width:
         self.x = screen_width
      if self.y > screen_height:
         self.y = screen_height
   
   def update(self, dx, dy):
      lcd.pixel(self.x, self.y, bgcolor)
      self.x += dx
      self.y += dy
      self.checkBorders()
      lcd.pixel(self.x, self.y, self.color)

mc = object()


setScreenColor(bgcolor)

#hat_Joystick0 = hat.get(hat.JOYSTICK)
imu0 = imu.IMU()
gyroZeroX = imu0.gyro[1]
gyroZeroY = imu0.gyro[0]

label0 = M5TextBox(60, 15, "Text", lcd.FONT_Default,0xFFFFFF, rotate=180)

while True:
  #mc_dx = int(hat_Joystick0.X / sensitivity)
  #mc_dy = int(-hat_Joystick0.Y / sensitivity)
  mc_dx = int((imu0.gyro[1] - gyroZeroX) / sensitivity)
  mc_dy = int((imu0.gyro[0] - gyroZeroY) / sensitivity)
  label0.setText(str(mc_dx) + ", " + str(mc_dy))
  mc.update(mc_dx, mc_dy)
  wait_ms(2)
