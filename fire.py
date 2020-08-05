from playsound import playsound
import time
import asyncio


loop = asyncio.get_event_loop()


def play():
    playsound('bell.mp3')


def write(text):
    with open('countdown.txt', 'w') as filetowrite:
        filetowrite.write(text)


def countdown(t):
    while t != -1:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        write(timeformat)
        time.sleep(1)
        t -= 1


minutes = input("How many minutes? ")

print("Starting Zazen for %s minute(s) with 15 seconds for preparation\n" % minutes)

countdown(15)
loop.run_in_executor(None, play)
countdown(60*minutes)
loop.run_in_executor(None, play)
