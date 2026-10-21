import pygame, random, time
pygame.init()

screen_width=900
screen_height=700

screen=pygame.display.set_mode((screen_width,screen_height))

def change_background():
    background=pygame.image.load('bground.png')
    background=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(background,(0,0))

class Bin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('bin.png')
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):

    def __init__(self,img):
        super().__init__()

        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('plastic.png')
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

bin=Bin()
allsprites.add(bin)

images = ['item1.png', 'item2.png', 'item3.png']

for i in range(50):
    item=Recyclable(random.choice(images))

    item.rect.x=random.randrange(screen_width)
    item.rect.y=random.randrange(screen_height)

    item_list.add(item)
    allsprites.add(item)

for i in range(20):
    plastic=Non_recyclable()

    plastic.rect.x=random.randrange(screen_width)
    plastic.rect.y=random.randrange(screen_height)

    plastic_list.add(plastic)
    allsprites.add(plastic)

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)

playing=True
score=0

clock=pygame.time.Clock()
start_time = time.time()

#font to print score on screen
myFont = pygame.font.SysFont("Times New Roman",22)
text = myFont.render('Score='+ str(0),True,BLACK)

while playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False

    time_elapse=time.time()-start_time
    if time_elapse>=60:

        if score>=20:
            screen.fill(GREEN)
            text1=myFont.render('Bin loot successful.',True,BLACK)
        else:
            screen.fill(RED)
            text1=myFont.render('Bin loot unsuccessful. Better luck next time!',True,BLACK)

        screen.blit(text1,(250,40))