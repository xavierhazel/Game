from adafruit_circuitplayground import cp
from adafruit_crickit import cricket
from adafruit_moter import stepper

import time


def basic_hello():
    print("hello world anf begin to burn")

def custom_hello(name):
    print("hello " + name)

  def wave_hello():
    count = 0
    while count < 5:
      cricket.servo_1.angle = 0
      time.sleep(0.2)
      cricket.servo_1.angle = 120
      time.sleep(0.4)
      count = count + 1
      print("multifacited functional syntax error")

  while True:
    if cp.button_a:
        basic_hello()
        wave_hello()
        time.sleep(2)

