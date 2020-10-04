__author__ ='tasakos'

import random
import sys


board=[[' ' for i in range(5)]for i in range(5)]#p1 board
board1=[[' ' for i in range(5)]for i in range(5)]#p2 board
player_ships1=[]# player 1 game positions
player_ships2=[]#player 1 or CPU game positions
p1shoots=[]#player 1 shoot positions
p2shoots=[]#player 2 or CPU shoot positions
str0 = 'abcde'

#update board
def uboard(*x):
    '''This function updates the player board'''
    if board[x[0]][x[1]]==' ':
        board[x[0]][x[1]]=x[4]
    if board1[x[2]][x[3]] == ' ':
        board1[x[2]][x[3]]=x[5]

#print board
def pboard():
    '''This function prints the player board'''
    print('{:>5}{:>10}'.format('P1','P2'))
    print('{0}{0:>10}'.format(' 12345'))
    for i in range(5):
        str1=''
        str2=''
        str1 +=str0[i]+board[i][0]+board[i][1]+board[i][2]+board[i][3]+board[i][4]
        str2 +=str0[i]+board1[i][0]+board1[i][1]+board1[i][2]+board1[i][3]+board1[i][4]
        print('{0}{1:>10}'.format(str1, str2))

#Get player positions
def get_pos(p):
    '''This function gets player's positions'''
    while 1:
        try:
            if p:
                for i in range(5):
                    sh = input('Player 1 enter the position of your ship no {}: '.format(i+1))
                    sht=(ord(sh[0])-97),(int(sh[1])-1)
                    while not (0<=ord(sh[0])-97<5 and 1<=int(sh[1:])<=5) or (sht in player_ships1):
                        sh = input('Invalid position, or position already taken. Try again: ')
                        sht = (ord(sh[0]) - 97), (int(sh[1]) - 1)
                    player_ships1.append(sht)
            else:
                for i in range(5):
                    sh = input('Player 1 enter the position of your ship no {}: '.format(i+1))
                    sht = (ord(sh[0]) - 97), (int(sh[1]) - 1)
                    while not (0 <= ord(sh[0]) - 97 < 5 and 1 <= int(sh[1:]) <= 5 ) or (sht in player_ships2):
                        sh = input('Invalid position, or position already taken. Try again: ')
                        sht = (ord(sh[0]) - 97), (int(sh[1]) - 1)
                    player_ships2.append(sht)
        except Exception as e:
            player_ships1.clear()
            print(e)
        else:
            break

#Get CPU positions
def cpu_pos():
    '''This function gets CPU positions'''
    while len(player_ships2) < 5:
        pos=random.randint(0,4), random.randint(0,4)
        if pos not in player_ships2:
            player_ships2.append(pos)

#CPU game handler
def cpu():
    '''This function handle CPU'''
    while len(player_ships1)!=0:
        if (player_ships2)==0:
            break
        m = random.randint(0,4),random.randint(0,4)
        while m not in p2shoots:
            p2shoots.append(m)
            print('Missile thrown at {}'.format(chr(m[0]+97)+str(m[1]+1)))
            if m in player_ships1:
                print('Target hit!')
                player_ships1.pop(player_ships1.index(m))
                uboard(m[0],m[1],0,0,'O',' ')
                pboard()
                player1(1)
            else:
                print('Target missed!')
                uboard(m[0], m[1], 0, 0, 'X', ' ')
                pboard()
                player1(1)
    else:
        print('GAME OVER. CPU wins!')
        sys.exit()

#Player 1 game handler
def player1(ch):
    '''This function handle player 1'''
    while 1:
        try:
            while len(player_ships2)!=0:
                if len(player_ships1) == 0:
                    break
                m = input('Player 1 enter the position to throw your missile: ')
                mt = (ord(m[0]) - 97), (int(m[1:]) - 1)
                while (mt in p1shoots) or not (0<=mt[0]<=4 and 0<=mt[1]<=4):
                    m= input('Invalid position, or missile already thrown there. Try again: ')
                    mt = (ord(m[0]) - 97), (int(m[1]) - 1)
                p1shoots.append(mt)
                print('P1 Missile thrown at {}'.format(m))
                if mt in player_ships2:
                    print('Target hit!')
                    player_ships2.pop(player_ships2.index(mt))
                    uboard(0,0,mt[0],mt[1],' ','O')
                    pboard()
                    if ch==2:
                        player2()
                    else:
                        cpu()
                else:
                    print('Target missed!')
                    uboard(0, 0, mt[0], mt[1], ' ', 'X')
                    pboard()
                    if ch==2:
                        player2()
                    else:
                        cpu()
            else:
                print('GAME OVER. player 1 wins!')
                sys.exit()
        except Exception as e:
            print(e)
        else:break

#PLayer 2 game handler
def player2():
    '''This function handle player 2'''
    while 1:
        try:
            while len(player_ships1)!=0:
                if len(player_ships2)==0:
                    break
                m = input('Player 2 enter the position to throw your missile: ')
                mt = (ord(m[0]) - 97), (int(m[1:]) - 1)
                while (mt in p2shoots)or not (0<=mt[0]<=4 and 0<=mt[1]<=4):
                    m=input('Invalid position, or missile already thrown there. Try again: ')
                    mt = (ord(m[0]) - 97), (int(m[1]) - 1)
                p2shoots.append(mt)
                print('Missile thrown at {}'.format(m))
                p2shoots.append(mt)
                if mt in player_ships1:
                    print('Target hit!')
                    player_ships1.pop(player_ships1.index(mt))
                    uboard(mt[0], mt[1], 0, 0, 'O', ' ')
                    pboard()
                    player1(2)
                else:
                    print('Target missed')
                    uboard(mt[0], mt[1], 0, 0, 'X', ' ')
                    pboard()
                    player1(2)
            else:
                print('GAME OVER. player 2 wins!')
                sys.exit()
        except Exception as e:
            print(e)
        else:
            break

#main program
def main():
    '''Main Function'''
    while 1:
        try:
            ch = int(input('''BATTLESHIP GAME
The objective is to sink the opponent's ships before the opponent sinks yours.
Input 1 for 1-player game or 2 for 2-player game: '''))
            if ch==2:
                get_pos(1)
                print(2000*'\n')
                get_pos(0)
                print(2000 * '\n')
                if random.randint(0,1)==0:
                    print('Player 1 starts first')
                    pboard()
                    player1(ch)
                else:
                    print('Player 2 starts first')
                    pboard()
                    player2()
            elif ch==1:
                cpu_pos()
                get_pos(1)
                print('Player 1 starts first')
                pboard()
                player1(ch)
            else:
                print('Wrong choice!')
                main()
        except Exception as e:
            print(e,'\n')
        else:
            break
if __name__ == '__main__':
    main()