import pygame
from constants import *

pygame.init()

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


# function to check all pieces valid options on board
def sprawdz_mozliwe_opcje(figury, lokalizacje, tura):
    global ruchy_roszada
    lista_ruchow = []
    lista_wszystkich_ruchow = []
    ruchy_roszada = []

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
            lista_ruchow, ruchy_roszada = ruchy_krol(lokalizacja, tura)
        lista_wszystkich_ruchow.append(lista_ruchow)
    return lista_wszystkich_ruchow



# check king valid moves
def ruchy_krol(pozycja, kolor):
    lista_ruchow = []
    ruchy_roszady = sprawdz_roszade()
    if kolejnosc < 2:
        if 'king' in biale_figury:
            krol_index = biale_figury.index('king')
            krol_lokalizacja = biale_lokalizacja[krol_index]
    else:
        if 'king' in czarne_figury:
            krol_index = czarne_figury.index('king')
            krol_lokalizacja = czarne_lokalizacja[krol_index]
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
        krol_w_zasiegu = False
        if cel not in lista_przyjaciol and 0 <= cel[0] <= 7 and 0 <= cel[1] <= 7:
            for i in range(8):
                cel2 = (cel[0] + cele[i][0], cel[1] + cele[i][1])
                if cel2 == krol_lokalizacja and 0 <= cel2[0] <= 7 and 0 <= cel2[1] <= 7:
                    krol_w_zasiegu = True
                    break
            if not krol_w_zasiegu:
                lista_ruchow.append(cel)

    return lista_ruchow, ruchy_roszady


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
        ekran.blit(czarne_male_obraz[index], (825, 5 + 50 * i))
    for i in range(len(czarne_zbite_figury)):
        zbite_figury = czarne_zbite_figury[i]
        index = lista_figur.index(zbite_figury)
        ekran.blit(biale_male_obraz[index], (925, 5 + 50 * i))







#check if any pieces are in check then return szach
def sprawdz_szach():
    global szach
    szach = False
    if kolejnosc < 2:
        if 'king' in biale_figury:
            krol_index = biale_figury.index('king')
            krol_lokalizacja = biale_lokalizacja[krol_index]
            for i in range(len(czarne_opcje)):
                if krol_lokalizacja in czarne_opcje[i]:
                    szach = True
                    biale_ruch[krol_index] = True
    else:
        if 'king' in czarne_figury:
            krol_index = czarne_figury.index('king')
            krol_lokalizacja = czarne_lokalizacja[krol_index]
            for i in range(len(biale_opcje)):
                if krol_lokalizacja in biale_opcje[i]:
                    szach = True
                    czarne_ruch[krol_index] = True

#draw a flashing square around king if szach = True
def pokaz_czy_szach():
    if szach:
        if licznik < 15:
            if kolejnosc < 2:
                king_index = biale_figury.index('king')
                king_location = biale_lokalizacja[king_index]
                pygame.draw.rect(ekran, 'dark red', [king_location[0] * 100 + 1, king_location[1] * 100 + 1, 100, 100], 5)
            else:
                king_index = czarne_figury.index('king')
                king_location = czarne_lokalizacja[king_index]
                pygame.draw.rect(ekran, 'dark blue', [king_location[0] * 100 + 1, king_location[1] * 100 + 1, 100, 100], 5)










def pokaz_koniec_gry():
    if zwyciezca == 'black':
        kolor = 'Czarne'
    else:
        kolor = 'Białe'
    pygame.draw.rect(ekran, 'black', [200, 200, 400, 70])
    ekran.blit(czcionka.render(f'{kolor} wygrywają! ', True, 'white'), (210, 210))
    ekran.blit(czcionka.render(f'Naciśnij ENTER aby zacząć od nowa!', True, 'white'), (210, 240))

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

def sprawdz_roszade():
    # king must not currently be in check, neither the rook nor king has moved previously, nothing between
    # and the king does not pass through or finish on an attacked piece
    ruchy_roszady = []  # store each valid castle move as [((king_coords), (castle_coords))]
    wieza_indexy = []
    wieza_lokalizacje = []
    krol_index = 0
    krol_pozycja = (0, 0)
    if kolejnosc > 1:
        for i in range(len(biale_figury)):
            if biale_figury[i] == 'rook':
                wieza_indexy.append(biale_ruch[i])
                wieza_lokalizacje.append(biale_lokalizacja[i])
            if biale_figury[i] == 'king':
                krol_index = i
                krol_pozycja = biale_lokalizacja[i]
        if not biale_ruch[krol_index] and False in wieza_indexy and not szach:
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
        if not czarne_ruch[krol_index] and False in wieza_indexy and not szach:
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
czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
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
    sprawdz_szach()
    pokaz_czy_szach()
    if not koniec_gry:
        biale_promuj, czarne_promuj, index_promocja = sprawdz_promocje()
        if biale_promuj or czarne_promuj:
            promocja()
            sprawdz_wybor_promocji()
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
                        if czarne_figury[czarne_figura] == 'king':
                            zwyciezca = 'white'
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
                    czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
                    biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
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
                    # check what piece is selected, so you can only draw castling ruchy if king is selected
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
                        if biale_figury[biale_figura] == 'king':
                            zwyciezca = 'black'
                        biale_figury.pop(biale_figura)
                        biale_lokalizacja.pop(biale_figura)
                        biale_ruch.pop(biale_figura)
                    if klikniecie_wspolrzedna == biale_w_przelocie:
                        biale_figura = biale_lokalizacja.index((biale_w_przelocie[0], biale_w_przelocie[1] + 1))
                        czarne_zbite_figury.append(biale_figury[biale_figura])
                        biale_figury.pop(biale_figura)
                        biale_lokalizacja.pop(biale_figura)
                        biale_ruch.pop(biale_figura)
                    czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
                    biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
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
                            czarne_opcje = sprawdz_mozliwe_opcje(czarne_figury, czarne_lokalizacja, 'black')
                            biale_opcje = sprawdz_mozliwe_opcje(biale_figury, biale_lokalizacja, 'white')
                            kolejnosc = 0
                            wybor = 100
                            dostepne_ruchy = []
        if event.type == pygame.KEYDOWN and koniec_gry:
            if event.key == pygame.K_RETURN:
                koniec_gry = False
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