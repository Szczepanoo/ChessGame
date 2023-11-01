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
biale_promocje = ['bishop', 'knight', 'rook', 'queen']
biale_ruch = [False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False]
biale_male_obrazy = [bialy_pionek_maly, bialy_hetman_maly, bialy_krol_maly, bialy_skoczek_maly,
                     biala_wieza_mala, bialy_goniec_maly]
czarne_obraz = [czarny_pionek, czarny_hetman, czarny_krol, czarny_skoczek, czarna_wieza, czarny_goniec]
czarne_male_obrazy = [czarny_pionek_maly, czarny_hetman_maly, czarny_krol_maly, czarny_skoczek_maly,
                      czarna_wieza_mala, czarny_goniec_maly]
czarne_promocje = ['bishop', 'knight', 'rook', 'queen']
czarne_ruch = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
lista_figur = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter
licznik = 0
zwyciezca = ''
koniec_gry = False
biale_w_przelocie = (100, 100)
czarne_w_przelocie = (100, 100)
biale_promuj = False
czarne_promuj = False
index_promocja = 100
szach = False
ruchy_roszada = []