import pygame
from limparTela import limparTela

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

gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

gameIcon = pygame.image.load("./assets/bman.png")
pygameDisplay.set_icon(gameIcon)


def jogo():
    jogando = True

    while jogando:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameDisplay.blit(bg, (0, 0))
                    pygameDisplay.update()


jogo()
