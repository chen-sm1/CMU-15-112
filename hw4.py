#################################################
# hw4.py
# name:
# andrew id:
#################################################

import cs112_f21_week4_linter
import math, copy

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

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Part A
#################################################

def alternatingSum(L):
    sum = 0
    square = 0
    for x in L:
        sum += x*(-1)**square
        square += 1
    return sum


def median(L):
    half = len(L)//2
    L = sorted(L)
    if L == []:
        return None
    elif len(L)%2 ==1:
        return L[half]
    else:
        return (L[half]+L[half-1])/2


def smallestDifference(L):
    if L == []:
        return -1
    L = sorted(L)
    result = L[-1]-L[0]
    for x in range(1,len(L)):
        if abs(L[x]-L[x-1]) < result:
            result = abs(L[x]-L[x-1])
    return result

def nondestructiveRemoveRepeats(L):
    result = []
    for x in L:
        if not x in result:
            result.append(x)
    return result

def destructiveRemoveRepeats(L):
    index = 0
    ls = []
    for x in L:
        if x in L[:index]:          #把重复元素的位置放在 ls 中
            ls.append(index)
        index += 1

    num = 0
    for x in ls:
        x = x -num                  #每次把重复元素删除时，索引都会减1
        L.pop(x)
        num += 1

#################################################
# Part B
#################################################

def isSorted(L):
    flag1 = 1
    flag2 = 1
    for x in range(1,len(L)): 
        if L[x]-L[x-1] >= 0:
            flag1 +=1
        if L[x]-L[x-1] <= 0:
            flag2 +=1
    if flag1 == len(L) or flag2 == len(L) or L == []:
        return True
    else:
        return False

def lookAndSay(L):
    result = []
    count = 1
    for x in range(len(L)-1):
        if L[x] == L[x+1]:
            count += 1
            if x == len(L)-2:   #若列表倒数第二个元素与倒数第一个元素相同，要把（count，L[x]）添加进result中
                result.append((count,L[x]))
        else:
            result.append((count,L[x]))
            count = 1
            if x == len(L)-2:  #若列表倒数第二个元素与倒数第一个元素不同，要把（1，L[-1]）添加进result中
                result.append((1,L[-1]))
    return result


def inverseLookAndSay(L):
    result = []
    for x in L:
        for y in range(x[0]):
            result.append(x[-1])
    return result



def multiplyPolynomials(p1, p2):
    result = []
    p1_index = 0 
    p2_index = 0
    for x in p1:
        for y in p2:
            index = p1_index + p2_index
            if index + 1 <= len(result):      #若result的长度足够容纳索引
                result[index] += x*y
            else:
                result.append(x*y)
            p2_index += 1
        p2_index = 0
        p1_index += 1
    return result

    '''result = []                          #方法2
    for x in range(len(p1)+len(p2)-1):
        result.append(0)
    p1_index = 0
    p2_index = 0
    for x in p1:
        for y in p2:
            result[p1_index+p2_index] += x*y
            p2_index += 1
        p2_index = 0
        p1_index += 1
    return result'''
    

    

def bestScrabbleScore(dictionary, letterScores, hand):
    def canCombine(dic = dictionary,han = hand):  #若手上的牌能组成字典上的单词，返回 可以组合 的单词列表
        ls = []
        flag = 0
        for x in dic:
            for y in x:
                if y in han and x.count(y) <= han.count(y):  
                    #and 后面的语句保证 hand 中的元素个数足够组合dic
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                flag = 0
                ls.append(x)
        return ls
    
    def computeScores(str,let=letterScores):    #计算字符串的分数
        score = 0
        for x in str:
            score += let[ord(x)-97]
        return score

    ls = canCombine()
    result = []
    maxscore = 0
    for x in ls:
        if computeScores(x) >= maxscore:
            maxscore = computeScores(x)
            result.append(x)
    if len(result) == 0:
        return None
    if len(result) == 1:
        result = result[0]
    return (result,maxscore)




                
    

    

#################################################
# Bonus/Optional
#################################################

def linearRegression(pointsList):
    return 42

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def _verifyAlternatingSumIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    alternatingSum(a)
    return (a == b)

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(_verifyAlternatingSumIsNondestructive())
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed!')

def _verifyMedianIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    median(a)
    return (a == b)

def testMedian():
    print('Testing median()...', end='')
    assert(_verifyMedianIsNondestructive())
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed!')

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = a + [ ] # copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed!")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed!")

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = a + [ ] # copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = a + [ ] # copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testAlternatingSum()
    testMedian()
    testSmallestDifference()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()

    # Part B:
    testIsSorted()
    testLookAndSay()
    testInverseLookAndSay()
    testMultiplyPolynomials()
    testBestScrabbleScore()

    # Bonus:
    #testLinearRegression()
    #testRunSimpleProgram() 

def main():
    cs112_f21_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
