import RPi.GPIO as GPIO
from flask import Flask, render_template,request
from picamera import Picamera
from io import BytesIO


led_pin_1 = 7
led_pin_2 = 11
led_pin_3 = 13 
led_pin_4 = 15
led_pin_5 = 29
led_pin_6 = 31

GPIO.setmode(GPIO.BOARD)

GPIO.setup(led_pin_1,GPIO.OUT)
GPIO.setup(led_pin_2,GPIO.OUT)
GPIO.setup(led_pin_3,GPIO.OUT)
GPIO.setup(led_pin_4,GPIO.OUT)
GPIO.setup(led_pin_5,GPIO.OUT)
GPIO.setup(led_pin_6,GPIO.OUT)

GPIO.output(led_pin_1,GPIO.HIGH)
GPIO.output(led_pin_2,GPIO.HIGH)
GPIO.output(led_pin_3,GPIO.HIGH)
GPIO.output(led_pin_4,GPIO.HIGH)
GPIO.output(led_pin_5,GPIO.HIGH)
GPIO.output(led_pin_6,GPIO.HIGH)

