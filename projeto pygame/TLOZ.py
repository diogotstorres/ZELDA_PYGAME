
#################### CLONE DE "THE LEGEND OF ZELDA" POR DIOGO TORRES DA SILVEIRA, TIA: 31715966 #################


import pygame
import sys
import os
import random
jogo_em_execucao = True

pygame.init()

meu_vermelho = (181, 49, 33)
minha_fonte = pygame.font.Font("fonte8.ttf", 20)
texto_nada = minha_fonte.render('', False, meu_vermelho)

historico = [(texto_nada,texto_nada),(texto_nada,texto_nada),(texto_nada,texto_nada)]
codigo_geral = 0

def gerar_codigo():
    global codigo_geral
    codigo_geral += 1
    return codigo_geral


while jogo_em_execucao:
        pygame.init()

        qtd_joysticks = pygame.joystick.get_count()
        if qtd_joysticks != 0:
                
                controle = pygame.joystick.Joystick(0)
                controle.init()
                num_botoes = controle.get_numbuttons()
                nome_controle = controle.get_name()
                print ("Joystick" + "0" + " name: " + nome_controle)
                

        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

        altura = 633
        largura = 756
        screen = pygame.display.set_mode((largura,altura))
        clock = pygame.time.Clock()
        tempo = 0
        pygame.display.set_caption("The Legend of Zelda")

        ################################################## TEXTO #########################################################

        meu_vermelho = (181, 49, 33)
        minha_fonte = pygame.font.Font("fonte8.ttf", 20)
        texto_tempo = minha_fonte.render('TEMPO: ', False, meu_vermelho)
        texto_pontos = minha_fonte.render('PONTOS: ', False, meu_vermelho)
        texto_vida = minha_fonte.render('- VIDA -', False, meu_vermelho)
        texto_game_over = minha_fonte.render('-- GAME OVER --', False, meu_vermelho)
        texto_jogar_novamente = minha_fonte.render('JOGAR NOVAMENTE ?', False, meu_vermelho)
        texto_sim = minha_fonte.render('SIM', False, meu_vermelho)
        texto_nao = minha_fonte.render('NÃO', False, meu_vermelho)
        texto_final = minha_fonte.render("CLONE DE 'THE LEGEND OF ZELDA'", False, meu_vermelho)
        texto_nome = minha_fonte.render('POR DIOGO TORRES', False, meu_vermelho)



        ################################################### SOM ##########################################################

        audio_intro = pygame.mixer.Sound("audio/intro.ogg")
        audio_jogo = pygame.mixer.Sound("audio/overworld.ogg")
        audio_espada = pygame.mixer.Sound("audio/espada.wav")
        audio_morte_mob = pygame.mixer.Sound("audio/morte_inimigo.wav")
        audio_link_dano = pygame.mixer.Sound("audio/player_dano.ogg")
        audio_link_morte = pygame.mixer.Sound("audio/player_morte.wav")
        audio_game_over = pygame.mixer.Sound("audio/game_over.ogg")
        audio_triforce = pygame.mixer.Sound("audio/triforce.ogg")
        audio_final = pygame.mixer.Sound("audio/final.ogg")



        ################################################# IMAGENS ########################################################

        imagem_abertura = pygame.image.load(os.path.join('fundos',"abertura.png"))
        imagem_instrucoes = pygame.image.load(os.path.join('fundos',"instrucoes.png"))
        imagem_dificuldade = pygame.image.load(os.path.join('fundos',"dificuldade.png"))
        imagem_pontuacao = pygame.image.load(os.path.join('fundos',"pontuacao.png"))
        imagem_jogar_novamente = pygame.image.load(os.path.join('fundos',"jogar_novamente.png"))

        imagem_triforce = pygame.transform.scale(pygame.image.load(os.path.join('tesouro',"triforce.png")), (50,50))
        imagem_triforce_menu = pygame.transform.scale(pygame.image.load(os.path.join('tesouro',"triforce.png")), (40,40))

        parede_baixo = pygame.transform.scale(pygame.image.load(os.path.join('portas',"parede_baixo.png")), (102,77))
        parede_cima = pygame.transform.scale(pygame.image.load(os.path.join('portas',"parede_cima.png")), (102,77))
        parede_direita = pygame.transform.scale(pygame.image.load(os.path.join('portas',"parede_direita.png")), (77,102))
        parede_esquerda = pygame.transform.scale(pygame.image.load(os.path.join('portas',"parede_esquerda.png")), (77,102))

        imagem_bloco = pygame.transform.scale(pygame.image.load(os.path.join('portas',"bloco.png")), (50,50))

        link_morte = pygame.transform.scale(pygame.image.load(os.path.join('link',"link_morte.png")), (50,50))
        link_vitoria = pygame.transform.scale(pygame.image.load(os.path.join('link',"link_vitoria.png")), (50,50))

        link_frente1 = pygame.image.load(os.path.join('link',"link_frente1.png"))
        link_frente2 = pygame.image.load(os.path.join('link',"link_frente2.png"))
        link_costas1 = pygame.image.load(os.path.join('link',"link_costas1.png"))
        link_costas2 = pygame.image.load(os.path.join('link',"link_costas2.png"))
        link_direita1 = pygame.image.load(os.path.join('link',"link_direita1.png"))
        link_direita2 = pygame.image.load(os.path.join('link',"link_direita2.png"))
        link_esquerda1 = pygame.image.load(os.path.join('link',"link_esquerda1.png"))
        link_esquerda2 = pygame.image.load(os.path.join('link',"link_esquerda2.png"))
        link_ataque_frente = pygame.image.load(os.path.join('link',"link_ataque_frente.png"))
        link_ataque_costas = pygame.image.load(os.path.join('link',"link_ataque_costas.png"))
        link_ataque_direita = pygame.image.load(os.path.join('link',"link_ataque_direita.png"))
        link_ataque_esquerda = pygame.image.load(os.path.join('link',"link_ataque_esquerda.png"))

        link_frente1_dano = pygame.image.load(os.path.join('link',"link_frente1_dano.png"))
        link_frente2_dano = pygame.image.load(os.path.join('link',"link_frente2_dano.png"))
        link_costas1_dano = pygame.image.load(os.path.join('link',"link_costas1_dano.png"))
        link_costas2_dano = pygame.image.load(os.path.join('link',"link_costas2_dano.png"))
        link_direita1_dano = pygame.image.load(os.path.join('link',"link_direita1_dano.png"))
        link_direita2_dano = pygame.image.load(os.path.join('link',"link_direita2_dano.png"))
        link_esquerda1_dano = pygame.image.load(os.path.join('link',"link_esquerda1_dano.png"))
        link_esquerda2_dano = pygame.image.load(os.path.join('link',"link_esquerda2_dano.png"))

        k_frente1 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_frente1.png")), (50,50))
        k_frente2 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_frente2.png")), (50,50))
        k_costas1 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_costas1.png")), (50,50))
        k_costas2 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_costas2.png")), (50,50))
        k_direita1 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_direita1.png")), (50,50))
        k_direita2 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_direita2.png")), (50,50))
        k_esquerda1 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_esquerda1.png")), (50,50))
        k_esquerda2 = pygame.transform.scale(pygame.image.load(os.path.join('mob1',"k_esquerda2.png")), (50,50))

        a_frente1 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_frente1.png")), (50,50))
        a_frente2 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_frente2.png")), (50,50))
        a_costas1 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_costas1.png")), (50,50))
        a_costas2 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_costas2.png")), (50,50))
        a_direita1 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_direita1.png")), (50,50))
        a_direita2 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_direita2.png")), (50,50))
        a_esquerda1 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_esquerda1.png")), (50,50))
        a_esquerda2 = pygame.transform.scale(pygame.image.load(os.path.join('mob2',"a_esquerda2.png")), (50,50))


        vida = pygame.image.load(os.path.join('hud',"vida.png"))
        vida = pygame.transform.scale(vida, (147, 27))
        coracao = pygame.image.load(os.path.join('hud',"s2.png"))
        coracao = pygame.transform.scale(coracao, (30, 30))

        ## LISTAS DE IMAGENS DO LINK ## 
        frente = [link_frente1, link_frente2, link_ataque_frente]
        costas = [link_costas1, link_costas2, link_ataque_costas]
        direita = [link_direita1, link_direita2, link_ataque_direita]
        esquerda = [link_esquerda1, link_esquerda2, link_ataque_esquerda]

        frente_dano = [link_frente1_dano, link_frente2_dano]
        costas_dano = [link_costas1_dano, link_costas2_dano]
        direita_dano = [link_direita1_dano, link_direita2_dano]
        esquerda_dano = [link_esquerda1_dano, link_esquerda2_dano]

        posicoes = {0:frente, 1:costas, 2:direita, 3:esquerda}


        ## LISTAS DE IMAGENS DOS INIMIGOS ##

        k_frente = [k_frente1, k_frente2]
        k_costas = [k_costas1, k_costas2]
        k_direita = [k_direita1, k_direita2]
        k_esquerda = [k_esquerda1, k_esquerda2]
        k_posicoes = {0:k_frente, 1:k_costas, 2:k_direita, 3:k_esquerda}

        a_frente = [a_frente1, a_frente2]
        a_costas = [a_costas1, a_costas2]
        a_direita = [a_direita1, a_direita2]
        a_esquerda = [a_esquerda1, a_esquerda2]
        a_posicoes = {0:a_frente, 1:a_costas, 2:a_direita, 3:a_esquerda}


        count1 = 0
        count2 = 0
        player = frente[0]
        player = pygame.transform.scale(player, (50, 50))
        playerX = 340
        playerY = 504

        kavaleiro = k_frente[0]

        fundo_sala1 = pygame.transform.scale(pygame.image.load(os.path.join('fundos',"fundo.png")), (756, 504)) 
        fundo_sala2 = pygame.transform.scale(pygame.image.load(os.path.join('fundos',"fundo2.png")), (756, 504)) 
        fundo_sala6 = pygame.transform.scale(pygame.image.load(os.path.join('fundos',"fundo6.png")), (756, 504))
        fundo_sala9 = pygame.transform.scale(pygame.image.load(os.path.join('fundos',"fundo9.png")), (756, 504))
        fundo_sala8 = pygame.transform.scale(pygame.image.load(os.path.join('fundos',"fundo8.png")), (756, 504))
        fundo_sala10 = pygame.transform.scale(pygame.image.load(os.path.join('fundos',"fundo10.png")), (756, 504)) 

        ####################################################### CLASSES ###################################################

        class Sala(object):
            def __init__(self, img_fundo, barreiras, mobs, conexoes):
                self.img_fundo = img_fundo
                self.barreiras = barreiras
                self.mobs = mobs ##lista dos inimigos na sala
                self.conexoes = conexoes

            def posicionar_imagem_fundo(self):
                screen.blit(self.img_fundo , (0,128))

            def posicionar_mobs(self):
                for mob in self.mobs:
                    if mob.vivo > 0:
                        mob.mob_na_tela()
                    else:
                        mob.retangulo = mob.imagem_presente.get_rect(topleft=(0, 0))

            def checar_colisoes_mobs(self):
                for mob in self.mobs:
                    a = player.get_rect(topleft=(playerX, playerY))
                    b = mob.retangulo
                    if a.colliderect(b):
                        return mob
                pygame.display.flip()

            def andar_mobs(self):
                for mob in self.mobs:
                    mob.andar_mob_aleatoriamente()

            def posicionar_barreiras(self):
                for barreira in self.barreiras:
                    barreira.barreira_na_tela()
                    
                    

        class Mob(object):
            def __init__(self, imagem_presente, imagens, vivo, mobX, mobY, pontos):
                self.imagem_presente = imagem_presente
                self.imagens = imagens
                self.posicao_atual = 0
                self.vivo = vivo
                self.mobX = mobX
                self.mobY = mobY
                self.retangulo = self.imagem_presente.get_rect(topleft=(self.mobX, self.mobY))
                self.count_a = 0
                self.count_b = 0
                self.direcao = 0
                self.colisao = False
                self.pontos = pontos

            def mob_na_tela(self):
                screen.blit(self.imagem_presente,(self.mobX,self.mobY))
                ## pygame.draw.rect(screen,(0,0,0),(75,205,606,355), 3)
                ## x = random.choice([a,s,d,f]))

            def andar_mob_aleatoriamente(self):
                if self.colisao == False:
                    if self.count_a % 25 == 0:
                        self.direcao = random.randint(0, 3)
                if self.direcao == 1:
                    self.mobY = self.mobY - 5
                elif self.direcao == 0:
                    self.mobY = self.mobY + 5
                elif self.direcao == 2:
                    self.mobX = self.mobX + 5
                elif self.direcao == 3:
                    self.mobX = self.mobX - 5
                self.imagem_presente = self.imagens[self.direcao][self.count_b]
                self.count_b = (self.count_b + 1) % 2
                self.count_a += 1
                if self.vivo > 0:
                    self.retangulo = self.imagem_presente.get_rect(topleft=(self.mobX, self.mobY))
                else:
                    self.retangulo = self.imagem_presente.get_rect(topleft=(0, 0))
                self.colisao = False


        class Cavaleiro_Vermelho(Mob):
            def __init__(self, mobX, mobY):
                super(Cavaleiro_Vermelho, self).__init__(
                    k_frente1, #IMAGEM PARA INICIALIZAÇÃO
                    [[k_frente1, k_frente2],[k_costas1, k_costas2],[k_direita1, k_direita2],[k_esquerda1, k_esquerda2]],
                    1, # NUMERO DE VIDAS
                    mobX, mobY, 
                    20) #PONTOS
                self.mobX = mobX
                self.mobY = mobY

        class Cavaleiro_Azul(Mob):
            def __init__(self, mobX, mobY):
                super(Cavaleiro_Azul, self).__init__(
                    a_frente1, #IMAGEM PARA INICIALIZAÇÃO
                    [[a_frente1, a_frente2],[a_costas1, a_costas2],[a_direita1, a_direita2],[a_esquerda1, a_esquerda2]],
                    3, # NUMERO DE VIDAS
                    mobX, mobY, 
                    70) #PONTOS
                self.mobX = mobX
                self.mobY = mobY
                



        class Barreira(object):
            def __init__(self, barrX, barrY, imagem, passavel, retangulo):
                self.barrX = barrX
                self.barrY = barrY
                self.imagem = imagem
                self.passavel = passavel
                self.retangulo = retangulo
                
            def barreira_na_tela(self):
                if self.imagem != None:
                    screen.blit(self.imagem,(self.barrX,self.barrY))
                    if self.retangulo == None:
                        self.retangulo = self.imagem.get_rect(topleft=(self.barrX, self.barrY))
                    #pygame.draw.rect(screen,(255,0,0),self.retangulo) ##ATIVAR PARA TESTES


                
            
        ###################################################### BARREIRAS ################################################

        parede_cima_A = Barreira(0, 0, None, False, pygame.Rect(0, 128, 335, 74))
        parede_cima_B = Barreira(0, 0, None, False, pygame.Rect(420, 128, 300, 74))
        parede_cima_C = Barreira(0, 0, None, True, pygame.Rect(0, 128, 900, 74))

        parede_baixo_A = Barreira(0, 0, None, False, pygame.Rect(0, 555, 335, 70))
        parede_baixo_B = Barreira(0, 0, None, False, pygame.Rect(420, 555, 300, 70))
        parede_baixo_C = Barreira(0, 0, None, True, pygame.Rect(0, 554, 999, 70))

        parede_esq_A = Barreira(0, 0, None, False, pygame.Rect(0, 128, 70, 212))
        parede_esq_B = Barreira(0, 0, None, False, pygame.Rect(0, 410, 70, 220))
        parede_esq_C = Barreira(0, 0, None, True, pygame.Rect(0, 128, 70, 900))

        parede_dir_A = Barreira(0, 0, None, False, pygame.Rect(680, 128, 70, 212))
        parede_dir_B = Barreira(0, 0, None, False, pygame.Rect(680, 410, 70, 220))
        parede_dir_C = Barreira(0, 0, None, True, pygame.Rect(680, 128, 70, 900))

        paredes_default = [parede_cima_A, parede_cima_B, parede_cima_C, parede_baixo_A, parede_baixo_B, parede_baixo_C,
                             parede_esq_A, parede_esq_B, parede_esq_C, parede_dir_A, parede_dir_B, parede_dir_C]


        sem_porta_baixo = Barreira(328,556,parede_baixo,False, pygame.Rect(0, 554, 999, 70))
        sem_porta_cima = Barreira(328,127,parede_cima,False, pygame.Rect(0, 128, 900, 74))
        sem_porta_direita = Barreira(680,330,parede_direita,False, pygame.Rect(681, 128, 70, 900))
        sem_porta_esquerda = Barreira(-1,330,parede_esquerda,False, pygame.Rect(0, 335, 70, 220))

        parede_falsa_cima = Barreira(328,127,parede_cima,True, pygame.Rect(0, 128, 900, 74))
        parede_falsa_baixo = Barreira(328,556,parede_baixo,True, pygame.Rect(0, 554, 999, 70))

        bloco11 = Barreira(77,505,imagem_bloco,False,None)
        bloco12 = Barreira(127,505,imagem_bloco,False,None)
        bloco13 = Barreira(177,505,imagem_bloco,False,None)
        bloco14 = Barreira(227,505,imagem_bloco,False,None)
        bloco15 = Barreira(275,505,imagem_bloco,False,None)
        bloco16 = Barreira(327,505,imagem_bloco,False,None)
        bloco110 = Barreira(530,505,imagem_bloco,False,None)
        bloco111 = Barreira(580,505,imagem_bloco,False,None)
        bloco112 = Barreira(630,505,imagem_bloco,False,None)

        bloco21 = Barreira(77,454,imagem_bloco,False,None)
        bloco22 = Barreira(127,454,imagem_bloco,False,None)
        bloco23 = Barreira(177,454,imagem_bloco,False,None)
        bloco24 = Barreira(227,454,imagem_bloco,False,None)
        bloco26 = Barreira(327,454,imagem_bloco,False,None)
        bloco25 = Barreira(275,454,imagem_bloco,False,None)
        bloco27 = Barreira(377,454,imagem_bloco,False,None)
        bloco28 = Barreira(429,454,imagem_bloco,False,None)
        bloco29 = Barreira(480,454,imagem_bloco,False,None)
        bloco210 = Barreira(530,454,imagem_bloco,False,None)
        bloco211 = Barreira(580,454,imagem_bloco,False,None)
        bloco212 = Barreira(630,454,imagem_bloco,False,None)

        bloco31 = Barreira(77,403,imagem_bloco,False,None)
        bloco32 = Barreira(127,403,imagem_bloco,False,None)
        bloco33 = Barreira(177,403,imagem_bloco,False,None)
        bloco34 = Barreira(227,403,imagem_bloco,False,None)
        bloco35 = Barreira(275,403,imagem_bloco,False,None)
        bloco36 = Barreira(327,403,imagem_bloco,False,None)
        bloco37 = Barreira(377,403,imagem_bloco,False,None)
        bloco38 = Barreira(429,403,imagem_bloco,False,None)
        bloco39 = Barreira(480,403,imagem_bloco,False,None)
        bloco310 = Barreira(530,403,imagem_bloco,False,None)
        bloco311 = Barreira(580,403,imagem_bloco,False,None)
        bloco312 = Barreira(630,403,imagem_bloco,False,None)

        bloco42 = Barreira(127,354,imagem_bloco,False,None)
        bloco43 = Barreira(177,354,imagem_bloco,False,None)
        bloco44 = Barreira(227,354,imagem_bloco,False,None)
        bloco45 = Barreira(275,354,imagem_bloco,False,None)
        bloco46 = Barreira(327,354,imagem_bloco,False,None)
        bloco47 = Barreira(377,354,imagem_bloco,False,None)
        bloco48 = Barreira(429,354,imagem_bloco,False,None)
        bloco49 = Barreira(480,354,imagem_bloco,False,None)
        bloco410 = Barreira(530,354,imagem_bloco,False,None)
        bloco411 = Barreira(580,354,imagem_bloco,False,None)

        bloco51 = Barreira(77,305,imagem_bloco,False,None)
        bloco52 = Barreira(127,305,imagem_bloco,False,None)
        bloco53 = Barreira(177,305,imagem_bloco,False,None)
        bloco54 = Barreira(227,305,imagem_bloco,False,None)
        bloco55 = Barreira(275,305,imagem_bloco,False,None)
        bloco56 = Barreira(327,305,imagem_bloco,False,None)
        bloco57 = Barreira(377,305,imagem_bloco,False,None)
        bloco58 = Barreira(429,305,imagem_bloco,False,None)
        bloco59 = Barreira(480,305,imagem_bloco,False,None)
        bloco510 = Barreira(530,305,imagem_bloco,False,None)
        bloco511 = Barreira(580,305,imagem_bloco,False,None)
        bloco512 = Barreira(630,305,imagem_bloco,False,None)

        bloco61 = Barreira(77,255,imagem_bloco,False,None)
        bloco62 = Barreira(127,255,imagem_bloco,False,None)
        bloco63 = Barreira(177,255,imagem_bloco,False,None)
        bloco64 = Barreira(227,255,imagem_bloco,False,None)
        bloco65 = Barreira(275,255,imagem_bloco,False,None)
        bloco66 = Barreira(327,255,imagem_bloco,False,None)
        bloco67 = Barreira(377,255,imagem_bloco,False,None)
        bloco68 = Barreira(429,255,imagem_bloco,False,None)
        bloco69 = Barreira(480,255,imagem_bloco,False,None)
        bloco610 = Barreira(530,255,imagem_bloco,False,None)
        bloco611 = Barreira(580,255,imagem_bloco,False,None)
        bloco612 = Barreira(630,255,imagem_bloco,False,None)

        bloco71 = Barreira(77,205,imagem_bloco,False,None)
        bloco72 = Barreira(127,205,imagem_bloco,False,None)
        bloco73 = Barreira(177,205,imagem_bloco,False,None)
        bloco74 = Barreira(227,205,imagem_bloco,False,None)
        bloco75 = Barreira(275,205,imagem_bloco,False,None)
        bloco76 = Barreira(327,205,imagem_bloco,False,None)
        bloco77 = Barreira(377,205,imagem_bloco,False,None)
        bloco78 = Barreira(429,205,imagem_bloco,False,None)
        bloco79 = Barreira(480,205,imagem_bloco,False,None)
        bloco710 = Barreira(530,205,imagem_bloco,False,None)
        bloco711 = Barreira(580,205,imagem_bloco,False,None)
        bloco712 = Barreira(630,205,imagem_bloco,False,None)

        Triforce = Barreira(353,364,imagem_triforce,True,None)

        ####################################################### INIMIGOS ################################################   

        cavaleiro_2a = Cavaleiro_Vermelho(630,255)
        cavaleiro_2b = Cavaleiro_Vermelho(125,255)
        cavaleiro_2c = Cavaleiro_Vermelho(120,495)
        cavaleiro_2d = Cavaleiro_Azul(230,320)
        cavaleiro_2e = Cavaleiro_Vermelho(585,495)
        cavaleiro_2f = Cavaleiro_Vermelho(430,320)
        cavaleiro_2g = Cavaleiro_Vermelho(430,220)

        cavaleiro_3a = Cavaleiro_Vermelho(390,300)
        cavaleiro_3b = Cavaleiro_Vermelho(560,225)
        cavaleiro_3c = Cavaleiro_Azul(390,300)
        cavaleiro_3d = Cavaleiro_Vermelho(560,225)
        cavaleiro_3e = Cavaleiro_Vermelho(85,215)

        cavaleiro_4a = Cavaleiro_Azul(115,354)
        cavaleiro_4b = Cavaleiro_Azul(295,354)
        cavaleiro_4c = Cavaleiro_Vermelho(465,354)
        cavaleiro_4d = Cavaleiro_Vermelho(430,220)
        cavaleiro_4e = Cavaleiro_Vermelho(430,220)

        cavaleiro_5a = Cavaleiro_Azul(197,354)
        cavaleiro_5b = Cavaleiro_Vermelho(347,354)
        cavaleiro_5c = Cavaleiro_Azul(500,354)
        cavaleiro_5d = Cavaleiro_Vermelho(347,264)
        cavaleiro_5e = Cavaleiro_Vermelho(347,464)

        cavaleiro_6a = Cavaleiro_Vermelho(430,320)
        cavaleiro_6b = Cavaleiro_Vermelho(430,220)
        cavaleiro_6c = Cavaleiro_Azul(230,320)
        cavaleiro_6d = Cavaleiro_Azul(360,460)
        cavaleiro_6e = Cavaleiro_Azul(327,320)
        cavaleiro_6f = Cavaleiro_Vermelho(230,220)

        cavaleiro_7a = Cavaleiro_Azul(127,460)
        cavaleiro_7b = Cavaleiro_Azul(560,460)
        cavaleiro_7c = Cavaleiro_Azul(177,320)
        cavaleiro_7d = Cavaleiro_Azul(560,320)
        cavaleiro_7e = Cavaleiro_Azul(360,460)
        cavaleiro_7f = Cavaleiro_Azul(327,320)

        cavaleiro_9a = Cavaleiro_Vermelho(377,454)
        cavaleiro_9b = Cavaleiro_Vermelho(480,355)
        cavaleiro_9c = Cavaleiro_Azul(377,355)
        cavaleiro_9d = Cavaleiro_Vermelho(377,454)

        cavaleiro_10a = Cavaleiro_Vermelho(377,354)
        cavaleiro_10b = Cavaleiro_Azul(480,255)
        cavaleiro_10c = Cavaleiro_Azul(377,255)
        cavaleiro_10d = Cavaleiro_Vermelho(377,354)

        cavaleiro_11a = Cavaleiro_Azul(275,255)
        cavaleiro_11b = Cavaleiro_Azul(275,454)
        cavaleiro_11c = Cavaleiro_Azul(275,354)
        cavaleiro_11d = Cavaleiro_Azul(530,255)
        cavaleiro_11e = Cavaleiro_Azul(500,403)
        cavaleiro_11f = Cavaleiro_Azul(397,474)

        cavaleiro_13a = Cavaleiro_Azul(127,454)
        cavaleiro_13b = Cavaleiro_Azul(377,255)
        cavaleiro_13c = Cavaleiro_Vermelho(377,403)
        cavaleiro_13d = Cavaleiro_Azul(227,235)
        cavaleiro_13e = Cavaleiro_Vermelho(439,354)



        ####################################################### SALAS ####################################################
                
        Sala1 = Sala(fundo_sala1, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_baixo, bloco55, bloco58, bloco73, bloco710], ##barreiras
                     
                     [],## lista dos inimigos na sala
                     {0:2, 1:None, 2:3, 3:4} ## conexões
                     )

        Sala2 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_cima, bloco13, bloco110, bloco23, bloco210, bloco33, bloco310, bloco43, bloco410,
                      bloco53, bloco510], 
                     
                     [cavaleiro_2a, cavaleiro_2b, cavaleiro_2c, cavaleiro_2d, cavaleiro_2e, cavaleiro_2f,cavaleiro_2g],
                     {0:None, 1:1, 2:5, 3:6}
                     )

        Sala3 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_baixo, sem_porta_cima, sem_porta_direita, bloco53, bloco43, bloco33,
                      bloco46, bloco59, bloco49, bloco39, bloco16, bloco76], 
                     
                     [cavaleiro_3a, cavaleiro_3b, cavaleiro_3c, cavaleiro_3d, cavaleiro_3e],
                     {0:None, 1:None, 2:None, 3:1}
                     )

        Sala4 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_baixo, parede_falsa_cima, sem_porta_esquerda,bloco310,bloco410,bloco510,bloco610,bloco710,
                      bloco54,bloco44,bloco34,bloco57,bloco47,bloco37],
                     
                     [cavaleiro_4a,cavaleiro_4b,cavaleiro_4c,cavaleiro_4d,cavaleiro_4e],
                     {0:6, 1:None, 2:1, 3:None}
                     )

        Sala6 = Sala(fundo_sala6, ##imagem de fundo
                     
                     paredes_default +
                     [parede_falsa_baixo,bloco12,bloco111,bloco22,bloco211,bloco72,bloco711,bloco62,bloco611], 
                     
                     [cavaleiro_6a,cavaleiro_6b,cavaleiro_6c,cavaleiro_6d,cavaleiro_6e,cavaleiro_6f],
                     {0:7, 1:4, 2:2, 3:10}
                     )

        Sala5 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_baixo,sem_porta_cima,sem_porta_direita,bloco32,bloco35,bloco38,bloco311,bloco42,
                      bloco45,bloco48,bloco411,bloco52,bloco55,bloco58,bloco511], 
                     
                     [cavaleiro_5a,cavaleiro_5b,cavaleiro_5c,cavaleiro_5d,cavaleiro_5e],
                     {0:None, 1:None, 2:None, 3:2}
                     )

        Sala7 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [parede_falsa_cima, bloco71,bloco72,bloco73,bloco74,bloco75,bloco76,bloco77,bloco78,bloco79,
                      bloco710,bloco711,bloco712,bloco61,bloco62,bloco63,bloco64,bloco65,bloco66,bloco67,bloco68,bloco69,
                      bloco610,bloco611,bloco612,bloco31,bloco32,bloco33,bloco34,bloco35,bloco36,bloco37,bloco38,
                      bloco39,bloco310,bloco311,bloco312], 
                     
                     [cavaleiro_7a,cavaleiro_7b,cavaleiro_7c,cavaleiro_7d,cavaleiro_7e,cavaleiro_7f],
                     {0:11, 1:6, 2:8, 3:9}
                     )

        Sala8 = Sala(fundo_sala8, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_baixo, sem_porta_direita,bloco21,bloco22,bloco23,bloco24,bloco25,bloco26,bloco27,
                      bloco38,bloco49,bloco59,bloco69,bloco79], 
                     
                     [],
                     {0:13, 1:None, 2:None, 3:7}
                     )

        Sala9 = Sala(fundo_sala9, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_cima, sem_porta_esquerda,bloco65,bloco66,bloco67,bloco68,bloco69,
                      bloco610,bloco611,bloco612,bloco54,bloco44,bloco34,bloco24,bloco14], 
                     
                     [cavaleiro_9a,cavaleiro_9b,cavaleiro_9c,cavaleiro_9d],
                     {0:None, 1:10, 2:7, 3:None}
                     )

        Sala10 = Sala(fundo_sala10, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_baixo, sem_porta_esquerda,bloco25,bloco26,bloco27,bloco28,bloco29,bloco210,
                      bloco211,bloco212,bloco34,bloco44,bloco54,bloco64,bloco74], 
                     
                     [cavaleiro_10a,cavaleiro_10b,cavaleiro_10c,cavaleiro_10d],
                     {0:9, 1:None, 2:6, 3:None}
                     )

        Sala11 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_baixo, sem_porta_esquerda,bloco111,bloco211,bloco311,bloco411,bloco111,
                      bloco38,bloco48,bloco58,bloco68,bloco78,bloco13,bloco23,bloco33,bloco43,bloco53,bloco63,bloco73], 
                     
                     [cavaleiro_11a,cavaleiro_11b,cavaleiro_11c,cavaleiro_11d,cavaleiro_11e,cavaleiro_11f],
                     {0:12, 1:7, 2:13, 3:None}
                     )

        Sala12 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_cima, sem_porta_esquerda, sem_porta_direita,bloco62,bloco63,bloco64,bloco65,bloco66,
                      bloco67,bloco68,bloco69,bloco610,bloco611,bloco22,bloco32,bloco42,bloco52,bloco211,bloco311,
                      bloco411,bloco511,bloco23,bloco24,bloco25,bloco28,bloco29,bloco210,bloco44,bloco49,bloco55,
                      bloco58,Triforce],
                      
                      [],
                     {0:None, 1:11, 2:None, 3:None}
                     )

        Sala13 = Sala(fundo_sala2, ##imagem de fundo
                     
                     paredes_default +
                     [sem_porta_cima, sem_porta_direita,bloco15,bloco25,bloco35,bloco110,bloco210,bloco310,
                      bloco410,bloco510,bloco610,bloco710,bloco45,bloco55,bloco42,bloco52,bloco62,bloco72], 
                     
                     [cavaleiro_13a,cavaleiro_13b,cavaleiro_13c,cavaleiro_13d,cavaleiro_13e],
                     {0:None, 1:8, 2:None, 3:11}
                     )


        #------------------ RELAÇÃO PARA CONEXÃO ENTRE AS SALAS ------------------#
        mundo = {1:Sala1, 2:Sala2, 3:Sala3, 4:Sala4, 5:Sala5, 6:Sala6, 7:Sala7, 8:Sala8, 9:Sala9, 10:Sala10, 11:Sala11,
                 12:Sala12, 13: Sala13}

        mapa_atual = 1

        ###### Identificador da sala atual (OBJETO) ######

        Sala_atual = mundo[mapa_atual]
        screen.blit

        jogo_em_execucao = True
        posicao = 0
        pygame.draw.rect(screen,(0,0,0),(1,1,largura,126))
        tempo = 0
        pontos = 0

        estado_de_dano = False


        def atualizar_fundo():
            screen.fill((0,0,0))
            
            screen.blit(texto_tempo,(20,30))
            screen.blit(texto_pontos,(20,70))
            
            
            Sala_atual.posicionar_imagem_fundo()
            
            ##pygame.draw.rect(screen,(255,0,0),(0,200,200,200), 3)
            screen.blit(texto_vida,(547,30))
            #screen.blit(vida, (560,20))
            Sala_atual.posicionar_mobs()
            Sala_atual.posicionar_barreiras()
            pygame.draw.rect(screen,(0,0,0),(0,128,756, 505), 3)

            ## CORAÇOES NA TELA
            for i in range(vida_atual):
                screen.blit(coracao, (523 + (35*i),70))
                
                        
            tamanho_numero = len(str(int(tempo)))
                
            if tamanho_numero == 1:
                tempo_numero = ("00000%.f" % tempo)
            elif tamanho_numero == 2:
                tempo_numero = ("0000%.f" % tempo)
            elif tamanho_numero == 3:
                tempo_numero = ("000%.f" % tempo)
            elif tamanho_numero == 4:
                tempo_numero = ("00%.f" % tempo)
            elif tamanho_numero == 5:
                tempo_numero = ("0%.f" % tempo)
            elif tamanho_numero == 6:
                tempo_numero = ("%.f" % tempo)
            else:
                tempo_numero = "999999"

            texto_tempo_numero = minha_fonte.render(tempo_numero, False, meu_vermelho)
            screen.blit(texto_tempo_numero,(140,30))


            tamanho_pontos = len(str(int(pontos)))    
            if tamanho_pontos == 1:
                pontos_numero = ("00000%s" % pontos)
            elif tamanho_pontos == 2:
                pontos_numero = ("0000%s" % pontos)
            elif tamanho_pontos == 3:
                pontos_numero = ("000%s" % pontos)
            elif tamanho_pontos == 4:
                pontos_numero = ("00%s" % pontos)
            elif tamanho_pontos == 5:
                pontos_numero = ("0%s" % pontos)
            elif tamanho_pontos == 6:
                pontos_numero = ("%s" % pontos)
            else:
                pontos_numero = "999999"
                
            texto_pontos_numero = minha_fonte.render(pontos_numero, False, meu_vermelho)
            screen.blit(texto_pontos_numero,(160,70))
            

            
        asd = pygame.Rect(80,200,606,354)
        ret = pygame.Rect(0,200,200,200)
        kavX, kavY = 300, 300
        vitoria = False


        screen.blit(imagem_abertura,(0,0))
        pygame.display.flip()
                    
        audio_intro.play(-1)


        loop_abertura = True          
        while loop_abertura:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(2)):
                    pygame.time.delay(200)
                    loop_abertura = False
                if event.type == pygame.QUIT or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(6)):
                    jogo_em_execucao = False
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    jogo_em_execucao = False
                    exit()

        screen.blit(imagem_instrucoes,(0,0))
        pygame.display.flip()


        loop_instrucoes = True          
        while loop_instrucoes:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(2)):
                    pygame.time.delay(200)
                    loop_instrucoes = False
                if event.type == pygame.QUIT or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(6)):
                    jogo_em_execucao = False
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    jogo_em_execucao = False
                    exit()


        screen.blit(imagem_dificuldade,(0,0))
        screen.blit(imagem_triforce,(127,155))
        pygame.display.flip()

        #177,354/177,255/177,155
        loop_dificuldade = True
        SELETOR_Y = 155
        SELETOR_LISTA = [145,245,344]
        i = 0

        while loop_dificuldade:
                
                for event in pygame.event.get():
            
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (qtd_joysticks != 0 and controle.get_hat(0) == (0,-1)): #keys[pygame.K_DOWN] or (qtd_joysticks != 0 and(controle.get_hat(0) == (0,-1))):
                                i += 1
                                if i > 2:
                                    i = 0
                                
                                        
                        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (qtd_joysticks != 0 and controle.get_hat(0) == (0,1)):
                                i -= 1
                                if i < 0:
                                    i = 2
                                
                        
                        elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE))or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(2)):
                            audio_intro.stop()
                            pygame.time.delay(200)
                            loop_dificuldade = False
                        if event.type == pygame.QUIT:
                            jogo_em_execucao = False
                            exit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            jogo_em_execucao = False
                            exit()


                SELETOR_Y = SELETOR_LISTA[i]
                screen.blit(imagem_dificuldade,(0,0))
                screen.blit(imagem_triforce,(127,SELETOR_Y))
                pygame.display.flip()

                vidas_por_dificuldade = [6,3,1]
                vida_atual = 6

        dificuldade = i
        vidas_por_dificuldade = [6,3,1]
        vida_atual = vidas_por_dificuldade[dificuldade]    


        audio_jogo.play(-1)  
        while jogo_em_execucao == True:

            if vida_atual <= 0:
                atualizar_fundo()
                player = link_morte
                screen.blit(player, (playerX, playerY))
                pygame.display.flip()
                pygame.time.delay(200)
                break

            if vitoria == True:
                atualizar_fundo()
                player = link_vitoria
                screen.blit(player, (playerX, playerY))
                pygame.display.flip()
                pygame.time.delay(200)
                break
                

            Sala_atual = mundo[mapa_atual]
            atualizar_fundo()
            clock.tick(20)
            tempo += 0.05
            
            if estado_de_dano == True:
                if tempo >= tempo_estado_de_dano + 0.5:
                    estado_de_dano = False
                
            
            for barreira in Sala_atual.barreiras:
                for mob in Sala_atual.mobs:
                    if barreira.retangulo != None:
                        a = mob.retangulo
                        if a.colliderect(barreira.retangulo):
                            if mob.direcao == 0:
                                a.bottom = barreira.retangulo.top - 10
                                mob.direcao = 1
                                
                            elif mob.direcao == 1:
                                a.top = barreira.retangulo.bottom + 10
                                mob.direcao = 0
                                
                            elif mob.direcao == 3:
                                a.right = barreira.retangulo.left - 10
                                mob.direcao = 2
                                
                            elif mob.direcao == 2:
                                a.left = barreira.retangulo.right + 10
                                mob.direcao = 3
                            mob.colisao = True
                            

             ## ANDA OS MOBS ###################################################################################
                            
            Sala_atual.andar_mobs()
           
                
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    jogo_em_execucao = False
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    jogo_em_execucao = False
                    exit()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(2)):
                    atualizar_fundo()
                    
            
                    player = posicoes[posicao][2]
                    if posicao == 0 or posicao == 1:
                        player = pygame.transform.scale(player, (50, 80))
                    else:
                        player = pygame.transform.scale(player, (80, 50))
                        
                    if posicao == 1:
                        playerY -= 30
                    if posicao == 3:
                        playerX -= 30

                    audio_espada.play()
                    screen.blit(player, (playerX, playerY))
                    
        #################### ATACAR INIMIGOS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!############################
                    mob = Sala_atual.checar_colisoes_mobs()
                    if mob != None:
                        audio_morte_mob.play()
                        mob.vivo -= 1
                        if mob.vivo == 0:
                            pontos += mob.pontos
                        
                        
                    pygame.display.flip()
                    pygame.time.delay(150)
                    atualizar_fundo()
                    
                    if posicao == 1:
                        playerY += 30
                    if posicao == 3:
                        playerX += 30
                        
                    player = posicoes[posicao][0]
                    player = pygame.transform.scale(player, (50, 50))
                    screen.blit(player, (playerX, playerY))
                        
            for barreira in Sala_atual.barreiras:
                    a = player.get_rect(topleft=(playerX, playerY))
                    if a.colliderect(barreira.retangulo):
                            if barreira.passavel == False:
                                    if posicao == 0:
                                            a.bottom = barreira.retangulo.top
                                            playerX,playerY = a.topleft
                                    if posicao == 1:
                                            playerY = barreira.retangulo.bottom
                                    if posicao == 2:
                                            a.right = barreira.retangulo.left
                                            playerX,playerY = a.topleft
                                    if posicao == 3:
                                            playerX = barreira.retangulo.right
                            elif barreira == Triforce:
                                    vitoria = True
                                                    
                        
            keys = pygame.key.get_pressed()
            

                
            if keys[pygame.K_DOWN] or (qtd_joysticks != 0 and(controle.get_hat(0) == (0,-1))):
                if estado_de_dano == False:
                    player = frente[count1]
                else:
                    player = frente_dano[count1]
                count1 = (count1 + 1) % 2
                playerY = playerY + 12
                posicao = 0 ##frente
                        
            elif keys[pygame.K_UP] or (qtd_joysticks != 0 and(controle.get_hat(0) == (0,1))):
                if estado_de_dano == False:
                    player = costas[count1]
                else:
                    player = costas_dano[count1]
                count1 = (count1 + 1) % 2
                playerY = playerY - 12
                posicao = 1 ##costas

            elif keys[pygame.K_RIGHT] or (qtd_joysticks != 0 and(controle.get_hat(0) == (1,0))):
                if estado_de_dano == False:
                    player = direita[count1]
                else:
                    player = direita_dano[count1]
                count1 = (count1 + 1) % 2
                playerX = playerX + 12
                posicao = 2 ##direita
                
            elif keys[pygame.K_LEFT] or (qtd_joysticks != 0 and (controle.get_hat(0) == (-1,0))):
                if estado_de_dano == False:
                    player = esquerda[count1]
                else:
                    player = esquerda_dano[count1]
                count1 = (count1 + 1) % 2
                playerX = playerX - 12
                posicao = 3 ##esquerda



            player = pygame.transform.scale(player, (50, 50))
            if playerY > 136 and playerX < 704:
                screen.blit(player, (playerX, playerY))
                pygame.display.update()
                
           
        ### DANO POR COLISÂO COM INIMIGOS: IMPLICA PERDA DE PONTOS, ATIVA ESTADO DE DANO
            if estado_de_dano == False:
                mob = Sala_atual.checar_colisoes_mobs()
                if mob != None:
                    audio_link_dano.play()
                    vida_atual -= 1
                    if pontos - 30 >= 0:
                        pontos = pontos - 30
                    else:
                        pontos = 0
                    estado_de_dano = True
                    tempo_estado_de_dano = tempo
                    


            if playerX > 704:
                if Sala_atual.conexoes[2] != None:
                    mapa_atual = Sala_atual.conexoes[2]
                    pygame.time.delay(300)
                playerX -= 704
                
            elif playerX < 0:
                if Sala_atual.conexoes[3] != None:
                    mapa_atual = Sala_atual.conexoes[3]
                    pygame.time.delay(300)
                playerX += 704
                
            elif playerY > 568:
                if Sala_atual.conexoes[1] != None:
                    mapa_atual = Sala_atual.conexoes[1]
                    pygame.time.delay(300)
                playerY = 136
                
            elif playerY < 136:
                if Sala_atual.conexoes[0] != None:
                    mapa_atual = Sala_atual.conexoes[0]
                    pygame.time.delay(300)
                playerY = 568

                
            
            pygame.display.flip()

        if vida_atual <= 0:
            audio_jogo.stop()
            audio_link_morte.play()
            pygame.time.delay(2700)
            atualizar_fundo()
            pygame.draw.rect(screen,(0,0,0),(0,128,756, 505))
            pygame.display.update()
            pygame.time.delay(1300)
            screen.blit(texto_game_over,(227,325))
            pygame.display.update()
            #pygame.display.flip()
            audio_game_over.play()
 

        else:
            audio_jogo.stop()
            audio_triforce.play()
            pygame.time.delay(9000)
            atualizar_fundo()
            #pygame.draw.rect(screen,(0,0,0),(0,128,756, 505))
            pygame.draw.rect(screen,(0,0,0),(0,0,largura, altura))
            pygame.display.update()
            pygame.time.delay(1700)
            audio_final.play()
            pygame.time.delay(1700)
            screen.blit(texto_nome,(75,245))
            screen.blit(texto_final,(107,305))
            pygame.display.update()
            if dificuldade == 0:
                    pontos += 10000
            elif dificuldade == 1:
                    pontos += 20000
            elif dificuldade == 2:
                    pontos += 30000
            

            loop_abertura = True
            while loop_abertura:
                    for event in pygame.event.get():
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and(controle.get_button(2)or controle.get_button(0))):
                            pygame.time.delay(200)
                            loop_abertura = False
                        if event.type == pygame.QUIT or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(6)):
                            jogo_em_execucao = False
                            exit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            jogo_em_execucao = False
                            exit()

            tamanho_numero = len(str(int(tempo)))
                
            if tamanho_numero == 1:
                tempo_numero = ("00000%.f" % tempo)
            elif tamanho_numero == 2:
                tempo_numero = ("0000%.f" % tempo)
            elif tamanho_numero == 3:
                tempo_numero = ("000%.f" % tempo)
            elif tamanho_numero == 4:
                tempo_numero = ("00%.f" % tempo)
            elif tamanho_numero == 5:
                tempo_numero = ("0%.f" % tempo)
            elif tamanho_numero == 6:
                tempo_numero = ("%.f" % tempo)
            else:
                tempo_numero = "999999"

            texto_tempo_numero = minha_fonte.render(tempo_numero, False, meu_vermelho)
            
            tamanho_pontos = len(str(int(pontos)))    
            if tamanho_pontos == 1:
                pontos_numero = ("00000%s" % pontos)
            elif tamanho_pontos == 2:
                pontos_numero = ("0000%s" % pontos)
            elif tamanho_pontos == 3:
                pontos_numero = ("000%s" % pontos)
            elif tamanho_pontos == 4:
                pontos_numero = ("00%s" % pontos)
            elif tamanho_pontos == 5:
                pontos_numero = ("0%s" % pontos)
            elif tamanho_pontos == 6:
                pontos_numero = ("%s" % pontos)
            else:
                pontos_numero = "999999"
                
            texto_pontos_numero = minha_fonte.render(pontos_numero, False, meu_vermelho)
            texto_bullet = minha_fonte.render("- ", False, meu_vermelho)
            
            
            screen.blit(imagem_pontuacao,(0,0))
            screen.blit(texto_tempo_numero,(420,142))
            screen.blit(texto_pontos_numero,(420,102))

            screen.blit(texto_tempo,(200,342))
            screen.blit(texto_pontos,(200,302))
            screen.blit(historico[-1][0],(420,342))
            screen.blit(historico[-1][1],(420,302))
            screen.blit(texto_tempo,(200,442))
            screen.blit(texto_pontos,(200,402))
            screen.blit(historico[-2][0],(420,442))
            screen.blit(historico[-2][1],(420,402))
            screen.blit(texto_tempo,(200,542))
            screen.blit(texto_pontos,(200,502))
            screen.blit(historico[-3][0],(420,542))
            screen.blit(historico[-3][1],(420,502))
                    
            pygame.display.flip()
            cod_atual = gerar_codigo()
            
            historico.append((texto_tempo_numero,texto_pontos_numero))

        loop_abertura = True          
        while loop_abertura:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and(controle.get_button(2)or controle.get_button(0))):
                    pygame.time.delay(200)
                    loop_abertura = False
                if event.type == pygame.QUIT or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(6)):
                    jogo_em_execucao = False
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    jogo_em_execucao = False
                    exit()

        

        screen.blit(imagem_jogar_novamente,(0,0))
        screen.blit(imagem_triforce,(127,155))
        pygame.display.flip()
        loop_replay = True
        
        SELETOR_Y = 155
        SELETOR_LISTA = [145,245]
        i = 0
        while loop_replay:
                
                for event in pygame.event.get():
            
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (qtd_joysticks != 0 and controle.get_hat(0) == (0,-1)): #keys[pygame.K_DOWN] or (qtd_joysticks != 0 and(controle.get_hat(0) == (0,-1))):
                                i += 1
                                if i > 1:
                                    i = 0
                                
                                        
                        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (qtd_joysticks != 0 and controle.get_hat(0) == (0,1)):
                                i -= 1
                                if i < 0:
                                    i = 1
                                
                        
                        elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE))or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(2)):
                            audio_intro.stop()
                            pygame.time.delay(200)
                            loop_replay = False
                            
                        if event.type == pygame.QUIT or (qtd_joysticks != 0 and event.type == pygame.JOYBUTTONDOWN and controle.get_button(6)):
                            jogo_em_execucao = False
                            exit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            jogo_em_execucao = False
                            exit()


                SELETOR_Y = SELETOR_LISTA[i]
                screen.blit(imagem_jogar_novamente,(0,0))
                screen.blit(imagem_triforce,(127,SELETOR_Y))
                pygame.display.flip()

        jogar_novamente_lista = [0,1]
        escolha = i
        jogar_novamente = jogar_novamente_lista[escolha]
        
                
        if jogar_novamente == 0:
                if vida_atual <= 0:
                        audio_game_over.stop()
                else:
                        audio_final.stop()
                        
                continue
                
        
        else:
                exit()
            
            
