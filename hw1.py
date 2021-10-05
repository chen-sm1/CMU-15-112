#################################################
# hw1.py
# name:
# andrew id:
#################################################

import cs112_f21_week1_linter
import math




#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Part A
#################################################

def distance(x1, y1, x2, y2):
    return pow(pow((x1-x2),2)+pow((y1-y2),2),0.5)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    circlepoint_distance =distance(x1,y1,x2,y2)
    radius_sum = r1+r2
    if circlepoint_distance <= radius_sum:
        return True
    else:
        return False

def getInRange(x, bound1, bound2):
    if bound1>bound2:
        lower_bound = bound2
        higher_bound = bound1
    else:
        lower_bound = bound1
        higher_bound = bound2
    if x <= lower_bound:
        return lower_bound
    elif x >= higher_bound:
        return higher_bound
    else:
        return x

def eggCartons(eggs):
    if eggs%12 == 0:
        return eggs//12
    else:
        return eggs//12+1 


def pascalsTriangleValue(row, col): 
    if row<col or row<0 or col<0:
        return None
    else:
        return math.factorial(row)/(math.factorial(col)*math.factorial(row-col))
    

def getKthDigit(n, k):#不用len,str
    n = abs(n)
    return n//(10**k)%10
    


def setKthDigit(n, k, d):
    neg_flag = 0
    if (n < 0):
        n=abs(n)
        neg_flag=1
    n_alter=n//(10**k)%10
    n=n+(d-n_alter)*10**k
    if neg_flag==1:
        return -n
    else:
        return n


#################################################
# Part B
#################################################
        
def nearestOdd(n):
    n_int = int(n)
    if (n_int%2 == 0):
        if (n_int == n or n_int <=0):
            return n_int-1
        else:
            return n_int+1
    else:
        return n_int
    



def numberOfPoolBalls(rows):
    return (rows+1)*rows/2

def numberOfPoolBallRows(balls):
    row=pow((balls*2+0.25),0.5)-0.5
    if int(row) < row:
        return int(row)+1
    else:
        return int(row)

def colorBlender(rgb1, rgb2, midpoints, n):
    b1=rgb1%1000
    g1=int((rgb1%1e6-b1)/1000)
    r1=int((rgb1-g1*10**3-b1)/1e6)
    b2=rgb2%1000
    g2=int((rgb2%1e6-b2)/1000)
    r2=int((rgb2-g2*10**3-b2)/1e6)
    r_gap=(r1-r2)/(midpoints+1)
    g_gap=(g1-g2)/(midpoints+1)
    b_gap=(b1-b2)/(midpoints+1)

    if n<0 or n>(midpoints+1):
        return None
    gap1=roundHalfUp((r1-n*r_gap))
    gap2=roundHalfUp((g1-n*g_gap))
    gap3=roundHalfUp((b1-n*b_gap))
    result=gap1*1e6+gap2*1e3+gap3
    return int(result)

#################################################
# Bonus/Optional
#################################################

def handToDice(abc):
    a=getKthDigit(abc, 2)
    b=getKthDigit(abc, 1)
    c=getKthDigit(abc, 0)
    return (a,b,c)

def diceToOrderedHand(a,b,c):
    max=a
    middle=c
    if a<b:
        max=b
        min=a
        if max<c:
            max=c
            middle=b
        elif min>c:
            min=c
            middle=a
    else:
        min=b
        if max<c:
            max=c
            middle=a
        elif min>c:
            min=c
            middle=b
    return max*100+middle*10+min
        
def playStep2(a,b):
    a0=getKthDigit(a,0)
    a1=getKthDigit(a,1)
    a2=getKthDigit(a,2)
    b0=getKthDigit(b,0)
    b1=getKthDigit(b,1)
    b2=getKthDigit(b,2)
    b3=getKthDigit(b,3)
    matching_dice=0
    a_max=0
    if a0==a1==a2:
        matching_dice=3
    else:
        if a0==a1 or a1==a2:
            matching_dice=2
    if matching_dice==0:
        a_max=max(a0,a1,a2)
        a=diceToOrderedHand(a_max,b0,b1)
        if b2<b3:
            b=b2*10+b3
        else:
            b=b3*10+b2
    elif matching_dice==2:
        if a0==a1:
            a=diceToOrderedHand(a0,a1,b0)
            b=diceToOrderedHand(b1,b2,b3)
            if b2<b3:
                b=b2*100+b3*10+b1
            if b2>b3:
                b=b3*100+b2*10+b1
            if b%10==0 and b>10:
                b=b//10
                if b%10==0 and b>10:
                    b=b//10
        else:
            a=diceToOrderedHand(a1,a2,b0)
            b=diceToOrderedHand(b1,b2,b3)
            if b2<b3:
                b=b2*100+b3*10+b1
            if b2>b3:
                b=b3*100+b2*10+b1
            if b>10 and b%10==0:
                b=b//10
                if b%10==0 and b>10:
                    b=b//10
    elif matching_dice==3:
        a=a0*100+a1*10+a2
        b=diceToOrderedHand(b0,b1,b3)
    return (int(a),int(b))

def score(n):
    ge = getKthDigit(n,0)
    shi = getKthDigit(n,1)
    bai = getKthDigit(n,2)
    if ge == shi == bai:
        return 20+3*ge
    elif ge == shi:
        return 10+2*ge
    elif bai == shi:
        return 10+2*shi
    else:
        return max(ge,shi,bai)

def bonusPlayThreeDiceYahtzee(dice):
    dice1 = 0
    dice2 = 0
    dice1 += getKthDigit(dice, 2) + getKthDigit(dice, 1)*10 
    dice1 += getKthDigit(dice, 0)*100
    dice2 += getKthDigit(dice, 6)*1e3 + getKthDigit(dice, 5)*1e2 
    dice2 += getKthDigit(dice,3) + getKthDigit(dice, 4)*10 
    hand,dice2 = playStep2(dice1,dice2)
    hand,dice2 = playStep2(hand,dice2)
    return (hand,score(hand))


def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)  
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testGetKthDigit()
    testSetKthDigit()
    # Part B:
    testNearestOdd()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testColorBlender()
    # Bonus:
    testBonusPlayThreeDiceYahtzee()
    # testBonusFindIntRootsOfCubic()

def main():
    cs112_f21_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
