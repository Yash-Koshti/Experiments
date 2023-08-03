import time
from turtle import *
# default minimized screen-size = 330, 285
t = Turtle()
t.pensize(3)
t.pu()
t.speed(6)

char_list = "abcdefghijklmnopqrstuvwxyz !.?"
size_dict = {'A' : 90, 'B' : 50, 'C' : 80, 'D' : 60, 'E' : 60, 'F' : 60, 'G' : 74, 'H' : 60, 'I' : 60, 'J' : 60, 
            'K' : 60, 'L' : 60, 'M' : 80, 'N' : 70, 'O' : 100, 'P' : 54, 'Q' : 100, 'R' : 60, 'S' : 66, 'T' : 80,
            'U' : 60, 'V' : 82, 'W' : 100, 'X' : 64, 'Y' : 74, 'Z' : 70, ' ' : 50, '!' : 50, '.' : 50, '?' : 60}

def chk_chars(chars):
    chars = str(chars).upper()
    total_size = 0
    
    for i in range(len(chars)): total_size += size_dict[chars[i]]

    return int(0-(total_size/2))

def frame(x, y, size):
    # t.speed(0)
    # t.home()
    # t.goto(x, y)
    # t.pensize(1)
    # t.pd()
    # for i in range(4):
    #     if i == 0 or i == 2:
    #         t.forward(size)
    #         t.right(90)
    #     else:
    #         t.forward(100)
    #         t.right(90)
    # t.pu()
    # t.pensize(3)
    t.home()
    # t.speed(6)

def alpha_A(x, y, size):
    frame(x, y, size)
    # t.home()

    t.goto(x+10, y-90)
    t.pd()
    t.left(67)
    t.forward(90)
    t.right(134)
    t.forward(90)
    t.pu()
    t.backward(45)
    t.right(112)
    t.pd()
    t.forward(35)
    t.pu()
    return x+size

def alpha_B(x, y, size):
    frame(x, y, size)
    # t.home()
    
    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.forward(10)
    t.circle(-21, 180)
    t.left(180)
    t.circle(-22, 180)
    t.forward(10)
    t.pu()
    return x+size

def alpha_C(x, y, size):
    frame(x, y, size)
    # t.home()
    
    t.goto(x+70, y-7)
    t.pd()
    t.left(160)
    t.circle(45, 220)
    t.pu()
    return x+size

def alpha_D(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.circle(-43, 180)
    t.pu()
    return x+size

def alpha_E(x, y, size):
    frame(x, y, size)

    t.goto(x+50, y-90)
    t.pd()
    t.left(180)
    t.forward(40)
    t.right(90)
    t.forward(85)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.pu()
    t.forward(42)
    t.right(90)
    t.forward(5)
    t.pd()
    t.forward(35)
    t.pu()
    return x+size

def alpha_F(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.pu()
    t.forward(42)
    t.right(90)
    t.forward(10)
    t.pd()
    t.forward(30)
    t.pu()
    return x+size

def alpha_G(x, y, size):
    frame(x, y, size)

    t.goto(x+45, y-50)
    t.pd()
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(15)
    t.circle(-43, 200)
    t.pu()
    return x+size

def alpha_H(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.pu()
    t.forward(40)
    t.right(90)
    t.pd()
    t.forward(85)
    t.backward(43)
    t.right(90)
    t.forward(40)
    t.pu()
    return x+size

def alpha_I(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-5)
    t.pd()
    t.forward(40)
    t.right(90)
    t.pu()
    t.forward(85)
    t.right(90)
    t.pd()
    t.forward(40)
    t.backward(20)
    t.right(90)
    t.forward(85)
    t.pu()
    return x+size

def alpha_J(x, y, size):
    frame(x, y, size)
    
    t.goto(x+15, y-5)
    t.pd()
    t.forward(35)
    t.right(90)
    t.forward(65)
    t.circle(-20, 180)
    t.pu()
    return x+size

def alpha_K(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.backward(43)
    t.right(45)
    t.forward(60)
    t.backward(59)
    # t.left(45)
    # t.backward(1)
    t.right(90)
    t.forward(59)
    t.pu()
    return x+size

def alpha_L(x, y, size):
    frame(x, y, size)

    t.goto(x+50, y-90)
    t.pd()
    t.left(180)
    t.forward(40)
    t.right(90)
    t.forward(85)
    t.pu()
    return x+size

def alpha_M(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(135)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(135)
    t.forward(85)
    t.pu()
    return x+size

def alpha_N(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(150)
    t.forward(98)
    t.left(150)
    t.forward(85)
    t.pu()
    return x+size

def alpha_O(x, y, size):
    frame(x, y, size)

    t.goto(x+50, y-7)
    t.pd()
    t.circle(-43, 360)
    t.pu()
    return x+size

def alpha_P(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.forward(10)
    t.circle(-25, 200)
    t.pu()
    return x+size

def alpha_Q(x, y, size):
    frame(x, y, size)

    t.goto(x+50, y-5)
    t.pd()
    t.circle(-42, 360)
    t.pu()
    t.right(90)
    t.forward(60)
    t.left(45)
    t.pd()
    t.forward(40)
    t.pu()
    return x+size

def alpha_R(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.forward(10)
    t.circle(-23, 200)
    t.left(147)
    t.forward(50)
    t.pu()
    return x+size

def alpha_S(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-90)
    t.pd()
    t.forward(25)
    t.circle(22, 180)
    t.forward(5)
    t.circle(-20, 180)
    t.forward(25)
    t.pu()
    return x+size

def alpha_T(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-5)
    t.pd()
    t.forward(60)
    t.backward(30)
    t.right(90)
    t.forward(85)
    t.pu()
    return x+size

def alpha_U(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-5)
    t.pd()
    t.right(90)
    t.forward(65)
    t.circle(20, 180)
    t.forward(65)
    t.pu()
    return x+size

def alpha_V(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-5)
    t.pd()
    t.right(70)
    t.forward(90)
    t.left(140)
    t.forward(90)
    t.pu()
    return x+size

def alpha_W(x, y, size):
    frame(x, y, size)
    
    t.goto(x+10, y-5)
    t.pd()
    t.right(74)
    t.forward(90)
    t.left(148)
    t.forward(55)
    t.right(148)
    t.forward(55)
    t.left(148)
    t.forward(90)
    t.pu()
    return x+size

def alpha_X(x, y, size):
    frame(x, y, size)

    t.goto(x+50, y-90)
    t.pd()
    t.left(113)
    t.forward(90)
    t.left(157)
    t.pu()
    t.forward(83)
    t.left(157)
    t.pd()
    t.forward(90)
    t.pu()
    return x+size

def alpha_Y(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-5)
    t.pd()
    t.right(55)
    t.forward(45)
    t.left(110)
    t.forward(45)
    t.pu()
    t.backward(45)
    t.right(145)
    t.pd()
    t.forward(50)
    t.pu()
    return x+size

def alpha_Z(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-5)
    t.pd()
    t.forward(51)
    t.right(120)
    t.forward(98)
    t.left(120)
    t.forward(51)
    t.pu()
    return x+size

def speCH_SPACE(x, y, size):
    frame(x, y, size)
    return x+size

def speCH_EXCLAMATION(x, y, size):
    frame(x, y, size)

    t.goto(x+25, y-15)
    t.pd()
    t.right(90)
    for i in range(30):
        t.pensize((30-i)/1.5)
        t.forward(2)
    t.pensize(3)
    t.pu()
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.pd()
    t.circle(5, 360)
    t.pu()
    return x+size

def speCH_PERIOD(x, y, size):
    frame(x, y, size)

    t.goto(x+20, y-85)
    t.left(180)
    t.forward(5)
    t.left(90)
    t.pd()
    t.circle(5, 360)
    t.pu()
    return x+size

def speCH_QUESTION(x, y, size):
    frame(x, y, size)

    t.goto(x+10, y-15)
    t.pd()
    t.left(60)
    t.circle(-20, 240)
    t.left(90)
    t.forward(30)
    t.pu()
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.pd()
    t.circle(5, 360)
    t.pu()
    return x+size

#"""Main function starts from here."""
word = input("Enter word:")
cnt = 0
for w in str(word).lower():
    if w in char_list:
        cnt += 1
if cnt == len(word):
    availabe_size = chk_chars(word)
    for i in range(len(word)):
        if word[i] == 'A' or word[i] == 'a': availabe_size = alpha_A(availabe_size, 50, size_dict['A'])
        elif word[i] == 'B' or word[i] == 'b': availabe_size = alpha_B(availabe_size, 50, size_dict['B'])
        elif word[i] == 'C' or word[i] == 'c': availabe_size = alpha_C(availabe_size, 50, size_dict['C'])
        elif word[i] == 'D' or word[i] == 'd': availabe_size = alpha_D(availabe_size, 50, size_dict['D'])
        elif word[i] == 'E' or word[i] == 'e': availabe_size = alpha_E(availabe_size, 50, size_dict['E'])
        elif word[i] == 'F' or word[i] == 'f': availabe_size = alpha_F(availabe_size, 50, size_dict['F'])
        elif word[i] == 'G' or word[i] == 'g': availabe_size = alpha_G(availabe_size, 50, size_dict['G'])
        elif word[i] == 'H' or word[i] == 'h': availabe_size = alpha_H(availabe_size, 50, size_dict['H'])
        elif word[i] == 'I' or word[i] == 'i': availabe_size = alpha_I(availabe_size, 50, size_dict['I'])
        elif word[i] == 'J' or word[i] == 'j': availabe_size = alpha_J(availabe_size, 50, size_dict['J'])
        elif word[i] == 'K' or word[i] == 'k': availabe_size = alpha_K(availabe_size, 50, size_dict['K'])
        elif word[i] == 'L' or word[i] == 'l': availabe_size = alpha_L(availabe_size, 50, size_dict['L'])
        elif word[i] == 'M' or word[i] == 'm': availabe_size = alpha_M(availabe_size, 50, size_dict['M'])
        elif word[i] == 'N' or word[i] == 'n': availabe_size = alpha_N(availabe_size, 50, size_dict['N'])
        elif word[i] == 'O' or word[i] == 'o': availabe_size = alpha_O(availabe_size, 50, size_dict['O'])
        elif word[i] == 'P' or word[i] == 'p': availabe_size = alpha_P(availabe_size, 50, size_dict['P'])
        elif word[i] == 'Q' or word[i] == 'q': availabe_size = alpha_Q(availabe_size, 50, size_dict['Q'])
        elif word[i] == 'R' or word[i] == 'r': availabe_size = alpha_R(availabe_size, 50, size_dict['R'])
        elif word[i] == 'S' or word[i] == 's': availabe_size = alpha_S(availabe_size, 50, size_dict['S'])
        elif word[i] == 'T' or word[i] == 't': availabe_size = alpha_T(availabe_size, 50, size_dict['T'])
        elif word[i] == 'U' or word[i] == 'u': availabe_size = alpha_U(availabe_size, 50, size_dict['U'])
        elif word[i] == 'V' or word[i] == 'v': availabe_size = alpha_V(availabe_size, 50, size_dict['V'])
        elif word[i] == 'W' or word[i] == 'w': availabe_size = alpha_W(availabe_size, 50, size_dict['W'])
        elif word[i] == 'X' or word[i] == 'x': availabe_size = alpha_X(availabe_size, 50, size_dict['X'])
        elif word[i] == 'Y' or word[i] == 'y': availabe_size = alpha_Y(availabe_size, 50, size_dict['Y'])
        elif word[i] == 'Z' or word[i] == 'z': availabe_size = alpha_Z(availabe_size, 50, size_dict['Z'])
        elif word[i] == ' ': availabe_size = speCH_SPACE(availabe_size, 50, size_dict[' '])
        elif word[i] == '!': availabe_size = speCH_EXCLAMATION(availabe_size, 50, size_dict['!'])
        elif word[i] == '.': availabe_size = speCH_PERIOD(availabe_size, 50, size_dict['.'])
        elif word[i] == '?': availabe_size = speCH_QUESTION(availabe_size, 50, size_dict['?'])
else: print("Invalid Input!")

time.sleep(2)