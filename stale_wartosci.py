import pygame
pygame.init()

SZEROKOSC = 1000
WYSOKOSC = 900
ekran = pygame.display.set_mode([SZEROKOSC, WYSOKOSC])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
srednia_czcionka = pygame.font.Font('freesansbold.ttf', 40)
duza_czcionka = pygame.font.Font('freesansbold.ttf', 50)
zegar = pygame.time.Clock()
fps = 60
# game variables and images
biale_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
pozycje_bialych = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
czarne_figury = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
pozycje_czarnych = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
zdobyte_figury_biale = []
zdobyte_figury_czarne = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
kolejnosc = 0
wybor = 100
poprawne_ruchy = []
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
black_pawn_small = pygame.transform.scale(czarny_pionek, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
white_promotions = ['bishop', 'knight', 'rook', 'queen']
white_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [czarny_pionek, czarny_hetman, czarny_krol, czarny_skoczek, czarna_wieza, czarny_goniec]
small_black_images = [black_pawn_small, czarny_hetman_maly, czarny_krol_maly, czarny_skoczek_maly,
                      czarna_wieza_mala, czarny_goniec_maly]
black_promotions = ['bishop', 'knight', 'rook', 'queen']
black_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
check = False
castling_moves = []