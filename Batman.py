import pygame

pygame.init()

altura = 468
largura = 950
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Dark Knight do Pedrinho")
bg = pygame.image.load("./assets/fundo.jpg")

gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

gameIcon = pygame.image.load("./assets/bman.png")
pygameDisplay.set_icon(gameIcon)

jogando = True

while jogando:
    # aqui será feito a leitura dos comandos
    for event in gameEvents.get():
        gameDisplay.blit(bg, (0, 0))
        pygameDisplay.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameDisplay.blit(bg, (0, 0))
