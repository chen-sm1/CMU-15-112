#################################################
# hw5.py
# name:
# andrew id:
#################################################

import cs112_f21_week5_linter
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

def nondestructiveRemoveRowAndCol(A, row, col):
    result = []
    for x in A:
        if A.index(x) == row:           
            continue
        result.append(x[0:])         
        #此处应复制 x 整个对象，否则后续删除 col元素时 会同时删除 A 列表的对应元素
    for x in result:
        x.pop(col)
    return result

def destructiveRemoveRowAndCol(A, row, col):
    for x in A:
        if A.index(x) == row:
            A.remove(x)
    for x in A:
        for y in x:
            if x.index(y) == col:
                x.remove(y)

    '''for x in A:
        print('aajds')
        if A.index(x) == row:
            A.remove(x)         此处对列表的修改会使循环少了一次，故失败
            continue
        for y in x:
            print(x.index(y))
            if x.index(y) == col:
                x.remove(y)'''

def matrixMultiply(m1,m2):
    '''result = []
    ls = []
    index1 = 0
    index2 = 0
    one = 0 
    print(m1,m2)
    for x in m1:
        for y in m2:
            print(index1,index2)
            if index1 == len(y):
                break
            one = x[index2] * y[index1]
            ls.append(one)
            index2 += 1
        index2 = 0
        index1 += 1
        result.append(ls)
        ls = []
    print(result)
    return result'''
    ls = []
    result = []
    one = 0
    for x in m1:
        for z in range(len(m2[0])):
            for y in range(len(m2)):
                one += x[y]*m2[y][z]
            ls.append(one)
            one = 0
        result.append(ls)
        ls = []
    return result

def isKingsTour(board):
    end = 0
    num = 1
    count = 0
    max = len(board)**2
    row1 = col1 = row2 = col2 = 100
    while end == 0:
        for x in board:
            for y in x:
                if y == num:
                    if row1 == row2 == 100:
                        row1 = board.index(x)
                        col1 = x.index(y)
                    elif not row1 == 100:
                        if not row2 == 100:
                            row1 = row2
                            col1 = col2
                        row2 = board.index(x)
                        col2 = x.index(y)
                    num += 1
                    break
                if abs(row1 - row2) < 2 and abs(col1 - col2) <2:
                    if num == max+1:
                        end = 1
                        return True
                    else:
                        count += 1
                        if count > max**2:      
                            #若一直重复循环，说明列表中的最大数到不了max，到一定次数后判定为false
                            end = 1
                            return False
                else:
                    if not row2 == 100:
                        end = 1
                        return False



                        
                        





#################################################
# Part B
#################################################

def isMagicSquare(a):
    if not len(a) == len(a[0]) :
        return False
    ls = []
    for x in a:
        for y in x:
            ls.append(y)
            if ls.count(y) >1:
                return False
            if not isinstance(y,int):
                return False

    sum1 = sum2 = sum3 = sum4 = end = 0
    for x in range(len(a)):
        for y in range(len(a[0])):
            sum1 += a[x][y]
            sum2 += a[y][x]
            if x == 0:
                sum = sum1
        if sum1 == sum2 == sum:
            sum1 = 0
            sum2 = 0
        else:
            return False
            break
        sum3 += a[x][x]
        sum4 += a[x][len(a)-1-x]
    if sum == sum3 == sum4:
        return True
    else:
        return False

        

def wordSearchWithIntegerWildcards(board, word):
    digit = []
    str = ''
    for x in board:
        for y in x:
            if isinstance(y,int):
                digit.append(y)
            else:
                str += y
    if len(word) in digit or len(word) == sum(digit):
        return True
    count = -1
    repeatAlpha = 'sai'
    for x in word:
        if x == repeatAlpha and not count == 0:          
            #如果 x 为重复的元素，则跳过，因为 x 已被万能数字代替
            count -= 0
            continue
        if not(x in str and str.count(x) >= word.count(x)):
            num = word.count(x) - str.count(x)
            if num in digit and x == word[word.index(x)+1]:
                digit.remove(num)
                repeatAlpha = x
                count = num-1
            elif num == sum(digit) and x == word[word.index(x)+1]:
                digit = []
                repeatAlpha = x
                count = num-1
            else:
                return False
    else:
        return True        
        
    

def areLegalValues(values):                
    #列表长度为 n**2, 列表元素为 0 到 n**2，1 到 n**2 最多出现一次
    for x in values:
        if values.count(x) > 1 and not x == 0:
            return False
        elif x > len(values):
            return False
    else:
        return True

def isLegalRow(board, row):
    ls = board[row]
    if areLegalValues(ls):
        return True
    else:
        return False

def isLegalCol(board, col):
    ls = []
    for x in board:
        ls.append(x[col])
    if areLegalValues(ls):
        return True 
    else:
        return False


def isLegalBlock(board, block):
    N = int(pow(len(board),0.5))
    originRow = 0 + N*(block//N)
    originCol = 0 + N*(block%N)
    ls = []
    for row in range(originRow,originRow+N):
        for col in range(originCol,originCol+N):
            ls.append(board[row][col])
    if areLegalValues(ls):
        return True 
    else:
        return False

def isLegalSudoku(board):
    for x in range(len(board)):
        if not isLegalRow(board,x): 
            return False
        elif not isLegalCol(board,x):
            return False
        elif not isLegalBlock(board,x):
            return False
    else:
        return True

#################################################
# Bonus/Optional
#################################################

def makeWordSearch(wordList, replaceEmpties):
    if wordList == []:
        return None
    board = []
    for x in range(len(wordList[0])):
        board.append([])
        for y in range(len(wordList[0])):
            board[x].append('')
        for y in range(len(wordList[0])):
            board[0][y] = wordList[0][y]
    for x in range(len(board)):
        for y in range(len(board)):
            if replaceEmpties == False and board[x][y] == '':
                board[x][y] = '-'
    print(board)
    return board

                
    

#################################################
# Test Functions (#ignore_rest)
#################################################

def testIsMagicSquare():
    print("Testing isMagicSquare()...", end="")
    assert(isMagicSquare([[42]]) == True)
    assert(isMagicSquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True)
    assert(isMagicSquare([[4-7, 9-7, 2-7], [3-7, 5-7, 7-7], [8-7, 1-7, 6-7]])
           == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMagicSquare(a))
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMagicSquare(a) == False)
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMagicSquare(a) == False)
    assert(isMagicSquare([[1, 2], [2, 1]]) == False)
    assert(isMagicSquare([[0], [0]]) == False) # Not square!
    assert(isMagicSquare([[1, 1], [1, 1]]) == False) # repeats
    assert(isMagicSquare('do not crash here!') == False)
    assert(isMagicSquare(['do not crash here!']) == False)
    assert(isMagicSquare([['do not crash here!']]) == False)
    print("Passed!")

def testNondestructiveRemoveRowAndCol():
    print('Testing nondestructiveRemoveRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testMatrixMultiply():
    print("Testing matrixMultiply()...", end='')
    m1 = [[1,2],
          [3,4]] # 2x2
    m2 = [[4],
          [5]]     # 2x1
    m3 = [[14],
          [32]]
    assert(matrixMultiply(m1,m2) == m3) 
    assert(matrixMultiply([[3, 7], [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]], 
                          [[9, 8, 3],
                           [5, 1, 3]])==
                          [[62, 31, 30],
                           [61, 37, 27],
                           [65, 44, 27],
                           [75, 46, 33],
                           [117, 73, 51],
                           [83, 60, 33]])
    assert matrixMultiply([[8]],[[5]])==[[40]]
    print("Passed!")

def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    a = [ [  3, 2, 1 ],
          [  6, 4, 9 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  2, 8, 9 ],
          [  3, 1, 7 ],
          [  4, 5, 6 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 9 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 1 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 9 ],
          [  6, 4, 1 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 1 ],
          [  6, 4, 0 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  1, 2, 3 ],
          [  7, 4, 8 ],
          [  6, 5, 9 ] ]
    assert(isKingsTour(a) == False)
    a = [ [ 3, 2, 1 ],
          [ 6, 4, 0 ],
          [ 5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    print("Passed!")

def testWordSearchWithIntegerWildcards():
    print("Testing wordSearchWithIntegerWildcards()...", end='')
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "dog") == True)
    assert(wordSearchWithIntegerWildcards(board, "cat") == True)
    assert(wordSearchWithIntegerWildcards(board, "tad") == True)
    assert(wordSearchWithIntegerWildcards(board, "cow") == False)
    board = [ [ 'd', 'o',  1  ],
              [  3 , 'a', 'c' ],
              [ 'o', 'q' ,'t' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "z") == True)
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzd") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzo") == True)
    board = [ [ 3 ] ]
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzz") == False)
    board = [ [ 'a', 'b', 'c' ],
              [ 'd',  2 , 'e' ],
              [ 'f', 'g', 'h' ]]
    assert(wordSearchWithIntegerWildcards(board, "aqqh") == True)
    assert(wordSearchWithIntegerWildcards(board, "aqqhh") == False)
    assert(wordSearchWithIntegerWildcards(board, "zz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzc") == True)
    assert(wordSearchWithIntegerWildcards(board, "zaz") == False)
    print("Passed!")

def testIsLegalSudoku():
    # From Leon Zhang!
    print("Testing isLegalSudoku()...", end="")
    board = [[0]]
    assert isLegalSudoku(board) == True
    board = [[1]]
    assert isLegalSudoku(board) == True

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [[0, 4, 0, 0],
             [0, 0, 3, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 2]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 1, 4, 3],
             [4, 3, 2, 1]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]    
    assert isLegalSudoku(board) == False

    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert isLegalSudoku(board) == True
    
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 9, 7, 9 ]
    ]
    assert isLegalSudoku(board) == False
    board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6, 8]]
    assert isLegalSudoku(board) == True
    # last number is supposed to be 8, not 10
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6,10]]
    assert isLegalSudoku(board) == False
    print("Passed!")

def testMakeWordSearch():
    print("Testing makeWordSearch()...", end="")
    board = makeWordSearch([], False)
    assert(board == None)

    board = makeWordSearch(["ab"], False)
    assert(board == [['a', 'b'], ['-', '-'] ])
    board = makeWordSearch(["ab"], True)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd"], False)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd", "de"], False)
    assert(board == [['a', 'b', '-'], ['c', 'd', '-'], ['d', 'e', '-']])
    board = makeWordSearch(["ab", "bc", "cd", "de"], True)
    assert(board == [['a', 'b', 'a'], ['c', 'd', 'c'], ['d', 'e', 'a']])

    board = makeWordSearch(["abc"], False)
    assert(board == [['a', 'b', 'c'], ['-', '-', '-'], ['-', '-', '-']])
    board = makeWordSearch(["abc"], True)
    assert(board == [['a', 'b', 'c'], ['c', 'd', 'a'], ['a', 'b', 'c']])

    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], False)
    assert(board == [['a', 'b', 'c'], ['d', 'e', '-'], ['c', 'f', 'g']])
    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], True)
    assert(board == [['a', 'b', 'c'], ['d', 'e', 'a'], ['c', 'f', 'g']])

    board = makeWordSearch(["abcd", "abc", "dcb"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['-', '-', '-', '-'], 
                     ['-', '-', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', '-', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', 'b', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           True)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', 'a'], 
                     ['b', 'a', 'd', 'e'],
                     ['c', 'e', 'b', 'a']])
    #[ (["abcd", "abc", "dcb", "xa", "by", "bya", "bbbx", "dbxa", "cbxa" ],
    #False),

    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testMatrixMultiply()
    testIsKingsTour()

    # Part B:
    testIsMagicSquare()
    testWordSearchWithIntegerWildcards()
    testIsLegalSudoku()
    #testThreeMensMorris() # this will be submitted in a separate file!

    # Bonus:
    testMakeWordSearch()

def main():
    cs112_f21_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
