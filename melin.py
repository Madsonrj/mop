import pygame

pygame.init()


TELA_WIDTH = 800
TELA_HEIGHT = 600

BLOC_WIDTH = TELA_WIDTH//40
BLOC_HEIGHT = TELA_HEIGHT//20

tela = pygame.display.set_mode((TELA_WIDTH,TELA_HEIGHT))

sprite_fundo = pygame.image.load("imagens/basictiles.png").convert_alpha()
sprite_sheet = pygame.image.load("imagens/sprite3.png").convert_alpha()



lista_mapa =[
    "pppppppppppppppppppppppppppppppppppppppp",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p", 
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "p                                      p",
    "pppppppppppppppppppppppppppppppppppppppp",
]



lista_objs =[
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ", 
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
]


def get_frame_by_gid(sprite,gid,columns=4,w=32,h=48,spac_h=0,
                     spac_y=0,margin_left =0, margin_top=0):
    linha = gid // columns
    coluna = gid % columns
    x = margin_left +(coluna*( w + spac_h ))
    y = margin_top +(linha*( h + spac_y))
    return sprite.subsurface((x,y),(w , h))


def load_image(img_set,x,y):
    imag_orig = img_set.subsurface((x,y),(16,16))
    scales = pygame.transform.scale(imag_orig,(BLOC_WIDTH,BLOC_HEIGHT))
    return scales

img_parede = load_image(sprite_fundo,48,0)
img_grama = load_image(sprite_fundo,16,16)



def desenha_imagem(map,caracter_image):
    for id_linha,linha in enumerate(map):
        for id_coluna,caracter in enumerate(linha):
            if caracter in caracter_image:
                x = id_coluna * BLOC_WIDTH
                y = id_linha *BLOC_HEIGHT
                img = caracter_image[caracter]
                tela.blit(img,(x,y))



class Zezin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.vel_x = 0
        self.vel_y = 0
        
        self.index = 0
        self.caminhando_baixo=[1,2,3]
        self.caminhando_direida = [9,10,11]
        self.caminhando_esquerda = [5,6,7]
        self.caminhando_cima = [13,14,15]
        self.parado_baixo =[0]
        self.parado_direita =[8]
        self.parado_esquerda = [4]
        self.parado_cima =[12]
        
        self.image =self.get_image(0)
        self.rect = pygame.Rect((32,32),(32,48))
        self.frames = self.parado_baixo
    
    
    
    def get_image(self,gid):
        img=get_frame_by_gid(sprite=sprite_sheet,gid=gid,columns=4,w=32,h=48,spac_h=0,
                         spac_y=0,margin_left =0, margin_top=0)
        return img
 

    def update(self):

        self.index+=0.25
        if self.index >= len(self.frames):
            self.index = 0
       
        gid = self.frames[int(self.index)]
        self.image = self.get_image(gid)

        self.rect.move_ip(self.vel_x,self.vel_y)

    def tratareventos(self,e):
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                self.vel_y = 5
                self.frames = self.caminhando_baixo

            if e.key == pygame.K_UP:
                self.vel_y = - 5
                self.frames = self.caminhando_cima

            if e.key == pygame.K_LEFT:
                self.vel_x = - 5
                self.frames = self.caminhando_esquerda


            if e.key == pygame.K_RIGHT:
                self.vel_x = 5
                self.frames = self.caminhando_direida
        


        if e.type == pygame.KEYUP:
            if e.key == pygame.K_DOWN:
                self.vel_y = 0
                self.frames = self.parado_baixo

            if e.key == pygame.K_UP:
                self.vel_y = 0
                self.frames = self.parado_cima

            if e.key == pygame.K_LEFT:
                self.vel_x = 0
                self.frames = self.parado_esquerda


            if e.key == pygame.K_RIGHT:
                self.vel_x = 0
                self.frames = self.parado_direita







zezin = Zezin()
group = pygame.sprite.Group(zezin)


relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    desenha_imagem(lista_mapa,{"p": img_parede, " ":img_grama })
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    
        zezin.tratareventos(event)
    
    
    
    group.draw(tela)
    group.update()
    
    pygame.display.flip()