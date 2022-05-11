import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.06) #volume do som
musica_de_fundo = pygame.mixer.music.load('BoxCat-Games-B-3.wav') #musica de fundo do game
pygame.mixer.music.play(-1)#pra se repetir ao acabar a musica

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

velocidade = 10
x_controle = velocidade
y_controle = 0

tela = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Snake Game By Yuri Alves')
relogio = pygame.time.Clock()


x_cobra = (1280/2) - (50/2)
y_cobra  = 720/2

x_maca=randint(100,1000)
y_maca=randint(20,500)
game_over = pygame.mixer.Sound('game_over.wav')
fonte = pygame.font.SysFont('centurygothic',40,True,True)
pontos=0
lista_cobra=[]
comprimento_inicial = 5
morreu=False





def reiniciar_jogo():
    global pontos
    global comprimento_inicial
    global morreu
    global x_cobra
    global y_cobra
    global lista_cobra
    global  lista_cabeca
    global x_maca
    global y_maca
    global musica_de_fundo
    pontos = 0
    comprimento_inicial=5
    morreu= False
    x_cobra = (1280 / 2) - (50 / 2)
    y_cobra = 720 / 2
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(100, 1000)
    y_maca = randint(20, 500)
    pygame.mixer.music.set_volume(0.06)  # volume do som
    musica_de_fundo = pygame.mixer.music.load('BoxCat-Games-B-3.wav')  # musica de fundo do game
    pygame.mixer.music.play(-1)  # pra se repetir ao acabar a musica






def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(xey[0],xey[1],20,20))


while True:
    relogio.tick(60) #taxa de atualização do jogo
    tela.fill((0,0,0))
    mensagem = f'Pontos:{pontos}'
    texto_formatado=fonte.render(mensagem,False,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a: #aqui é pra ir um ação de cada vez
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle=0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle=velocidade
                    y_controle=0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle=0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    '''''''''
    if pygame.key.get_pressed()[K_a]: #aqui é constante
        x_cobra-=20
    if pygame.key.get_pressed()[K_d]:
        x_cobra+=20
    if pygame.key.get_pressed()[K_w]:
        y_cobra-=20
    if pygame.key.get_pressed()[K_s]:
        y_cobra+=20
    '''''''''

    x_cobra = x_cobra +x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))# criando um quadrado
    maca = pygame.draw.rect(tela, (255, 0,0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca=randint(100,1000)
        y_maca=randint(20,500)
        pontos+=1
        barulho_colisao.play()
        comprimento_inicial+=1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca)>1: # condição para se a cobrar encostar nela mesma (morrer)
        fonte2 =  pygame.font.SysFont('centurygothic',20,True,True) # fonte para escrever o txt
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente!'
        texto_formatado2 = fonte2.render(mensagem,False,(255,255,255))
        game_over.play()
        morreu=True
        while morreu:

            tela.fill((0,0,0))
            musica_de_fundo = pygame.mixer.music.stop()


            for event in pygame.event.get():
                if event.type == QUIT:
                     pygame.quit()
                     exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:


                        reiniciar_jogo()
            tela.blit(texto_formatado2,(300,330))
            pygame.display.update()
    #Condicionais para quando a cobra sumir num canto da tela, ela aparecer no oposto
    if x_cobra > 1280:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = 1280
    if y_cobra > 720:
        x_cobra = 0
    if y_cobra <0:
        y_cobra = 720



    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)


    tela.blit(texto_formatado,(850,40))


    #pygame.draw.circle(tela,(0,255,0),(360,260),40) # criando um circulo

    #pygame.draw.line(tela,(255,255,0), (420,0), (420,600), 8) criando uma linha

    pygame.display.update()


