import pygame
from constants import *

pygame.init()
'''

        MAIN GAME DISPLAY SETTINGS

'''
# draw main game board
def generuj_plansze():
    for i in range(32):
        kolumna = i % 4
        wiersz = i // 4
        if wiersz % 2 == 0:
            pygame.draw.rect(ekran, 'light gray', [600 - (kolumna * 200), wiersz * 100, 100, 100])
        else:
            pygame.draw.rect(ekran, 'light gray', [700 - (kolumna * 200), wiersz * 100, 100, 100])
        pygame.draw.rect(ekran, 'gray', [0, 800, SZEROKOSC, 100])
        pygame.draw.rect(ekran, 'gold', [0, 800, SZEROKOSC, 100], 5)
        pygame.draw.rect(ekran, 'gold', [800, 0, 200, WYSOKOSC], 5)
        status_tekst = ['Białe: Wybierz figurę! ', 'Białe: Wybierz pole!',
                       'Czarne: Wybierz figurę!', 'Czarne: Wybierz pole!']
        ekran.blit(duza_czcionka.render(status_tekst[kolejnosc], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(ekran, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(ekran, 'black', (100 * i, 0), (100 * i, 800), 2)
        ekran.blit(srednia_czcionka.render('PODDAJ', True, 'black'), (810, 830))
# draw pieces onto board
def generuj_figury():
    for i in range(len(biale_figury)):
        index = lista_figur.index(biale_figury[i])
        if biale_figury[i] == 'pawn':
            ekran.blit(biale_pionek, (biale_lokalizacja[i][0] * 100 + 22, biale_lokalizacja[i][1] * 100 + 30))
        else:
            ekran.blit(biale_obraz[index], (biale_lokalizacja[i][0] * 100 + 10, biale_lokalizacja[i][1] * 100 + 10))
        if kolejnosc < 2:
            if wybor == i:
                pygame.draw.rect(ekran, 'red', [biale_lokalizacja[i][0] * 100 + 1, biale_lokalizacja[i][1] * 100 + 1,
                                                100, 100], 2)

    for i in range(len(czarne_figury)):
        index = lista_figur.index(czarne_figury[i])
        if czarne_figury[i] == 'pawn':
            ekran.blit(czarne_pionek, (czarne_lokalizacja[i][0] * 100 + 22, czarne_lokalizacja[i][1] * 100 + 30))
        else:
            ekran.blit(czarne_obraz[index], (czarne_lokalizacja[i][0] * 100 + 10, czarne_lokalizacja[i][1] * 100 + 10))
        if kolejnosc >= 2:
            if wybor == i:
                pygame.draw.rect(ekran, 'blue', [czarne_lokalizacja[i][0] * 100 + 1, czarne_lokalizacja[i][1] * 100 + 1,
                                                 100, 100], 2)
# draw captured pieces on side of screen
def pokaz_zbite_figury():
    for i in range(len(biale_zbite_figury)):
        zbite_figury = biale_zbite_figury[i]
        index = lista_figur.index(zbite_figury)
        ekran.blit(czarne_male_obraz[index], (825, 5 + 50 * i))
    for i in range(len(czarne_zbite_figury)):
        zbite_figury = czarne_zbite_figury[i]
        index = lista_figur.index(zbite_figury)
        ekran.blit(biale_male_obraz[index], (925, 5 + 50 * i))
# kończy grę
def pokaz_koniec_gry():
    if zwyciezca == 'draw':
        pygame.draw.rect(ekran, 'black', [200, 200, 400, 70])
        ekran.blit(czcionka.render(f'Remis! ', True, 'white'), (210, 210))
        ekran.blit(czcionka.render(f'Naciśnij ENTER aby zacząć od nowa!', True, 'white'), (210, 240))
    else:
        if zwyciezca == 'black':
            kolor = 'Czarne'
        else:
            kolor = 'Białe'
        pygame.draw.rect(ekran, 'black', [200, 200, 400, 70])
        ekran.blit(czcionka.render(f'{kolor} wygrywają! ', True, 'white'), (210, 210))
        ekran.blit(czcionka.render(f'Naciśnij ENTER aby zacząć od nowa!', True, 'white'), (210, 240))
#wyswietla dostepne ruchy roszady
def pokaz_roszada(ruchy):
    if kolejnosc < 2:
        kolor = 'red'
    else:
        kolor = 'blue'
    for i in range(len(ruchy)):
        pygame.draw.circle(ekran, kolor, (ruchy[i][0][0] * 100 + 50, ruchy[i][0][1] * 100 + 70), 8)
        ekran.blit(czcionka.render('Król', True, 'black'), (ruchy[i][0][0] * 100 + 30, ruchy[i][0][1] * 100 + 70))
        pygame.draw.circle(ekran, kolor, (ruchy[i][1][0] * 100 + 50, ruchy[i][1][1] * 100 + 70), 8)
        ekran.blit(czcionka.render('Wieża', True, 'black'),
                   (ruchy[i][1][0] * 100 + 30, ruchy[i][1][1] * 100 + 70))
        pygame.draw.line(ekran, kolor, (ruchy[i][0][0] * 100 + 50, ruchy[i][0][1] * 100 + 70),
                         (ruchy[i][1][0] * 100 + 50, ruchy[i][1][1] * 100 + 70), 2)
# okno z figurami do promocji
def promocja():
    pygame.draw.rect(ekran, 'dark gray', [800, 0, 200, 420])
    biale_promuj, czarne_promuj, promocja_index = sprawdz_promocje()
    if biale_promuj:
        kolor = 'white'
        for i in range(len(biale_promocja)):
            figura = biale_promocja[i]
            index = lista_figur.index(figura)
            ekran.blit(biale_obraz[index], (860, 5 + 100 * i))
    elif czarne_promuj:
        kolor = 'black'
        for i in range(len(czarne_promocja)):
            figura = czarne_promocja[i]
            index = lista_figur.index(figura)
            ekran.blit(czarne_obraz[index], (860, 5 + 100 * i))
    pygame.draw.rect(ekran, kolor, [800, 0, 200, 420], 8)
#podswietla pola na ktore mozna sie ruszyc
def pokaz_mozliwe_ruchy(ruchy):
    if kolejnosc < 2:
        kolor = 'red'
    else:
        kolor = 'blue'
    for i in range(len(ruchy)):
        pygame.draw.circle(ekran, kolor, (ruchy[i][0] * 100 + 50, ruchy[i][1] * 100 + 50), 5)
# obramowka dookola krola jesli ten w szachu
def pokaz_czy_szach():
    if licznik < 15:
        if biale_szach:
            king_index = biale_figury.index('king')
            king_location = biale_lokalizacja[king_index]
            pygame.draw.rect(ekran, 'dark red', [king_location[0] * 100 + 1, king_location[1] * 100 + 1, 100, 100], 5)
        elif czarne_szach:
            king_index = czarne_figury.index('king')
            king_location = czarne_lokalizacja[king_index]
            pygame.draw.rect(ekran, 'dark blue', [king_location[0] * 100 + 1, king_location[1] * 100 + 1, 100, 100], 5)


'''

        DEFINED PIECES MOVES

'''
# main function executing others that are calculating valid moves
def okresl_nastepne_ruchy():
    global biale_szach, czarne_szach, biale_opcje, czarne_opcje, zwyciezca
    biale_szach = False
    czarne_szach = False
    biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
    czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
    sprawdz_szach(biale_opcje, czarne_opcje)
    if czarne_szach:
        czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
    elif biale_szach:
        biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')

    ilosc_ruchow = 0
    for sublist in biale_opcje:
        ilosc_ruchow += len(sublist)
    if ilosc_ruchow == 0 and biale_szach:
        zwyciezca = 'black'
    elif ilosc_ruchow == 0 and not biale_szach:
        zwyciezca = 'draw'
    ilosc_ruchow = 0
    for sublist in czarne_opcje:
        ilosc_ruchow += len(sublist)
    if ilosc_ruchow == 0 and czarne_szach:
        zwyciezca = 'white'
    elif ilosc_ruchow == 0 and not czarne_szach:
        zwyciezca = 'draw'

# function to check all pieces valid options on board
def sprawdz_mozliwe_opcje(figury, lokalizacje, tura):
    global ruchy_roszada
    lista_ruchow = []
    lista_wszystkich_ruchow = []
    ruchy_roszada = []
    if tura == 'white':
        szachowane_pola = ruchy_w_szach(czarne_figury, czarne_lokalizacja, 'black')  # pozycja figur oraz ścieżke do króla
    else:
        szachowane_pola = ruchy_w_szach(biale_figury, biale_lokalizacja, 'white')  # pozycja figur oraz ścieżke do króla
    for i in range((len(figury))):
        lokalizacja = lokalizacje[i]
        figura = figury[i]
        if figura == 'pawn':
            lista_ruchow = ruchy_pionek(lokalizacja, tura)
        elif figura == 'rook':
            lista_ruchow = ruchy_wieza(lokalizacja, tura)
        elif figura == 'knight':
            lista_ruchow = ruchy_skoczek(lokalizacja, tura)
        elif figura == 'bishop':
            lista_ruchow = ruchy_goniec(lokalizacja, tura)
        elif figura == 'queen':
            lista_ruchow = ruchy_hetman(lokalizacja, tura)
        elif figura == 'king':
            lista_ruchow = []

        if szachowane_pola and lista_ruchow: # jeśli nie puste
            ostateczna_lista_ruchow = []
            for ruch in lista_ruchow:
                if ruch in szachowane_pola:
                    ostateczna_lista_ruchow.append(ruch)
            lista_wszystkich_ruchow.append(ostateczna_lista_ruchow)
        else:
            lista_wszystkich_ruchow.append(lista_ruchow)

    figura_index = figury.index('king')
    lokalizacja = lokalizacje[figura_index]
    lista_ruchow, ruchy_roszada = ruchy_krol(lokalizacja, tura)
    if tura == 'white': # jedynie do testow
        print(f"ruchy roszady {ruchy_roszada}")
    lista_wszystkich_ruchow[figura_index] = lista_ruchow

    return prognozowanie_szachu(lista_wszystkich_ruchow, tura)
    #return lista_wszystkich_ruchow
# check for valid moves for just selected piece
def sprawdz_mozliwe_ruchy():
    if kolejnosc < 2:
        #lista_opcji = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
        lista_opcji = biale_opcje
    else:
        #lista_opcji = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
        lista_opcji = czarne_opcje
    mozliwe_opcje = lista_opcji[wybor]
    return mozliwe_opcje
# checking if king is in check
def sprawdz_szach(biale_opcje, czarne_opcje):
    global szach, biale_szach, czarne_szach
    #szach = False
    biale_szach = False
    czarne_szach = False
    biale_krol_index = biale_figury.index('king')
    biale_krol_lokalizacja = biale_lokalizacja[biale_krol_index]
    czarne_krol_index = czarne_figury.index('king')
    czarne_krol_lokalizacja = czarne_lokalizacja[czarne_krol_index]

    for sublist in czarne_opcje:
        if biale_krol_lokalizacja in sublist:
            biale_szach = True
            #szach = True
            sublist.remove(biale_krol_lokalizacja)
            biale_ruch[biale_krol_index] = True
    for sublist2 in biale_opcje:
        if czarne_krol_lokalizacja in sublist2:
            czarne_szach = True
            #szach = True
            sublist2.remove(czarne_krol_lokalizacja)
            czarne_ruch[czarne_krol_index] = True


# default pieces valid moves
def ruchy_krol(pozycja, kolor):
    lista_ruchow = []
    ruchy_roszady = sprawdz_roszade(kolor)
    if kolor == 'white':
        lista_przyjaciol = biale_lokalizacja
        pozycja_krola = czarne_lokalizacja[czarne_figury.index('king')]
    else:
        lista_przyjaciol = czarne_lokalizacja
        pozycja_krola = biale_lokalizacja[biale_figury.index('king')]
    # 8 squares to check for kings, they can go one square any direction
    cele = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        cel = (pozycja[0] + cele[i][0], pozycja[1] + cele[i][1])
        krol_w_zasiegu = False
        if cel not in lista_przyjaciol and 0 <= cel[0] <= 7 and 0 <= cel[1] <= 7:
            #król nie może stać obok króla
            for i in range(8):
                cel2 = (cel[0] + cele[i][0], cel[1] + cele[i][1])
                if cel2 == pozycja_krola and 0 <= cel2[0] <= 7 and 0 <= cel2[1] <= 7:
                    krol_w_zasiegu = True
                    break
            if not krol_w_zasiegu:
                lista_ruchow.append(cel)
    return lista_ruchow, ruchy_roszady
def ruchy_pionek(pozycja, kolor):
    lista_ruchow = []
    if kolor == 'white':
        if (pozycja[0], pozycja[1] + 1) not in biale_lokalizacja and \
                (pozycja[0], pozycja[1] + 1) not in czarne_lokalizacja and pozycja[1] < 7:
            lista_ruchow.append((pozycja[0], pozycja[1] + 1))
            # indent the check for two spaces ahead, so it is only checked if one space ahead is also open
            if (pozycja[0], pozycja[1] + 2) not in biale_lokalizacja and \
                    (pozycja[0], pozycja[1] + 2) not in czarne_lokalizacja and pozycja[1] == 1:
                lista_ruchow.append((pozycja[0], pozycja[1] + 2))
        if (pozycja[0] + 1, pozycja[1] + 1) in czarne_lokalizacja:
            lista_ruchow.append((pozycja[0] + 1, pozycja[1] + 1))
        if (pozycja[0] - 1, pozycja[1] + 1) in czarne_lokalizacja:
            lista_ruchow.append((pozycja[0] - 1, pozycja[1] + 1))
        # add en passant move checker
        if (pozycja[0] + 1, pozycja[1] + 1) == czarne_w_przelocie:
            lista_ruchow.append((pozycja[0] + 1, pozycja[1] + 1))
        if (pozycja[0] - 1, pozycja[1] + 1) == czarne_w_przelocie:
            lista_ruchow.append((pozycja[0] - 1, pozycja[1] + 1))
    else:
        if (pozycja[0], pozycja[1] - 1) not in biale_lokalizacja and \
                (pozycja[0], pozycja[1] - 1) not in czarne_lokalizacja and pozycja[1] > 0:
            lista_ruchow.append((pozycja[0], pozycja[1] - 1))
            # indent the check for two spaces ahead, so it is only checked if one space ahead is also open
            if (pozycja[0], pozycja[1] - 2) not in biale_lokalizacja and \
                    (pozycja[0], pozycja[1] - 2) not in czarne_lokalizacja and pozycja[1] == 6:
                lista_ruchow.append((pozycja[0], pozycja[1] - 2))
        if (pozycja[0] + 1, pozycja[1] - 1) in biale_lokalizacja:
            lista_ruchow.append((pozycja[0] + 1, pozycja[1] - 1))
        if (pozycja[0] - 1, pozycja[1] - 1) in biale_lokalizacja:
            lista_ruchow.append((pozycja[0] - 1, pozycja[1] - 1))
        # add en passant move checker
        if (pozycja[0] + 1, pozycja[1] - 1) == biale_w_przelocie:
            lista_ruchow.append((pozycja[0] + 1, pozycja[1] - 1))
        if (pozycja[0] - 1, pozycja[1] - 1) == biale_w_przelocie:
            lista_ruchow.append((pozycja[0] - 1, pozycja[1] - 1))
    return lista_ruchow
def ruchy_skoczek(pozycja, kolor):
    lista_ruchow = []
    if kolor == 'white':
        lista_wrogow = czarne_lokalizacja
        lista_przyjaciol = biale_lokalizacja
    else:
        lista_przyjaciol = czarne_lokalizacja
        lista_wrogow = biale_lokalizacja
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    cele = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        cel = (pozycja[0] + cele[i][0], pozycja[1] + cele[i][1])
        if cel not in lista_przyjaciol and 0 <= cel[0] <= 7 and 0 <= cel[1] <= 7:
            lista_ruchow.append(cel)
    return lista_ruchow
def ruchy_wieza(pozycja, kolor):
    lista_ruchow = []
    if kolor == 'white':
        lista_wrogow = czarne_lokalizacja
        lista_przyjaciol = biale_lokalizacja
    else:
        lista_przyjaciol = czarne_lokalizacja
        lista_wrogow = biale_lokalizacja
    for i in range(4):  # down, up, right, left
        sciezka = True
        lancuch = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while sciezka:
            if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) not in lista_przyjaciol and \
                    0 <= pozycja[0] + (lancuch * x) <= 7 and 0 <= pozycja[1] + (lancuch * y) <= 7:
                lista_ruchow.append((pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)))
                if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) in lista_wrogow:
                    sciezka = False
                lancuch += 1
            else:
                sciezka = False
    return lista_ruchow
def ruchy_goniec(pozycja, kolor):
    lista_ruchow = []
    if kolor == 'white':
        lista_wrogow = czarne_lokalizacja
        lista_przyjaciol = biale_lokalizacja
    else:
        lista_przyjaciol = czarne_lokalizacja
        lista_wrogow = biale_lokalizacja
    for i in range(4):  # up-right, up-left, down-right, down-left
        sciezka = True
        lancuch = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while sciezka:
            if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) not in lista_przyjaciol and \
                    0 <= pozycja[0] + (lancuch * x) <= 7 and 0 <= pozycja[1] + (lancuch * y) <= 7:
                lista_ruchow.append((pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)))
                if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) in lista_wrogow:
                    sciezka = False
                lancuch += 1
            else:
                sciezka = False
    return lista_ruchow
def ruchy_hetman(pozycja, kolor):
    lista_ruchow = ruchy_goniec(pozycja, kolor)
    druga_lista = ruchy_wieza(pozycja, kolor)
    for i in range(len(druga_lista)):
        lista_ruchow.append(druga_lista[i])
    return lista_ruchow


'''

        DEFINING AVAILABLE MOVES IF KING IN CHECK

'''


#zapisuje pozycje figur szachujących króla oraz ścieżke do króla
def ruchy_w_szach(figury, lokalizacje, tura):
    lista_ruchow = []
    lista_wszystkich_ruchow = []
    if biale_szach:
        pozycja_krola = biale_lokalizacja[biale_figury.index('king')]
    elif czarne_szach:
        pozycja_krola = czarne_lokalizacja[czarne_figury.index('king')]
    else:
        return lista_wszystkich_ruchow

    for i in range((len(figury))):
        lokalizacja = lokalizacje[i]
        figura = figury[i]
        if figura == 'pawn':
            lista_ruchow = ruchy_pionek_w_szach(lokalizacja, tura)
        elif figura == 'rook':
            lista_ruchow = ruchy_wieza_w_szach(lokalizacja, tura)
        elif figura == 'knight':
            lista_ruchow = ruchy_skoczek_w_szach(lokalizacja, tura)
        elif figura == 'bishop':
            lista_ruchow = ruchy_goniec_w_szach(lokalizacja, tura)
        elif figura == 'queen':
            lista_ruchow = ruchy_hetman_w_szach(lokalizacja, tura)
        elif figura == 'king':
            #lista_ruchow = ruchy_krol_w_szachu(lokalizacja, tura, lista_wszystkich_ruchow)
            #lista_ruchow, ruchy_roszady = ruchy_krol(lokalizacja, tura)
            lista_ruchow = []
        lista_wszystkich_ruchow.append(lista_ruchow)
    #dodac ruchy krola ----------------------------------------------------------------------------------------------------------------------------

    temp_wszystkie_ruchy = []
    for i in range((len(figury))):  # mozna sie tylko ruszyc w miejsca szachowane, przeksztalca listy w jedna
        if lista_wszystkich_ruchow[i]:
            for ruch in lista_wszystkich_ruchow[i]:
                if ruch not in temp_wszystkie_ruchy and ruch != pozycja_krola:
                    temp_wszystkie_ruchy.append(ruch)
    if temp_wszystkie_ruchy:
        return temp_wszystkie_ruchy
    return lista_wszystkich_ruchow
# valid moves while in check
def ruchy_pionek_w_szach(pozycja, kolor): #jeszcze nie zrobione
    lista_ruchow = []
    if kolor == 'white':
        pozycja_krola = czarne_lokalizacja[czarne_figury.index('king')]
        if (pozycja[0] + 1, pozycja[1] + 1) == pozycja_krola:
            lista_ruchow.append((pozycja[0], pozycja[1]))
        elif (pozycja[0] - 1, pozycja[1] + 1) == pozycja_krola:
            lista_ruchow.append((pozycja[0], pozycja[1]))
    else:
        pozycja_krola = biale_lokalizacja[biale_figury.index('king')]
        if (pozycja[0] + 1, pozycja[1] - 1) == pozycja_krola:
            lista_ruchow.append((pozycja[0], pozycja[1]))
        if (pozycja[0] - 1, pozycja[1] - 1) == pozycja_krola:
            lista_ruchow.append((pozycja[0], pozycja[1]))
    return lista_ruchow
def ruchy_skoczek_w_szach(pozycja, kolor):
    if kolor == 'white':
        pozycja_krola = czarne_lokalizacja[czarne_figury.index('king')]
    else:
        pozycja_krola = biale_lokalizacja[biale_figury.index('king')]
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    cele = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for kierunek in cele:
        cel = (pozycja[0] + kierunek[0], pozycja[1] + kierunek[1])
        if cel == pozycja_krola:
            return [(pozycja[0], pozycja[1])]
    return []
def ruchy_wieza_w_szach(pozycja, kolor):
    lista_ruchow = []
    if kolor == 'white':
        lista_przyjaciol = biale_lokalizacja
        pozycja_krola = czarne_lokalizacja[czarne_figury.index('king')]
    else:
        lista_przyjaciol = czarne_lokalizacja
        pozycja_krola = biale_lokalizacja[biale_figury.index('king')]

    for i in range(4):  # down, up, right, left
        temp_lista_ruchow = []
        sciezka = True
        lancuch = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while sciezka:
            if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) not in lista_przyjaciol and \
                    0 <= pozycja[0] + (lancuch * x) <= 7 and 0 <= pozycja[1] + (lancuch * y) <= 7: #granice planszy
                temp_lista_ruchow.append((pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)))
                if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) == pozycja_krola:
                    temp_lista_ruchow.append((pozycja[0], pozycja[1]))
                    for each in temp_lista_ruchow:
                        lista_ruchow.append(each)
                    return lista_ruchow
                lancuch += 1
            else:
                sciezka = False
    return lista_ruchow
def ruchy_goniec_w_szach(pozycja, kolor):
    lista_ruchow = []
    temp_lista_ruchow = []
    if kolor == 'white':
        lista_przyjaciol = biale_lokalizacja
        pozycja_krola = czarne_lokalizacja[czarne_figury.index('king')]
    else:
        lista_przyjaciol = czarne_lokalizacja
        pozycja_krola = biale_lokalizacja[biale_figury.index('king')]
    for i in range(4):  # up-right, up-left, down-right, down-left
        sciezka = True
        lancuch = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while sciezka:
            if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) not in lista_przyjaciol and \
                    0 <= pozycja[0] + (lancuch * x) <= 7 and 0 <= pozycja[1] + (lancuch * y) <= 7: #granice planszy
                temp_lista_ruchow.append((pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)))
                if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) == pozycja_krola:
                    sciezka = False
                    temp_lista_ruchow.append((pozycja[0], pozycja[1]))
                    return temp_lista_ruchow
                lancuch += 1
            else:
                sciezka = False
        temp_lista_ruchow = []
    return lista_ruchow
def ruchy_hetman_w_szach(pozycja, kolor):
    lista_ruchow = ruchy_goniec_w_szach(pozycja, kolor)
    druga_lista = ruchy_wieza_w_szach(pozycja, kolor)
    for i in range(len(druga_lista)):
        lista_ruchow.append(druga_lista[i])
    return lista_ruchow

'''

        BLOCK PIECES CAUSING CHECK

'''
# blokowanie figur, których ruch prowadzi do szachu
def prognozowanie_szachu(dostepne_ruchy, tura):
    tymczasowe_wszystkie_ruchy = [[] for _ in range(len(dostepne_ruchy))]
    if tura == 'white':
        figury = biale_figury
        wspolrzedne = biale_lokalizacja  # współrzędne wszystkich białych figur
        wrogowie_figury = czarne_figury
        wrogowie_lokalizacja = czarne_lokalizacja
    else:
        figury = czarne_figury
        wspolrzedne = czarne_lokalizacja # współrzędne wszystkich czarnych figur
        wrogowie_figury = biale_figury
        wrogowie_lokalizacja = biale_lokalizacja

    for i in range(len(figury)): # dla każdej figury
        if dostepne_ruchy[i]: # jeżeli nie poste
            temp = wspolrzedne[i] # temp = oryginalna lokalizacja figury
            for j in range(len(dostepne_ruchy[i])): # dla każdego możliwego ruchu
                wspolrzedne[i] = dostepne_ruchy[i][j] # przenieś figurę do możliwego ruchu
                temp_figury = wrogowie_figury.copy() # temp_figury = tymczasowe figury przeciwnika
                temp_lokalizacja = wrogowie_lokalizacja.copy() # temp_lokalizacja = tymczasowe lokalizacje przeciwnika
                if wspolrzedne[i] in temp_lokalizacja: # jeżeli ruch zbija figurę
                    temp_figury.pop(temp_lokalizacja.index(wspolrzedne[i]))
                    temp_lokalizacja.pop(temp_lokalizacja.index(wspolrzedne[i])) # tymczasowo usuń zbitą figurę
                czy_szach = czy_wystepuje_szach(figury, wspolrzedne, tura, temp_figury, temp_lokalizacja) # czy po wykonaniu ruchu wystąpił by szach
                if not czy_szach:
                    tymczasowe_wszystkie_ruchy[i].append(dostepne_ruchy[i][j])
            wspolrzedne[i] = temp
    return tymczasowe_wszystkie_ruchy
def czy_wystepuje_szach(figury, wspolrzedne, tura, wrogowie_figury, wrogowie_lokalizacja):
    lista_ruchow = []
    prognozowane_ruchy = []
    pozycja_krola = wspolrzedne[figury.index('king')]
    if tura == 'white':
        kolor = 'black'
    else: # tura == 'black'
        kolor = 'white'

    # dla tury bialych sprawdzamy ruchy czarnych itd
    for i in range(len(wrogowie_figury)):
        pozycja_wroga = wrogowie_lokalizacja[i]
        figura_wroga = wrogowie_figury[i]
        if figura_wroga == 'pawn':
            # pozycja_wroga - lokalizacja czarnej figury dla wejsciowa tura = 'white'
            # kolor - czarne dla wejsciowa tura = 'white'
            # wrogowie_lokalizacja - czarne_lokalizacje dla wejsciowa tura = 'white'
            # wspolrzedne - zmienione biale_lokalizacja dla wejsciowa tura = 'black'
            lista_ruchow = prognoza_pionek(pozycja_wroga, kolor, wrogowie_lokalizacja)
        elif figura_wroga == 'rook':
            lista_ruchow = prognoza_wieza(pozycja_wroga, wrogowie_lokalizacja, wspolrzedne)
        elif figura_wroga == 'knight':
            lista_ruchow = prognoza_skoczek(pozycja_wroga, wrogowie_lokalizacja)
        elif figura_wroga == 'bishop':
            lista_ruchow = prognoza_goniec(pozycja_wroga, wrogowie_lokalizacja, wspolrzedne)
        elif figura_wroga == 'queen':
            lista_ruchow = prognoza_hetman(pozycja_wroga, wrogowie_lokalizacja, wspolrzedne)
        elif figura_wroga == 'king': # krol nie moze szachowac wiec po co go sprawdzac
            lista_ruchow = []
        prognozowane_ruchy.append(lista_ruchow)

    for sublist in prognozowane_ruchy:
        if pozycja_krola in sublist:
            return True
    return False

# pieces moves
def prognoza_roszada(kolor, wspolrzedne, wrogowie_lokalizacja):
    # king must not currently be in check, neither the rook nor king has moved previously, nothing between
    # and the king does not pass through or finish on an attacked piece
    ruchy_roszady = []  # store each valid castle move as [((king_coords), (castle_coords))]
    wieza_indexy = []
    wieza_lokalizacje = []
    krol_index = 0
    krol_pozycja = (0, 0)
    if kolor == 'white':
        for i in range(len(biale_figury)):
            if biale_figury[i] == 'rook':
                wieza_indexy.append(biale_ruch[i])
                wieza_lokalizacje.append(wrogowie_lokalizacja[i])
            if biale_figury[i] == 'king':
                krol_index = i
                krol_pozycja = wrogowie_lokalizacja[i]
        if not biale_ruch[krol_index] and False in wieza_indexy and not biale_szach:
            for i in range(len(wieza_indexy)):
                roszada = True
                if wieza_lokalizacje[i][0] > krol_pozycja[0]:
                    puste_pola = [(krol_pozycja[0] + 1, krol_pozycja[1]), (krol_pozycja[0] + 2, krol_pozycja[1]),
                                     (krol_pozycja[0] + 3, krol_pozycja[1])]
                else:
                    puste_pola = [(krol_pozycja[0] - 1, krol_pozycja[1]), (krol_pozycja[0] - 2, krol_pozycja[1])]
                for j in range(len(puste_pola)):
                    if puste_pola[j] in wrogowie_lokalizacja or puste_pola[j] in wspolrzedne or \
                            puste_pola[j] in czarne_opcje or wieza_indexy[i]:
                        roszada = False
                if roszada:
                    ruchy_roszady.append((puste_pola[1], puste_pola[0]))
    else:
        for i in range(len(czarne_figury)):
            if czarne_figury[i] == 'rook':
                wieza_indexy.append(czarne_ruch[i])
                wieza_lokalizacje.append(wspolrzedne[i])
            if czarne_figury[i] == 'king':
                krol_index = i
                krol_pozycja = wspolrzedne[i]
        if not czarne_ruch[krol_index] and False in wieza_indexy and not czarne_szach:
            for i in range(len(wieza_indexy)):
                roszada = True
                if wieza_lokalizacje[i][0] > krol_pozycja[0]:
                    puste_pola = [(krol_pozycja[0] + 1, krol_pozycja[1]), (krol_pozycja[0] + 2, krol_pozycja[1]),
                                     (krol_pozycja[0] + 3, krol_pozycja[1])]
                else:
                    puste_pola = [(krol_pozycja[0] - 1, krol_pozycja[1]), (krol_pozycja[0] - 2, krol_pozycja[1])]
                for j in range(len(puste_pola)):
                    if puste_pola[j] in wrogowie_lokalizacja or puste_pola[j] in wspolrzedne or \
                            puste_pola[j] in biale_opcje or wieza_indexy[i]:
                        roszada = False
                if roszada:
                    ruchy_roszady.append((puste_pola[1], puste_pola[0]))
    return ruchy_roszady
def prognoza_pionek(pozycjaA, kolor, przyjaciele):
    lista_ruchow = []
    if kolor == 'white':
        if (pozycjaA[0] + 1, pozycjaA[1] + 1) in przyjaciele:
            lista_ruchow.append((pozycjaA[0] + 1, pozycjaA[1] + 1))
        if (pozycjaA[0] - 1, pozycjaA[1] + 1) in przyjaciele:
            lista_ruchow.append((pozycjaA[0] - 1, pozycjaA[1] + 1))
    else:
        if (pozycjaA[0] + 1, pozycjaA[1] - 1) in przyjaciele:
            lista_ruchow.append((pozycjaA[0] + 1, pozycjaA[1] - 1))
        if (pozycjaA[0] - 1, pozycjaA[1] - 1) in przyjaciele:
            lista_ruchow.append((pozycjaA[0] - 1, pozycjaA[1] - 1))
    return lista_ruchow
def prognoza_skoczek(pozycjaA, przyjaciele):
    lista_ruchow = []
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    cele = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        cel = (pozycjaA[0] + cele[i][0], pozycjaA[1] + cele[i][1])
        if cel not in przyjaciele and 0 <= cel[0] <= 7 and 0 <= cel[1] <= 7:
            lista_ruchow.append(cel)
    return lista_ruchow
def prognoza_wieza(pozycja, przyjaciele, wrogowie):
    lista_ruchow = []
    for i in range(4):  # down, up, right, left
        sciezka = True
        lancuch = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while sciezka:
            if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) not in przyjaciele and \
                    0 <= pozycja[0] + (lancuch * x) <= 7 and 0 <= pozycja[1] + (lancuch * y) <= 7:
                lista_ruchow.append((pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)))
                if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) in wrogowie:
                    sciezka = False
                lancuch += 1
            else:
                sciezka = False
    return lista_ruchow
def prognoza_goniec(pozycja, przyjaciele, wrogowie):
    lista_ruchow = []
    for i in range(4):  # up-right, up-left, down-right, down-left
        sciezka = True
        lancuch = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while sciezka:
            if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) not in przyjaciele and \
                    0 <= pozycja[0] + (lancuch * x) <= 7 and 0 <= pozycja[1] + (lancuch * y) <= 7:
                lista_ruchow.append((pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)))
                if (pozycja[0] + (lancuch * x), pozycja[1] + (lancuch * y)) in wrogowie:
                    sciezka = False
                lancuch += 1
            else:
                sciezka = False
    return lista_ruchow
def prognoza_hetman(pozycja, przyjaciele, wrogowie):
    lista_ruchow = prognoza_goniec(pozycja, przyjaciele, wrogowie)
    druga_lista = prognoza_wieza(pozycja, przyjaciele, wrogowie)
    for i in range(len(druga_lista)):
        lista_ruchow.append(druga_lista[i])
    return lista_ruchow

'''

        DEFINED ADVANCE PIECES MOVES

'''
def sprawdz_bicie_w_przelocie(stare_wspolrzedne, nowe_wspolrzedne):
    if kolejnosc <= 1:
        index = biale_lokalizacja.index(stare_wspolrzedne)
        wspolrzedne_w_przelocie = (nowe_wspolrzedne[0], nowe_wspolrzedne[1] - 1)
        figura = biale_figury[index]
    else:
        index = czarne_lokalizacja.index(stare_wspolrzedne)
        wspolrzedne_w_przelocie = (nowe_wspolrzedne[0], nowe_wspolrzedne[1] + 1)
        figura = czarne_figury[index]
    if figura == 'pawn' and abs(stare_wspolrzedne[1] - nowe_wspolrzedne[1]) > 1:
        # if piece was pawn and moved two spaces, return EP coords as defined above
        pass
    else:
        wspolrzedne_w_przelocie = (100, 100)
    return wspolrzedne_w_przelocie
def sprawdz_roszade(kolor):
    # king must not currently be in check, neither the rook nor king has moved previously, nothing between
    # and the king does not pass through or finish on an attacked piece
    ruchy_roszady = []  # store each valid castle move as [((king_coords), (castle_coords))]
    wieza_indexy = []
    wieza_lokalizacje = []
    krol_index = 0
    krol_pozycja = (0, 0)
    if kolor == 'white':
        for i in range(len(biale_figury)):
            if biale_figury[i] == 'rook':
                wieza_indexy.append(biale_ruch[i])
                wieza_lokalizacje.append(biale_lokalizacja[i])
            if biale_figury[i] == 'king':
                krol_index = i
                krol_pozycja = biale_lokalizacja[i]
        if not biale_ruch[krol_index] and False in wieza_indexy: # and not biale_szach:
            for i in range(len(wieza_indexy)):
                roszada = True
                if wieza_lokalizacje[i][0] > krol_pozycja[0]:
                    puste_pola = [(krol_pozycja[0] + 1, krol_pozycja[1]), (krol_pozycja[0] + 2, krol_pozycja[1]),
                                     (krol_pozycja[0] + 3, krol_pozycja[1])]
                else:
                    puste_pola = [(krol_pozycja[0] - 1, krol_pozycja[1]), (krol_pozycja[0] - 2, krol_pozycja[1])]
                for j in range(len(puste_pola)):
                    if puste_pola[j] in biale_lokalizacja or puste_pola[j] in czarne_lokalizacja or \
                            puste_pola[j] in czarne_opcje or wieza_indexy[i]:
                        roszada = False
                if roszada:
                    ruchy_roszady.append((puste_pola[1], puste_pola[0]))
    else:
        for i in range(len(czarne_figury)):
            if czarne_figury[i] == 'rook':
                wieza_indexy.append(czarne_ruch[i])
                wieza_lokalizacje.append(czarne_lokalizacja[i])
            if czarne_figury[i] == 'king':
                krol_index = i
                krol_pozycja = czarne_lokalizacja[i]
        if not czarne_ruch[krol_index] and False in wieza_indexy: # and not czarne_szach:
            for i in range(len(wieza_indexy)):
                roszada = True
                if wieza_lokalizacje[i][0] > krol_pozycja[0]:
                    puste_pola = [(krol_pozycja[0] + 1, krol_pozycja[1]), (krol_pozycja[0] + 2, krol_pozycja[1]),
                                     (krol_pozycja[0] + 3, krol_pozycja[1])]
                else:
                    puste_pola = [(krol_pozycja[0] - 1, krol_pozycja[1]), (krol_pozycja[0] - 2, krol_pozycja[1])]
                for j in range(len(puste_pola)):
                    if puste_pola[j] in biale_lokalizacja or puste_pola[j] in czarne_lokalizacja or \
                            puste_pola[j] in biale_opcje or wieza_indexy[i]:
                        roszada = False
                if roszada:
                    ruchy_roszady.append((puste_pola[1], puste_pola[0]))
    return ruchy_roszady
# add pawn promotion
def sprawdz_promocje():
    pionek_indexy = []
    biale_promuj = False
    czarne_promuj = False
    promocja_index = 100
    for i in range(len(biale_figury)):
        if biale_figury[i] == 'pawn':
            pionek_indexy.append(i)
    for i in range(len(pionek_indexy)):
        if biale_lokalizacja[pionek_indexy[i]][1] == 7:
            biale_promuj = True
            promocja_index = pionek_indexy[i]
    pionek_indexy = []
    for i in range(len(czarne_figury)):
        if czarne_figury[i] == 'pawn':
            pionek_indexy.append(i)
    for i in range(len(pionek_indexy)):
        if czarne_lokalizacja[pionek_indexy[i]][1] == 0:
            czarne_promuj = True
            promocja_index = pionek_indexy[i]
    return biale_promuj, czarne_promuj, promocja_index
# select piece you want to promote to
def sprawdz_wybor_promocji():
    biale_promuj, czarne_promuj, promocja_index = sprawdz_promocje()
    mysz_pozycja = pygame.mouse.get_pos()
    lewy_wcisniety = pygame.mouse.get_pressed()[0]
    x_pozycja = mysz_pozycja[0] // 100
    y_pozycja = mysz_pozycja[1] // 100
    if biale_promuj and lewy_wcisniety and x_pozycja > 7 and y_pozycja < 4:
        biale_figury[index_promocja] = biale_promocja[y_pozycja]
    elif czarne_promuj and lewy_wcisniety and x_pozycja > 7 and y_pozycja < 4:
        czarne_figury[index_promocja] = czarne_promocja[y_pozycja]


# main game loop -------------------------------------------------------------------------------------------------------
biale_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn']
biale_lokalizacja = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                     (4, 1)]
czarne_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                 'pawn']
czarne_lokalizacja = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                      (5, 6)]
# na sprawdzenie mat i pat
'''biale_figury = ['king']
biale_lokalizacja = [(0, 0)]
czarne_figury = ['rook', 'rook', 'king']
czarne_lokalizacja = [(1, 7), (2, 7), (7, 7)]'''
'''
                    ^^^^^^ UŁOŻENIE FIGUR POD TESTY ^^^^^^
                    
                    
                    
'''

biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
uruchom = True
koniec_gry = False
while uruchom:
    zegar.tick(fps)
    if licznik < 30:
        licznik += 1
    else:
        licznik = 0
    ekran.fill('dark gray')
    generuj_plansze()
    generuj_figury()
    pokaz_zbite_figury()
    pokaz_czy_szach()
    if not koniec_gry:
        biale_promuj, czarne_promuj, index_promocja = sprawdz_promocje()
        if biale_promuj or czarne_promuj:
            promocja()
            sprawdz_wybor_promocji()
            okresl_nastepne_ruchy() # biale_opcje, czarne_opcje, czy szach
    if wybor != 100:
        dostepne_ruchy = sprawdz_mozliwe_ruchy()
        pokaz_mozliwe_ruchy(dostepne_ruchy)
        if wybrany_element == 'king':
            pokaz_roszada(ruchy_roszada)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchom = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not koniec_gry:
            x_wspolrzedna = event.pos[0] // 100
            y_wspolrzedna = event.pos[1] // 100
            klikniecie_wspolrzedna = (x_wspolrzedna, y_wspolrzedna)
            if kolejnosc <= 1:
                if klikniecie_wspolrzedna == (8, 8) or klikniecie_wspolrzedna == (9, 8):
                    zwyciezca = 'black'
                if klikniecie_wspolrzedna in biale_lokalizacja:
                    wybor = biale_lokalizacja.index(klikniecie_wspolrzedna)
                    # check what piece is selected, so you can only draw castling moves if king is selected
                    wybrany_element = biale_figury[wybor]
                    if kolejnosc == 0:
                        kolejnosc = 1
                if klikniecie_wspolrzedna in dostepne_ruchy and wybor != 100:
                    biale_w_przelocie = sprawdz_bicie_w_przelocie(biale_lokalizacja[wybor], klikniecie_wspolrzedna)
                    biale_lokalizacja[wybor] = klikniecie_wspolrzedna
                    biale_ruch[wybor] = True
                    if klikniecie_wspolrzedna in czarne_lokalizacja:
                        czarne_figura = czarne_lokalizacja.index(klikniecie_wspolrzedna)
                        biale_zbite_figury.append(czarne_figury[czarne_figura])
                        czarne_figury.pop(czarne_figura)
                        czarne_lokalizacja.pop(czarne_figura)
                        czarne_ruch.pop(czarne_figura)
                    # adding check if en passant pawn was captured
                    if klikniecie_wspolrzedna == czarne_w_przelocie:
                        czarne_figura = czarne_lokalizacja.index((czarne_w_przelocie[0], czarne_w_przelocie[1] - 1))
                        biale_zbite_figury.append(czarne_figury[czarne_figura])
                        czarne_figury.pop(czarne_figura)
                        czarne_lokalizacja.pop(czarne_figura)
                        czarne_ruch.pop(czarne_figura)
                    okresl_nastepne_ruchy() # biale_opcje, czarne_opcje, czy szach
                    kolejnosc = 2
                    wybor = 100
                    dostepne_ruchy = []
                # add option to castle
                elif wybor != 100 and wybrany_element == 'king':
                    for q in range(len(ruchy_roszada)):
                        if klikniecie_wspolrzedna == ruchy_roszada[q][0]:
                            biale_lokalizacja[wybor] = klikniecie_wspolrzedna
                            biale_ruch[wybor] = True
                            if klikniecie_wspolrzedna == (1, 0):
                                wieza_wspolrzedne = (0, 0)
                            else:
                                wieza_wspolrzedne = (7, 0)
                            wieza_index = biale_lokalizacja.index(wieza_wspolrzedne)
                            biale_lokalizacja[wieza_index] = ruchy_roszada[q][1]
                            okresl_nastepne_ruchy() # biale_opcje, czarne_opcje, czy szach
                            kolejnosc = 2
                            wybor = 100
                            dostepne_ruchy = []
            if kolejnosc > 1:
                if czarne_szach:
                    czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
                elif biale_szach:
                    biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
                if klikniecie_wspolrzedna == (8, 8) or klikniecie_wspolrzedna == (9, 8):
                    zwyciezca = 'white'
                if klikniecie_wspolrzedna in czarne_lokalizacja:
                    wybor = czarne_lokalizacja.index(klikniecie_wspolrzedna)
                    # check what piece is selected, so you can only draw castling moves if king is selected
                    wybrany_element = czarne_figury[wybor]
                    if kolejnosc == 2:
                        kolejnosc = 3
                if klikniecie_wspolrzedna in dostepne_ruchy and wybor != 100:
                    czarne_w_przelocie = sprawdz_bicie_w_przelocie(czarne_lokalizacja[wybor], klikniecie_wspolrzedna)
                    czarne_lokalizacja[wybor] = klikniecie_wspolrzedna
                    czarne_ruch[wybor] = True
                    if klikniecie_wspolrzedna in biale_lokalizacja:
                        biale_figura = biale_lokalizacja.index(klikniecie_wspolrzedna)
                        czarne_zbite_figury.append(biale_figury[biale_figura])
                        biale_figury.pop(biale_figura)
                        biale_lokalizacja.pop(biale_figura)
                        biale_ruch.pop(biale_figura)
                    if klikniecie_wspolrzedna == biale_w_przelocie:
                        biale_figura = biale_lokalizacja.index((biale_w_przelocie[0], biale_w_przelocie[1] + 1))
                        czarne_zbite_figury.append(biale_figury[biale_figura])
                        biale_figury.pop(biale_figura)
                        biale_lokalizacja.pop(biale_figura)
                        biale_ruch.pop(biale_figura)
                    okresl_nastepne_ruchy() # biale_opcje, czarne_opcje, czy szach
                    kolejnosc = 0
                    wybor = 100
                    dostepne_ruchy = []
                # add option to castle
                elif wybor != 100 and wybrany_element == 'king':
                    for q in range(len(ruchy_roszada)):
                        if klikniecie_wspolrzedna == ruchy_roszada[q][0]:
                            czarne_lokalizacja[wybor] = klikniecie_wspolrzedna
                            czarne_ruch[wybor] = True
                            if klikniecie_wspolrzedna == (1, 7):
                                wieza_wspolrzedne = (0, 7)
                            else:
                                wieza_wspolrzedne = (7, 7)
                            wieza_index = czarne_lokalizacja.index(wieza_wspolrzedne)
                            czarne_lokalizacja[wieza_index] = ruchy_roszada[q][1]
                            okresl_nastepne_ruchy() # biale_opcje, czarne_opcje, czy szach
                            kolejnosc = 0
                            wybor = 100
                            dostepne_ruchy = []
        if event.type == pygame.KEYDOWN and koniec_gry:
            if event.key == pygame.K_RETURN:
                koniec_gry = False
                szach = False
                biale_szach = False
                czarne_szach = False
                zwyciezca = ''
                biale_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                biale_lokalizacja = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                     (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                biale_ruch = [False, False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False, False]
                czarne_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                czarne_lokalizacja = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                      (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                czarne_ruch = [False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False]
                biale_zbite_figury = []
                czarne_zbite_figury = []
                kolejnosc = 0
                wybor = 100
                dostepne_ruchy = []
                czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
                biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
    if zwyciezca != '':
        koniec_gry = True
        pokaz_koniec_gry()

    pygame.display.flip()
pygame.quit()