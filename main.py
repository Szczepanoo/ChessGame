# two player chess in python with Pygame!
# part one, set up variables images and game loop

import pygame

pygame.init()
SZEROKOSC = 1000
WYSOKOSC = 900
ekran = pygame.display.set_mode([SZEROKOSC, WYSOKOSC])
pygame.display.set_caption('Two-Player Pygame Chess!')
czcionka = pygame.czcionka.Font('freesansbold.ttf', 20)
srednia_czcionka = pygame.czcionka.Font('freesansbold.ttf', 40)
duza_czcionka = pygame.czcionka.Font('freesansbold.ttf', 50)
zegar = pygame.time.Clock()
fps = 60
# game variables and images
biale_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
biale_lokalizacja = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                     (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
czarne_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
czarne_lokalizacja = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                      (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
biale_zbite_figury = []
czarne_zbite_figury = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
kolejnosc = 0
wybor = 100
dostepne_ruchy = []
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
czarny_hetman = pygame.image.load('assets/images/black queen.png')
czarny_hetman = pygame.transform.scale(czarny_hetman, (80, 80))
czarny_hetman_maly = pygame.transform.scale(czarny_hetman, (45, 45))
czarny_krol = pygame.image.load('assets/images/black king.png')
czarny_krol = pygame.transform.scale(czarny_krol, (80, 80))
czarny_krol_maly = pygame.transform.scale(czarny_krol, (45, 45))
czarna_wieza = pygame.image.load('assets/images/black rook.png')
czarna_wieza = pygame.transform.scale(czarna_wieza, (80, 80))
czarna_wieza_mala = pygame.transform.scale(czarna_wieza, (45, 45))
czarny_goniec = pygame.image.load('assets/images/black bishop.png')
czarny_goniec = pygame.transform.scale(czarny_goniec, (80, 80))
czarny_goniec_maly = pygame.transform.scale(czarny_goniec, (45, 45))
czarny_skoczek = pygame.image.load('assets/images/black knight.png')
czarny_skoczek = pygame.transform.scale(czarny_skoczek, (80, 80))
czarny_skoczek_maly = pygame.transform.scale(czarny_skoczek, (45, 45))
czarny_pionek = pygame.image.load('assets/images/black pawn.png')
czarny_pionek = pygame.transform.scale(czarny_pionek, (65, 65))
czarny_pionek_maly = pygame.transform.scale(czarny_pionek, (45, 45))

bialy_hetman = pygame.image.load('assets/images/white queen.png')
bialy_hetman = pygame.transform.scale(bialy_hetman, (80, 80))
bialy_hetman_maly = pygame.transform.scale(bialy_hetman, (45, 45))
bialy_krol = pygame.image.load('assets/images/white king.png')
bialy_krol = pygame.transform.scale(bialy_krol, (80, 80))
bialy_krol_maly = pygame.transform.scale(bialy_krol, (45, 45))
biala_wieza = pygame.image.load('assets/images/white rook.png')
biala_wieza = pygame.transform.scale(biala_wieza, (80, 80))
biala_wieza_mala = pygame.transform.scale(biala_wieza, (45, 45))
bialy_goniec = pygame.image.load('assets/images/white bishop.png')
bialy_goniec = pygame.transform.scale(bialy_goniec, (80, 80))
bialy_goniec_maly = pygame.transform.scale(bialy_goniec, (45, 45))
bialy_skoczek = pygame.image.load('assets/images/white knight.png')
bialy_skoczek = pygame.transform.scale(bialy_skoczek, (80, 80))
bialy_skoczek_maly = pygame.transform.scale(bialy_skoczek, (45, 45))
bialy_pionek = pygame.image.load('assets/images/white pawn.png')
bialy_pionek = pygame.transform.scale(bialy_pionek, (65, 65))
bialy_pionek_maly = pygame.transform.scale(bialy_pionek, (45, 45))
biale_obrazy = [bialy_pionek, bialy_hetman, bialy_krol, bialy_skoczek, biala_wieza, bialy_goniec]
biale_male_obrazy = [bialy_pionek_maly, bialy_hetman_maly, bialy_krol_maly, bialy_skoczek_maly,
                     biala_wieza_mala, bialy_goniec_maly]
czarne_obrazy = [czarny_pionek, czarny_hetman, czarny_krol, czarny_skoczek, czarna_wieza, czarny_goniec]
czarne_male_obrazy = [czarny_pionek_maly, czarny_hetman_maly, czarny_krol_maly, czarny_skoczek_maly,
                      czarna_wieza_mala, czarny_goniec_maly]
lista_figur = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter
licznik = 0
zwyciezca = ''
koniec_gry = False

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
        status_tekst = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        ekran.blit(duza_czcionka.render(status_tekst[kolejnosc], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(ekran, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(ekran, 'black', (100 * i, 0), (100 * i, 800), 2)
        ekran.blit(srednia_czcionka.render('FORFEIT', True, 'black'), (810, 830))


# draw pieces onto board
def generuj_figury():
    for i in range(len(biale_figury)):
        index = lista_figur.index(biale_figury[i])
        if biale_figury[i] == 'pawn':
            ekran.blit(bialy_pionek, (biale_lokalizacja[i][0] * 100 + 22, biale_lokalizacja[i][1] * 100 + 30))
        else:
            ekran.blit(biale_obrazy[index], (biale_lokalizacja[i][0] * 100 + 10, biale_lokalizacja[i][1] * 100 + 10))
        if kolejnosc < 2:
            if wybor == i:
                pygame.draw.rect(ekran, 'red', [biale_lokalizacja[i][0] * 100 + 1, biale_lokalizacja[i][1] * 100 + 1,
                                                100, 100], 2)

    for i in range(len(czarne_figury)):
        index = lista_figur.index(czarne_figury[i])
        if czarne_figury[i] == 'pawn':
            ekran.blit(czarny_pionek, (czarne_lokalizacja[i][0] * 100 + 22, czarne_lokalizacja[i][1] * 100 + 30))
        else:
            ekran.blit(czarne_obrazy[index], (czarne_lokalizacja[i][0] * 100 + 10, czarne_lokalizacja[i][1] * 100 + 10))
        if kolejnosc >= 2:
            if wybor == i:
                pygame.draw.rect(ekran, 'blue', [czarne_lokalizacja[i][0] * 100 + 1, czarne_lokalizacja[i][1] * 100 + 1,
                                                 100, 100], 2)


# function to check all pieces valid options on board
def sprawdz_mozliwe_opcje(figury, lokalizacje, tura):
    lista_ruchow = []
    lista_wszystkich_ruchow = []
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
            lista_ruchow = ruchy_krol(lokalizacja, tura)
        lista_wszystkich_ruchow.append(lista_ruchow)
    return lista_wszystkich_ruchow


# check king valid moves
def ruchy_krol(pozycja, kolor):
    lista_ruchow = []
    if kolor == 'white':
        lista_wrogow = czarne_lokalizacja
        lista_przyjaciol = biale_lokalizacja
    else:
        lista_przyjaciol = czarne_lokalizacja
        lista_wrogow = biale_lokalizacja
    # 8 squares to check for kings, they can go one square any direction
    cele = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        cel = (pozycja[0] + cele[i][0], pozycja[1] + cele[i][1])
        if cel not in lista_przyjaciol and 0 <= cel[0] <= 7 and 0 <= cel[1] <= 7:
            lista_ruchow.append(cel)
    return lista_ruchow


# check queen valid moves
def ruchy_hetman(pozycja, kolor):
    lista_ruchow = ruchy_goniec(pozycja, kolor)
    druga_lista = ruchy_wieza(pozycja, kolor)
    for i in range(len(druga_lista)):
        lista_ruchow.append(druga_lista[i])
    return lista_ruchow


# check bishop moves
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


# check rook moves
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


# check valid pawn moves
def ruchy_pionek(pozycja, kolor):
    lista_ruchow = []
    if kolor == 'white':
        if (pozycja[0], pozycja[1] + 1) not in biale_lokalizacja and \
                (pozycja[0], pozycja[1] + 1) not in czarne_lokalizacja and pozycja[1] < 7:
            lista_ruchow.append((pozycja[0], pozycja[1] + 1))
        if (pozycja[0], pozycja[1] + 2) not in biale_lokalizacja and \
                (pozycja[0], pozycja[1] + 2) not in czarne_lokalizacja and pozycja[1] == 1:
            lista_ruchow.append((pozycja[0], pozycja[1] + 2))
        if (pozycja[0] + 1, pozycja[1] + 1) in czarne_lokalizacja:
            lista_ruchow.append((pozycja[0] + 1, pozycja[1] + 1))
        if (pozycja[0] - 1, pozycja[1] + 1) in czarne_lokalizacja:
            lista_ruchow.append((pozycja[0] - 1, pozycja[1] + 1))
    else:
        if (pozycja[0], pozycja[1] - 1) not in biale_lokalizacja and \
                (pozycja[0], pozycja[1] - 1) not in czarne_lokalizacja and pozycja[1] > 0:
            lista_ruchow.append((pozycja[0], pozycja[1] - 1))
        if (pozycja[0], pozycja[1] - 2) not in biale_lokalizacja and \
                (pozycja[0], pozycja[1] - 2) not in czarne_lokalizacja and pozycja[1] == 6:
            lista_ruchow.append((pozycja[0], pozycja[1] - 2))
        if (pozycja[0] + 1, pozycja[1] - 1) in biale_lokalizacja:
            lista_ruchow.append((pozycja[0] + 1, pozycja[1] - 1))
        if (pozycja[0] - 1, pozycja[1] - 1) in biale_lokalizacja:
            lista_ruchow.append((pozycja[0] - 1, pozycja[1] - 1))
    return lista_ruchow


# check valid knight moves
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


# check for valid moves for just selected piece
def sprawdz_mozliwe_ruchy():
    if kolejnosc < 2:
        lista_opcji = biale_opcje
    else:
        lista_opcji = czarne_opcje
    mozliwe_opcje = lista_opcji[wybor]
    return mozliwe_opcje


# draw valid moves on screen
def pokaz_mozliwe_ruchy(ruchy):
    if kolejnosc < 2:
        kolor = 'red'
    else:
        kolor = 'blue'
    for i in range(len(ruchy)):
        pygame.draw.circle(ekran, kolor, (ruchy[i][0] * 100 + 50, ruchy[i][1] * 100 + 50), 5)


# draw captured pieces on side of screen
def pokaz_zbite_figury():
    for i in range(len(biale_zbite_figury)):
        zbite_figury = biale_zbite_figury[i]
        index = lista_figur.index(zbite_figury)
        ekran.blit(czarne_male_obrazy[index], (825, 5 + 50 * i))
    for i in range(len(czarne_zbite_figury)):
        zbite_figury = czarne_zbite_figury[i]
        index = lista_figur.index(zbite_figury)
        ekran.blit(biale_male_obrazy[index], (925, 5 + 50 * i))


# draw a flashing square around king if in check
def pokaz_czy_szach():
    if kolejnosc < 2:
        if 'king' in biale_figury:
            king_index = biale_figury.index('king')
            king_location = biale_lokalizacja[king_index]
            for i in range(len(czarne_opcje)):
                if king_location in czarne_opcje[i]:
                    if licznik < 15:
                        pygame.draw.rect(ekran, 'dark red', [biale_lokalizacja[king_index][0] * 100 + 1,
                                                             biale_lokalizacja[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in czarne_figury:
            king_index = czarne_figury.index('king')
            king_location = czarne_lokalizacja[king_index]
            for i in range(len(biale_opcje)):
                if king_location in biale_opcje[i]:
                    if licznik < 15:
                        pygame.draw.rect(ekran, 'dark blue', [czarne_lokalizacja[king_index][0] * 100 + 1,
                                                              czarne_lokalizacja[king_index][1] * 100 + 1, 100, 100], 5)


def pokaz_koniec_gry():
    pygame.draw.rect(ekran, 'black', [200, 200, 400, 70])
    ekran.blit(czcionka.render(f'{zwyciezca} won the game!', True, 'white'), (210, 210))
    ekran.blit(czcionka.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


# main game loop
czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
uruchom = True
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
    if wybor != 100:
        dostepne_ruchy = sprawdz_mozliwe_ruchy()
        pokaz_mozliwe_ruchy(dostepne_ruchy)
    # event handling
    for zdarzenie in pygame.zdarzenie.get():
        if zdarzenie.type == pygame.QUIT:
            uruchom = False
        if zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1 and not koniec_gry:
            x_wspolrzedna = zdarzenie.pos[0] // 100
            y_wspolrzedna = zdarzenie.pos[1] // 100
            klikniecie_wspolrzedna = (x_wspolrzedna, y_wspolrzedna)
            if kolejnosc <= 1:
                if klikniecie_wspolrzedna == (8, 8) or klikniecie_wspolrzedna == (9, 8):
                    zwyciezca = 'black'
                if klikniecie_wspolrzedna in biale_lokalizacja:
                    wybor = biale_lokalizacja.index(klikniecie_wspolrzedna)
                    if kolejnosc == 0:
                        kolejnosc = 1
                if klikniecie_wspolrzedna in dostepne_ruchy and wybor != 100:
                    biale_lokalizacja[wybor] = klikniecie_wspolrzedna
                    if klikniecie_wspolrzedna in czarne_lokalizacja:
                        czarne_figura = czarne_lokalizacja.index(klikniecie_wspolrzedna)
                        biale_zbite_figury.append(czarne_figury[czarne_figura])
                        if czarne_figury[czarne_figura] == 'king':
                            zwyciezca = 'white'
                        czarne_figury.pop(czarne_figura)
                        czarne_lokalizacja.pop(czarne_figura)
                    czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
                    biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
                    kolejnosc = 2
                    wybor = 100
                    dostepne_ruchy = []
            if kolejnosc > 1:
                if klikniecie_wspolrzedna == (8, 8) or klikniecie_wspolrzedna == (9, 8):
                    zwyciezca = 'white'
                if klikniecie_wspolrzedna in czarne_lokalizacja:
                    wybor = czarne_lokalizacja.index(klikniecie_wspolrzedna)
                    if kolejnosc == 2:
                        kolejnosc = 3
                if klikniecie_wspolrzedna in dostepne_ruchy and wybor != 100:
                    czarne_lokalizacja[wybor] = klikniecie_wspolrzedna
                    if klikniecie_wspolrzedna in biale_lokalizacja:
                        biale_figura = biale_lokalizacja.index(klikniecie_wspolrzedna)
                        czarne_zbite_figury.append(biale_figury[biale_figura])
                        if biale_figury[biale_figura] == 'king':
                            zwyciezca = 'black'
                        biale_figury.pop(biale_figura)
                        biale_lokalizacja.pop(biale_figura)
                    czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
                    biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
                    kolejnosc = 0
                    wybor = 100
                    dostepne_ruchy = []
        if zdarzenie.type == pygame.KEYDOWN and koniec_gry:
            if zdarzenie.key == pygame.K_RETURN:
                koniec_gry = False
                zwyciezca = ''
                biale_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                biale_lokalizacja = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                     (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                czarne_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                czarne_lokalizacja = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                      (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
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