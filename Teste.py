import pygame
import random

pygame.init()
altura = 300
largura = 800
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Star Wars do Marcão")
bg = pygame.image.load("assets/fundo.png")
bg_destroy = pygame.image.load("assets/bg-destroy.jpeg")


gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

gameIcon = pygame.image.load("assets/TrupperIco.ico")
pygameDisplay.set_icon(gameIcon)

pink = (255, 125, 198)
black = (0, 0, 0)
white = (255, 255, 255)


explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
explosaoSound.set_volume(0.5)

missileSound = pygame.mixer.Sound("assets/missile.wav")
missileSound.set_volume(0.1)


def dead(pontos):
    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                         " pontos!", True, black)
    gameDisplay.blit(texto, (50, 100))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    textoContinue = fonteContinue.render("press enter to restart", True, white)
    gameDisplay.blit(textoContinue, (50, 200))

    pygameDisplay.update()


def jogo():
    jogando = True
    movimentoX = 0
    movimentoY = random.randrange(0, altura)
    velocidade = 1
    direcao = True
    posicaoXNave = 450
    posicaoYNave = 100
    movimentoXNave = 0
    movimentoYNave = 0
    pontos = 0
    missile = pygame.image.load("assets/missile.png")
    missile = pygame.transform.flip(missile, True, False)
    #missile = pygame.transform.scale(missile, (300, 30))
    nave = pygame.image.load("assets/nave.png")
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(missileSound)
    larguraNave = 217
    alturaNave = 150
    larguraMissel = 150
    alturaMissel = 52
    limiar = 28
    velocidadeNave = 10

    while True:
        # aqui será feito a leitura dos comandos
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoXNave = -velocidadeNave
                elif event.key == pygame.K_RIGHT:
                    movimentoXNave = velocidadeNave
                elif event.key == pygame.K_UP:
                    movimentoYNave = -velocidadeNave
                elif event.key == pygame.K_DOWN:
                    movimentoYNave = velocidadeNave
                elif event.key == pygame.K_RETURN:
                    jogo()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXNave = 0
                    movimentoYNave = 0

        if jogando == True:
            # aqui vai o jogo

            # controlando limites da nave
            posicaoXNave = posicaoXNave + movimentoXNave
            if posicaoXNave < 0:
                posicaoXNave = 0
            elif posicaoXNave > largura - larguraNave:
                posicaoXNave = largura - larguraNave

            posicaoYNave = posicaoYNave + movimentoYNave
            if posicaoYNave < 0:
                posicaoYNave = 0
            elif posicaoYNave > altura - alturaNave:
                posicaoYNave = altura - alturaNave

            gameDisplay.fill(pink)
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(nave, (posicaoXNave, posicaoYNave))
            gameDisplay.blit(missile, (movimentoX, movimentoY))
            # pygame.draw.circle(
            #    gameDisplay, black, [movimentoX, movimentoY], 20, 0 )

            if direcao == True:
                if movimentoX <= 800 - 150:
                    movimentoX = movimentoX + velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    direcao = False
                    pontos = pontos + 1
                    movimentoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    missile = pygame.transform.flip(missile, True, False)
            else:
                if movimentoX >= 0:
                    movimentoX = movimentoX - velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    direcao = True
                    pontos += 1
                    movimentoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    missile = pygame.transform.flip(missile, True, False)
            # atualização de tela
            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 280))

            # controle de colisão
            '''
            naveRect = nave.get_rect()
            naveRect.x = posicaoXNave
            naveRect.y = posicaoYNave

            missileRect = missile.get_rect()
            missileRect.x = movimentoX
            missileRect.y = movimentoY

            if naveRect.colliderect(missileRect) == True:
                jogando = False
                dead(pontos)
            else:
                print("analisando....")
            '''
            pixelYMissel = list(range(movimentoY, movimentoY+alturaMissel + 1))
            pixelXMissel = list(
                range(movimentoX, movimentoX+larguraMissel + 1))

            pixelYNave = list(
                range(posicaoYNave, posicaoYNave + alturaNave + 1))
            pixelXNave = list(
                range(posicaoXNave, posicaoXNave + larguraNave + 1))

            colisaoY = list(set(pixelYMissel) & set(pixelYNave))
            colisaoX = list(set(pixelXMissel) & set(pixelXNave))
            if len(colisaoY) > limiar:
                if len(colisaoX) > limiar:
                    jogando = False
                    dead(pontos)

        pygameDisplay.update()
        clock.tick(60)


jogo()
