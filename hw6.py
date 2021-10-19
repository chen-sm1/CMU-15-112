#################################################
# hw6.py
#
# Your name:
# Your andrew id:
#
# Your partner's name:
# Your partner's andrew id:
#################################################

import cs112_f21_week6_linter
import math, copy, random

from cmu_112_graphics import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def isPerfectSquare(n):
    sqrt = math.sqrt(n)
    if sqrt == int(sqrt):
        return True
    else:
        return False

def isSortOfSquarish(n):
    if n < 0 or isPerfectSquare(n):
        return False
    digit = []
    flag = 0                        #判断是否已经到了有效位
    for x in range(10,-1,-1):
        if not n//(10**x)%10 == 0:
            digit.append(n//(10**x)%10)
            flag = 1
        elif n//(10**x)%10 == 0 and flag == 1:          #若 n 中含有 0，则 False
            return False
    digit.sort()
    nSorted = 0
    for x in range(len(digit)):
        nSorted += digit[x]*10**(len(digit)-1-x)
    if isPerfectSquare(nSorted):
        return True
    else:
        return False





def nthSortOfSquarish(n):
    count = -1
    for x in range(10000):
        if isSortOfSquarish(x):
            count += 1
        if count == n:
            return x
            
#################################################
# s21-midterm1-animation
#################################################

def s21MidtermAnimation_appStarted(app):
    app.label = 'S21 Midterm Animation!'
    app.i = 0
    app.y = 0
    app.color = 'purple'
    app.timerDelay = 10

def s21MidtermAnimation_keyPressed(app, event):
    app.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])

def s21MidtermAnimation_timerFired(app):
    app.y += 20
    if app.y >= app.height/2:
        app.y = 0
        app.i = (app.i + 1) % len(app.label)
        if app.label[app.i].isspace(): app.i += 1

def s21MidtermAnimation_redrawAll(app, canvas):
    for j in range(app.i+1):
        x = app.width/len(app.label) * (j + 0.5)
        y = app.height/2 if (j < app.i) else app.y
        canvas.create_text(x, y, fill=app.color,
                           text=app.label[j], font=f'Arial 30 bold')

def s21Midterm1Animation():
    runApp(width=400, height=400, fnPrefix='s21MidtermAnimation_')

#################################################
# Tetris
#################################################

def appStarted(app):
    app.label = 'Tetris!'
    app.color = 'orange'
    app.size = 0

def keyPressed(app, event):
    app.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])

def timerFired(app):
    app.size += 10

def redrawAll(app, canvas):
    for s in ((app.size % 300), ((app.size + 150) % 300)):
        canvas.create_text(app.width/2, app.height/2, fill=app.color,
                           text=app.label, font=f'Arial {s} bold')

def playTetris():
    runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare(n))...', end='')
    assert(isPerfectSquare(4) == True)
    assert(isPerfectSquare(9) == True)
    assert(isPerfectSquare(10) == False)
    assert(isPerfectSquare(225) == True)
    assert(isPerfectSquare(1225) == True)
    assert(isPerfectSquare(1226) == False)
    print('Passed')


def testIsSortOfSquarish():
    print('Testing isSortOfSquarish(n))...', end='')
    assert(isSortOfSquarish(52) == True)
    assert(isSortOfSquarish(16) == False)
    assert(isSortOfSquarish(502) == False)
    assert(isSortOfSquarish(414) == True)
    assert(isSortOfSquarish(5221) == True)
    assert(isSortOfSquarish(6221) == False)
    assert(isSortOfSquarish(-52) == False)
    print('Passed')


def testNthSortOfSquarish():
    print('Testing nthSortOfSquarish()...', end='')
    assert(nthSortOfSquarish(0) == 52)
    assert(nthSortOfSquarish(1) == 61)
    assert(nthSortOfSquarish(2) == 63)
    assert(nthSortOfSquarish(3) == 94)
    assert(nthSortOfSquarish(4) == 252)
    assert(nthSortOfSquarish(8) == 522)
    print('Passed')

def testAll():
    testIsPerfectSquare()
    testIsSortOfSquarish()
    testNthSortOfSquarish()

#################################################
# main
#################################################

def main():
    cs112_f21_week6_linter.lint()
    s21Midterm1Animation()
    playTetris()
    testAll()

if __name__ == '__main__':
    main()
