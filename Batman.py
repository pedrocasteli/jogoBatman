import pygame
from limparTela import limparTela
import random

while True:
    limparTela()
    try:
        nome = input("Digite seu nome: ")
        if (not nome) or (len(nome.replace(" ", "")) == 0):
            raise ValueError("=> Nome em branco!")
        email = input("Digite seu e-mail: ")
        if (not email) or (len(email.replace(" ", "")) == 0):
            raise ValueError("=> E-mail em branco!")
        try:
            f = open("historico.txt", "a")
        except:
            limparTela()
            print("*** ERRO ***")
            print("Não foi possível abrir/criar o arquivo.", end=" ")
            input()
            quit()
        f.write("Nome: {}\nE-mail: {}\n----------\n".format(nome, email))
        f.close()
        break
    except ValueError as e:
        limparTela()
        print("*** ERRO ***")
        print(e, end=" ")
        input()


pygame.init()

altura = 468
largura = 950
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Dark Knight do Pedrinho")
bg = pygame.image.load("./assets/fundo.jpg")
bg_destroy = pygame.image.load("assets/bg_gameover.jpg")
bg_destroy = pygame.transform.scale(bg_destroy, (950, 468))

gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

gameIcon = pygame.image.load("./assets/bman.png")
pygameDisplay.set_icon(gameIcon)

black = (0, 0, 0)
white = (255, 255, 255)


def gameover(pontos):
    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    fonte = pygame.font.Font("freesansbold.ttf", 30)
    texto = fonte.render("Você perdeu com " +
                         str(pontos) + " pontos!", True, white)
    gameDisplay.blit(texto, (10, 10))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 20)
    textoContinue = fonteContinue.render(
        "Pressione Enter para recomeçar...", True, white)
    gameDisplay.blit(textoContinue, (10, 448))

    pygameDisplay.update()


def jogo():
    jogando = True
    movimentoX = 0
    movimentoY = random.randrange(0, altura)
    velocidade = 1
    direcao = True
    posicaoXBatman = 400
    posicaoYBatman = 100
    movimentoXBatman = 0
    movimentoYBatman = 0
    pontos = 0
    coringa = pygame.image.load("assets/coringa.png")
    coringa = pygame.transform.scale(coringa, (100, 160))
    coringa = pygame.transform.flip(coringa, True, False)
    batman = pygame.image.load("assets/batman.png")
    batman = pygame.transform.scale(batman, (130, 180))
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    larguraBatman = 130
    alturaBatman = 180
    larguraCoringa = 100
    alturaCoringa = 160
    limiar = 28
    velocidadeBatman = 10

    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoXBatman = -velocidadeBatman
                elif event.key == pygame.K_RIGHT:
                    movimentoXBatman = velocidadeBatman
                elif event.key == pygame.K_UP:
                    movimentoYBatman = -velocidadeBatman
                elif event.key == pygame.K_DOWN:
                    movimentoYBatman = velocidadeBatman
                elif event.key == pygame.K_RETURN:
                    jogo()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXBatman = 0
                    movimentoYBatman = 0

        if jogando == True:
            posicaoXBatman = posicaoXBatman + movimentoXBatman
            if posicaoXBatman < 0:
                posicaoXBatman = 0
            elif posicaoXBatman > largura - larguraBatman:
                posicaoXBatman = largura - larguraBatman

            posicaoYBatman = posicaoYBatman + movimentoYBatman
            if posicaoYBatman < 0:
                posicaoYBatman = 0
            elif posicaoYBatman > altura - alturaBatman:
                posicaoYBatman = altura - alturaBatman

            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(batman, (posicaoXBatman, posicaoYBatman))
            gameDisplay.blit(coringa, (movimentoX, movimentoY))

            if direcao == True:
                if movimentoX <= 950 - 100:
                    movimentoX = movimentoX + velocidade
                else:
                    direcao = False
                    pontos = pontos + 1
                    movimentoY = random.randrange(0, altura - alturaCoringa)
                    velocidade = velocidade + 1
                    coringa = pygame.transform.flip(coringa, True, False)
            else:
                if movimentoX >= 0:
                    movimentoX = movimentoX - velocidade
                else:
                    direcao = True
                    pontos += 1
                    movimentoY = random.randrange(0, altura - alturaCoringa)
                    velocidade = velocidade + 1
                    coringa = pygame.transform.flip(coringa, True, False)

            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render("Pontos: " + str(pontos), True, white)
            gameDisplay.blit(texto, (20, 428))

            pixelYCoringa = list(
                range(movimentoY, movimentoY + alturaCoringa + 1))
            pixelXCoringa = list(
                range(movimentoX, movimentoX + larguraCoringa + 1))

            pixelYBatman = list(
                range(posicaoYBatman, posicaoYBatman + alturaBatman + 1))
            pixelXBatman = list(
                range(posicaoXBatman, posicaoXBatman + larguraBatman + 1))

            colisaoY = list(set(pixelYCoringa) & set(pixelYBatman))
            colisaoX = list(set(pixelXCoringa) & set(pixelXBatman))
            if len(colisaoY) > limiar:
                if len(colisaoX) > limiar:
                    jogando = False
                    gameover(pontos)

        pygameDisplay.update()
        clock.tick(60)


jogo()
