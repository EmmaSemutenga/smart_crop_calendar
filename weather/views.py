# from django.shortcuts import render

# from gpiozero import LED
# from time import sleep
# from sense_emu import SenseHat
# from .models import Temperature
# from datetime import datetime
# from apscheduler.schedulers.background import BackgroundScheduler

# led = LED(25)

# sense = SenseHat()

# red = (255, 0, 0)
# blue = (0, 0, 255)

# def add_temp():
#     temp = sense.temp
#     if temp > 30:
#         Temperature.objects.create(reading=temp)
#     print(temp)

# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(add_temp, 'interval', seconds=30)
#     scheduler.start()