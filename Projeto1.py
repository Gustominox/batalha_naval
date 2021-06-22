# coding=utf-8
from graphics import *
import random
class jogador:
    def __init__(self,tupleBarcos,tab):
        self.barcos = tupleBarcos
        self.tabuleiro = tab

class peca:
    def __init__(self,linIni,colIni,ori):
        self.linhaInicial = linIni
        self.colunaInicial = colIni
        self.orientacao = ori

class submarino(peca):
    def __init__(self,linIni,colIni,ori):
        peca.__init__(self,linIni,colIni,ori)
        self.tmh = 1
        self.estado = [1]

class fragata(peca):
    def __init__(self,linIni,colIni,ori):
        peca.__init__(self,linIni,colIni,ori)
        self.tmh = 2
        self.estado = [1, 1]

class navio(peca):
    def __init__(self,linIni,colIni,ori):
        peca.__init__(self,linIni,colIni,ori)
        self.tmh = 3
        self.estado = [1, 1, 1]

class cruzador(peca):
    def __init__(self,linIni,colIni,ori):
        peca.__init__(self,linIni,colIni,ori)
        self.tmh = 4
        self.estado = [1, 1, 1, 1]


class portaAvioes(peca):
    def __init__(self,linIni,colIni,ori):
        peca.__init__(self,linIni,colIni,ori)
        self.tmh = 5
        self.estado = [1, 1, 1, 1, 1]

def coordStrtoInt(stri):
    arr = stri.split(';')
    if len(arr) < 2:
        lin = -1
        col = -1
    else:
        lin = 9 - (ord(arr[0]) - 65)
        col = int(arr[1]) - 1
    return lin, col

def innitTupBar(win,jogador,computador,msg):
    
    while True:
        msg.setText('Coordenada inicial Submarino\nformato([A-J];[1-10])')
        coords, ori = inputEntry(win,'Setup')
        lin, col = coordStrtoInt( coords )
        if 0 <= lin < 10 and 0 <= col < 10: 
            sub = submarino(lin,col,ori)
            if colocaBarco(sub,jogador):
                jogador.barcos = (sub)
                desenhaTabs(win,jogador,computador)
                break

    while True:    
        msg.setText('Coordenada inicial Fragata\nformato([A-J];[1-10])')
        coords, ori = inputEntry(win,'Setup')
        lin, col = coordStrtoInt( coords )
        if 0 <= lin < 10 and 0 <= col < 10: 
            fra = fragata (lin,col,ori)
            if colocaBarco(fra,jogador):
                jogador.barcos = (sub,fra)
                desenhaTabs(win,jogador,computador)
                break
    while True:
        msg.setText('Coordenada inicial Navio\nformato([A-J];[1-10])')
        coords, ori = inputEntry(win,'Setup')
        lin, col = coordStrtoInt( coords )
        if 0 <= lin < 10 and 0 <= col < 10: 
            nav = navio (lin,col,ori)
            if colocaBarco(nav,jogador):
                jogador.barcos = (sub,fra,nav)
                desenhaTabs(win,jogador,computador)
                break

    while True:
        msg.setText('Coordenada inicial Cruzador\nformato([A-J];[1-10])')
        coords, ori = inputEntry(win,'Setup')
        lin, col = coordStrtoInt( coords )
        if 0 <= lin < 10 and 0 <= col < 10: 
            cru = cruzador (lin,col,ori)
            if colocaBarco(cru,jogador):    
                jogador.barcos = (sub,fra,nav,cru)
                desenhaTabs(win,jogador,computador)
                break
    
    while True:
        msg.setText('Coordenada inicial Porta-aviões\nformato([A-J];[1-10])')
        coords, ori = inputEntry(win,'Setup')
        lin, col = coordStrtoInt( coords )
        if 0 <= lin < 10 and 0 <= col < 10: 
            poA = portaAvioes (lin,col,ori)
            if colocaBarco(poA,jogador):
                jogador.barcos = (sub,fra,nav,cru,poA)
                desenhaTabs(win,jogador,computador)
                break
    


def innitTabuleiro():
    tabuleiro = []
    for j in range(0,10):
        newLine = []
        for i in range(0,10):
            newLine.append(0)
        tabuleiro.append(newLine)
    return tabuleiro 

def testaPos(barco,jogador):
    flag = True
    i = 0
    j = 0
    step = 0
    tab = jogador.tabuleiro
    for lin in tab:
        if barco.linhaInicial == i:
            for val in lin:
                if barco.colunaInicial == j:
                    while(step < barco.tmh):
                        if barco.orientacao == 'Horizontal':
                            if j+step > 9:
                                flag = False
                            elif lin[j+step] == 1:
                                flag = False
                        elif barco.orientacao == 'Vertical' :
                            if i-step < 0:
                                flag = False
                            elif tab[i-step][j] == 1:
                                flag = False
                        step += 1
                j += 1
        i += 1
    return flag

def colocaBarco(barco,jogador):
    flag = testaPos(barco,jogador)
    if flag:
        colocaBarcoAux(barco,jogador)
    return flag


def colocaBarcoAux(barco,jogador):
    i = 0
    j = 0
    step = 0
    tab = jogador.tabuleiro
    for lin in tab:
        if barco.linhaInicial == i:
            for val in lin:
                if barco.colunaInicial == j:
                    while(step < barco.tmh):
                        if barco.orientacao == 'Horizontal':
                            lin[j+step] = 1
                        elif barco.orientacao == 'Vertical':
                            tab[i-step][j] = 1
                        step += 1
                j += 1
        i += 1
    
def acertaBarco(barcos,lin,col):
    i=0
    j=0
    k=0
    for i in range(0,5):
        if barcos[i].orientacao == 'Horizontal':
            if barcos[i].linhaInicial == lin:
                for j in range(0,barcos[i].tmh):
                    if barcos[i].colunaInicial + j == col:
                                barcos[i].estado[j] = 2
                                return barcos[i]
        elif barcos[i].orientacao == 'Vertical':    
            if barcos[i].colunaInicial == col:
                for j in range(0,barcos[i].tmh):
                    if barcos[i].linhaInicial - j == lin:
                                barcos[i].estado[j] = 2
                                return barcos[i]

def jogada(lin,col,jogador,msg,user):
    i = 0
    j = 0
    msg.setText('Joagada do Adversario.\nClica em qualquer lado \npara continuar.')
    tab = jogador.tabuleiro
    for linha in tab:
        if lin == i:
            for val in linha:
                if col == j:
                    if tab[lin][col] == 0:
                        tab[lin][col] = 3
                        if user:
                            msg.setText('Acertaste na Água!\nClica em qualquer lado \npara continuar.')
                    elif tab[lin][col] == 1:
                        tab[lin][col] = 2
                        barco = acertaBarco(jogador.barcos,lin,col)
                        if user:
                            msg.setText('Acertaste num Barco!\nClica em qualquer lado \npara continuar.')
                        if barcoAfundou(barco):
                            if user:
                                msg.setText('Afundaste um Barco!\nClica em qualquer lado \npara continuar.')
                    else:
                        if user:
                            msg.setText('Ja tinhas jogado\nnessa coordenada')
                j += 1
        i += 1

    if jogoAcabou(jogador.barcos):
        return 0
    else:
        return 3

def barcoAfundou(barco):
    flag = True
    for val in barco.estado:
        if val == 1:
            flag = False
    return flag

def jogoAcabou(barcos):
    flag = True
    for barco in barcos:
        if not barcoAfundou(barco):
            flag = False
    return flag


def desenhatab(win,jogador,offset):
    for i in range(0,11):
        line = Line(Point(10,offset + 10 * i+10), Point(110 , offset + 10*i+10))
        line.draw(win)
    
    for i in range(0,11):
        line = Line(Point(10*i+10, offset + 10), Point(10*i+10,offset + 110 ))
        line.draw(win)

def desenhaPecas(win,jogador,player,offset):
    i = 0
    j = 0
    tmh = 9
    for lin in jogador.tabuleiro:
        for val in lin: 
            if val == 0:
                quadrado = Polygon(Point(10 * j + 10, offset + 10 * i + 10 ),Point(10 * j + 10, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10))
                quadrado.setFill('blue')
                quadrado.draw(win)
            if val == 1:
                if player:
                    quadrado = Polygon(Point(10 * j + 10, offset + 10 * i + 10 ),Point(10 * j + 10, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10))
                    quadrado.setFill('gray')
                    quadrado.draw(win)
                else:
                    quadrado = Polygon(Point(10 * j + 10, offset + 10 * i + 10 ),Point(10 * j + 10, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10))
                    quadrado.setFill('blue')
                    quadrado.draw(win)
            if val == 2:
                quadrado = Polygon(Point(10 * j + 10, offset + 10 * i + 10 ),Point(10 * j + 10, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10))
                quadrado.setFill('red')
                quadrado.draw(win)
            if val == 3:
                quadrado = Polygon(Point(10 * j + 10, offset + 10 * i + 10 ),Point(10 * j + 10, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10 + tmh),Point(10 * j + 10 + tmh, offset + 10 * i + 10))
                quadrado.setFill('green')
                quadrado.draw(win)
            j += 1
            if j == 10:
                j = 0
        i += 1

def inputEntry(win,modo):
    entry = Entry(Point(win.getWidth()/2+170, 230),10)
    entry.draw(win)
    
    if modo == 'Jogar':
        btJogar = Rectangle(Point(win.getWidth()/2, 150), Point(win.getWidth()/2 + 72 + 80 , 200))
        btJogar.setFill('red')
        btJogar.draw(win)
        textoJogar = Text(btJogar.getCenter(),'Jogar')
        textoJogar.draw(win)
    
    if modo == 'Setup':
        vert = Rectangle(Point(win.getWidth()/2, 150), Point(win.getWidth()/2 + 70 , 200))
        vert.setFill('green')
        vert.draw(win)
        txVert = Text(vert.getCenter(),'Vertical')
        txVert.draw(win)

    if modo == 'Setup':
        hori = Rectangle(Point(win.getWidth()/2 + 78, 150), Point(win.getWidth()/2 + 72 + 80 , 200))
        hori.setFill('green')
        hori.draw(win)
        txHori = Text(hori.getCenter(),'Horizontal')
        txHori.draw(win)

    if modo == 'Setup':
        while True:
            click = win.getMouse()
            
            if inside(click,vert):
                ori = 'Vertical'
                vert.undraw()
                txVert.undraw()
                hori.undraw()
                txHori.undraw()
                break
            elif inside(click,hori):
                ori = 'Horizontal'
                vert.undraw()
                txVert.undraw()
                hori.undraw()
                txHori.undraw()
                break
    else: 
        while True:
            click = win.getMouse()
            if inside(click,btJogar):
                btJogar.undraw()
                textoJogar.undraw()
                ori = None
                break
    
    
    coords = entry.getText()
    return coords, ori

def desenhaTabs(win,jogador,computador):
    
    desenhatab(win,jogador,0)
    desenhaPecas(win,jogador,True,0)

    desenhatab(win,computador,200)
    desenhaPecas(win,computador,False,200)


def inside(point, rectangle):
    ll = rectangle.getP1() 
    ur = rectangle.getP2()  

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def oriN():
    oriN = random.randrange(2)
    if oriN == 0:
        return 'Vertical'
    else:
        return 'Horizontal'

def computador(compu):
    
    lin = random.randrange(10)
    col = random.randrange(10)   
    ori = oriN()

    sub = submarino (lin,col,ori)
    while not testaPos(sub,compu):
        lin = random.randrange(10)
        col = random.randrange(10)
        ori = oriN()      
        sub.linhaInicial = lin
        sub.colunaInicial = col  
    colocaBarco(sub,compu)      
    compu.barcos = (sub)

    fra = fragata (lin,col,ori)
    while not testaPos(fra,compu):
        lin = random.randrange(10)
        col = random.randrange(10)
        ori = oriN()      
        fra.linhaInicial = lin
        fra.colunaInicial = col
    colocaBarco(fra,compu)        
    compu.barcos = (sub,fra)
    
    nav = navio (lin,col,ori)
    while not testaPos(nav,compu):
        lin = random.randrange(10)
        col = random.randrange(10)
        ori = oriN()      
        nav.linhaInicial = lin
        nav.colunaInicial = col        
    colocaBarco(nav,compu)
    compu.barcos = (sub,fra,nav)

    cru = cruzador (lin,col,ori)
    while not testaPos(cru,compu):
        lin = random.randrange(10)
        col = random.randrange(10)
        ori = oriN()      
        cru.linhaInicial = lin
        cru.colunaInicial = col  
    colocaBarco(cru,compu)
    compu.barcos = (sub,fra,nav,cru)

    poA = portaAvioes (lin,col,ori)
    while not testaPos(poA,compu):
        lin = random.randrange(10)
        col = random.randrange(10)
        ori = oriN()      
        poA.linhaInicial = lin
        poA.colunaInicial = col
    colocaBarco(poA,compu)        
    compu.barcos = (sub,fra,nav,cru,poA)

    return compu        

def ai():
    lin = random.randrange(10)
    col = random.randrange(10)  
    return lin ,col

def ranking(computador):
    rank = 0
    for lin in computador.tabuleiro:
        for peca in lin:
            if peca == 2:
                rank += 10
            elif peca == 3:
                rank -= 2
        
    return rank * 10

def lerRank(win):
    file = open("Ranks.txt","r")
    line = file.readline()
    offset = 0
    ranks = []
    i = 0
    while line:
        rankMsg = Text(Point(500, 350-offset),line)
        rankMsg.draw(win)
        offset += 15
        lines = line.split(':')
        ranks.append (int(lines[1][:-1]))
        line = file.readline()
        i+=1
    file.close() 
    return ranks

def escreRank(ranks):
    file = open("Ranks.txt","w")
    for i in range(0,5):
        file.write("Rank " + str(i+1) + ":" + str(ranks[i]) + '\n')
    file.close()

def insertRank(rank,ranks):    
    for i in range(0,5):
        if ranks[i] <= rank:
            ranks[i] = rank
            break
    return ranks



def menu():
    win = GraphWin('Batalha naval', 600,400)
    win.yUp()
    ranks = lerRank(win)
    msg = Text(Point(win.getWidth()/2, 230),'Batalha Naval\nClique para iniciar')
    msg.draw(win)
    win.getMouse()
    adere1 = Text(Point(63, 117),'1 2 3 4 5 6 7 8 9 10')
    adere1.setSize(9)
    adere1.draw(win)
    
    adere2 = Text(Point(63, 317),'1 2 3 4 5 6 7 8 9 10')
    adere2.setSize(9)
    adere2.draw(win)

    adere3 = Text(Point(4, 257),'A\nB\nC\nD\nE\nF\nG\nH\nI\nJ')
    adere3.setSize(7)
    adere3.draw(win)

    adere4 = Text(Point(4, 57),'A\nB\nC\nD\nE\nF\nG\nH\nI\nJ')
    adere4.setSize(7)
    adere4.draw(win)

    while (True):
        compu = jogador((),innitTabuleiro())
        player = jogador((),innitTabuleiro())
        desenhaTabs(win,player,compu)
        innitTupBar(win,player,compu,msg)
        computador(compu)
        desenhaTabs(win,player,compu)
        replay = 3
        while replay == 3: 
            msg.setText('A sua Jogada:\nformato([A-J];[1-10])')
            jog, buffer = inputEntry(win,'Jogar')
            lin, col = coordStrtoInt( jog )
            replay = jogada(lin,col,compu,msg,True)
            desenhaTabs(win,player,compu)
            win.getMouse()
            lin ,col = ai()
            replay = jogada(lin,col,player,msg,False)
            desenhaTabs(win,player,compu)
            win.getMouse()
        
        if replay == 0:
            if jogoAcabou(player.barcos):
                rank = ranking(compu)
                ranks = insertRank(rank,ranks)
                escreRank(ranks)
                msg.setText('Ganhaste!\n Pontuação: ' + str(rank))
            else:
                msg.setText('Perdeste...')

        btJogTer = Rectangle(Point(win.getWidth()/2-20, 150), Point(win.getWidth()/2 + 72 + 80 +20 , 200))
        btJogTer.setFill('blue')
        btJogTer.draw(win)
        textoJogTer = Text(btJogTer.getCenter(),'Jogar Novamente?\n(clique fora para encerrar)')
        textoJogTer.draw(win)
        click = win.getMouse()
        jogNov = inside(click,btJogTer)

        if jogNov:
            btJogTer.undraw()
            textoJogTer.undraw()
            continue
        else:
            break
        
    msg.setText('Jogo Encerrado')
    win.getMouse()
    win.close()
menu()