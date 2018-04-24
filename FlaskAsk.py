import logging
import serial
import signal
from flask import Flask, render_template
from flask_ask import Ask, statement, question
from random import *
from datetime import timedelta, datetime
import time

TIMEOUT = 3
app = Flask(__name__)
ask = Ask(app, "/")

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#ser = serial.Serial('/dev/cu.usbmodem1411', 115200)

def passByte(b):
    print("Passing byte " + str(b))
    ser.write(bytes([int(b)]))

def halt():
    passByte(0)

def moveForward():
    passByte(1)

def turnRight():
    passByte(2)

def turnLeft():
    passByte(3)

def moveBackward():
    passByte(4)

@ask.launch
def welcomemsg():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

Team5 = ['teddy', 'Vladimir', 'Jessie']

@ask.intent("FollowIntent")
def follow(firstname):
    if firstname in Team5:
        msg = "Tracking for {}".format(firstname)
    elif firstname == 'follow':
    	return question("Who should I follow?").reprompt("May I please have a name?")
    elif firstname not in Team5:
        msg = "I Can't follow {} he is not a member of Team 5".format(firstname)
        return question(msg).reprompt("May I please have another name?")
    return statement(msg)
"""
@ask.intent("WhoToFollowIntent")
def what_is_my_name():
    return question("Who should I follow?").reprompt("May I please have a name?")
"""
@ask.intent("MoveIntent")
def move(direction):
    if direction == 'left':
        turnLeft()
        msg = "moving left"
    elif direction == 'right':
        turnRight()
        msg = "moving right"
    elif direction == 'forward':
        moveForward()
        msg = "moving forward"
    elif direction == 'backward':
        moveBackward()
        msg = "moving backward"
    elif direction == 'move':
        return question("In what direction?").reprompt("Can you please give a direction?")
    return statement(msg)

@ask.intent("MemoryIntent")
def memorygame(number):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]*10
    y = sample(numbers, 90)    # Generate 90 random numbers
    # round_msg = "Beginning memory game."
    i = 1
    score = 0

    q = y[0:i]
    round_msg = "Please repeat",q
    return statement(round_msg)
    
@ask.intent("AnswerIntent")
answer = []
endtime = datetime.utcnow() + timedelta(seconds = 5)
while True:
    if number == 'one':
        answer + [1]
        endtime = endtime + timedelta(seconds = 2)
    elif number == 'two':
        answer + [2]
        endtime = endtime + timedelta(seconds = 2)          
    elif number == 'three':
        answer + [3]
        endtime = endtime + timedelta(seconds = 2)
    elif number == 'four':
        answer + [4]
        endtime = endtime + timedelta(seconds = 2)
    elif number == 'five':
        answer + [5]
        endtime = endtime + timedelta(seconds = 2)
    elif number == 'six':
        answer + [6]
        endtime = endtime + timedelta(seconds = 2)
    elif number == 'seven':
        answer + [7]
        endtime = endtime + timedelta(seconds = 2)
    elif number == 'eight':
        answer + [8]
        endtime = endtime + timedelta(seconds = 2)
    elif number == 'nine':
        answer + [9]      
        endtime = endtime + timedelta(seconds = 2)
    elif datetime.utcnow() > endtime:
        break
# answer += [int(x) for x in input().split()]
# print(answer)

if answer == q:
    score += 1
    i += 1
else: 
    msg = "Incorrect answer, your final score is",score
    break
if  (q == [90]):
    print("You beat the game, congratulations.")
    break
return statement(msg)

@ask.intent("AMAZON.StopIntent")
def stop():
    halt()
    return statement("Stopping")

if __name__ == '__main__':
    app.run(debug=True)