import pygame
pygame.init()

SZEROKOSC = 1000
WYSOKOSC = 900
ekran = pygame.display.set_mode([SZEROKOSC, WYSOKOSC])
pygame.display.set_caption('Two-Player Pygame Chess!')
czcionka = pygame.font.Font('freesansbold.ttf', 20)
srednia_czcionka = pygame.font.Font('freesansbold.ttf', 40)
duza_czcionka = pygame.font.Font('freesansbold.ttf', 50)
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
czarne_hetman = pygame.image.load('assets/images/black queen.png')
czarne_hetman = pygame.transform.scale(czarne_hetman, (80, 80))
czarne_hetman_maly = pygame.transform.scale(czarne_hetman, (45, 45))
czarne_krol = pygame.image.load('assets/images/black king.png')
czarne_krol = pygame.transform.scale(czarne_krol, (80, 80))
czarne_krol_maly = pygame.transform.scale(czarne_krol, (45, 45))
czarne_wieza = pygame.image.load('assets/images/black rook.png')
czarne_wieza = pygame.transform.scale(czarne_wieza, (80, 80))
czarne_wieza_mala = pygame.transform.scale(czarne_wieza, (45, 45))
czarne_goniec = pygame.image.load('assets/images/black bishop.png')
czarne_goniec = pygame.transform.scale(czarne_goniec, (80, 80))
czarne_goniec_maly = pygame.transform.scale(czarne_goniec, (45, 45))
czarne_skoczek = pygame.image.load('assets/images/black knight.png')
czarne_skoczek = pygame.transform.scale(czarne_skoczek, (80, 80))
czarne_skoczek_maly = pygame.transform.scale(czarne_skoczek, (45, 45))
czarne_pionek = pygame.image.load('assets/images/black pawn.png')
czarne_pionek = pygame.transform.scale(czarne_pionek, (65, 65))
czarne_pionek_maly = pygame.transform.scale(czarne_pionek, (45, 45))
biale_hetman = pygame.image.load('assets/images/white queen.png')
biale_hetman = pygame.transform.scale(biale_hetman, (80, 80))
biale_hetman_maly = pygame.transform.scale(biale_hetman, (45, 45))
biale_krol = pygame.image.load('assets/images/white king.png')
biale_krol = pygame.transform.scale(biale_krol, (80, 80))
biale_krol_maly = pygame.transform.scale(biale_krol, (45, 45))
biale_wieza = pygame.image.load('assets/images/white rook.png')
biale_wieza = pygame.transform.scale(biale_wieza, (80, 80))
biale_wieza_mala = pygame.transform.scale(biale_wieza, (45, 45))
biale_goniec = pygame.image.load('assets/images/white bishop.png')
biale_goniec = pygame.transform.scale(biale_goniec, (80, 80))
biale_goniec_maly = pygame.transform.scale(biale_goniec, (45, 45))
biale_skoczek = pygame.image.load('assets/images/white knight.png')
biale_skoczek = pygame.transform.scale(biale_skoczek, (80, 80))
biale_skoczek_maly = pygame.transform.scale(biale_skoczek, (45, 45))
biale_pionek = pygame.image.load('assets/images/white pawn.png')
biale_pionek = pygame.transform.scale(biale_pionek, (65, 65))
biale_pionek_maly = pygame.transform.scale(biale_pionek, (45, 45))
biale_obraz = [biale_pionek, biale_hetman, biale_krol, biale_skoczek, biale_wieza, biale_goniec]
biale_promocja = ['bishop', 'knight', 'rook', 'queen']
biale_ruch = [False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False]
biale_male_obraz = [biale_pionek_maly, biale_hetman_maly, biale_krol_maly, biale_skoczek_maly,
                     biale_wieza_mala, biale_goniec_maly]
czarne_obraz = [czarne_pionek, czarne_hetman, czarne_krol, czarne_skoczek, czarne_wieza, czarne_goniec]
czarne_male_obraz = [czarne_pionek_maly, czarne_hetman_maly, czarne_krol_maly, czarne_skoczek_maly,
                      czarne_wieza_mala, czarne_goniec_maly]
czarne_promocja = ['bishop', 'knight', 'rook', 'queen']
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
biale_szach = False
czarne_szach = False
ruchy_roszada = []