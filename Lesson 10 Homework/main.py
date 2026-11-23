import pygame,random,time
pygame.init()

global text1

screen_height=900
screen_width=700

screen=pygame.display.set_mode((screen_width,screen_height))

def change_background():
    background=pygame.image.load('background.png')
    background=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(background,(0,0))

class Chest(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('chest.png')
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Treasure(pygame.sprite.Sprite):

    def __init__(self,img):
        super().__init__()

        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

class Garbage(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image=pygame.image.load('can.png')
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

treasure_list=pygame.sprite.Group()
garbage_list=pygame.sprite.Group()
allthings=pygame.sprite.Group()

chest=Chest()
allthings.add(chest)

treasures = ['pearl.png','coin.png','diamond.png']

for i in range(50):
    treasure=Treasure(random.choice(treasures))

    treasure.rect.x=random.randrange(screen_width)
    treasure.rect.y=random.randrange(screen_height)

    treasure_list.add(treasure)
    allthings.add(treasure)

for i in range(20):
    can=Garbage()

    can.rect.x=random.randrange(screen_width)
    can.rect.y=random.randrange(screen_height)

    garbage_list.add(can)
    allthings.add(can)

score=0
myFont = pygame.font.SysFont('Times New Roman',22)

clock=pygame.time.Clock()
start_time = time.time()
display_score = myFont.render('Score=' + str(0),True,'black')

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    time_elapse=time.time()-start_time
    if time_elapse>=60:

        if score>=20:

            screen.fill('green')
            end_text=myFont.render('Treasure Loot Successful! Good Job!',True,'black')

        else:
            screen.fill('red')
            end_text=myFont.render('Treasure Loot Unsuccessful! Better Luck Next Time!',True,'black')

        screen.blit(end_text,(10,20))

    else:
        change_background()
        countdown=myFont.render('Time Left: ' + str(60 - int(time_elapse)),True,'black')
        screen.blit(countdown,(10,20))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if chest.rect.y >0:
                chest.rect.y-=5

        if keys[pygame.K_DOWN]:
            if chest.rect.y <screen_height:
                chest.rect.y+=5

        if keys[pygame.K_RIGHT]:
            if chest.rect.x <screen_width:
                chest.rect.x+=5

        if keys[pygame.K_LEFT]:
            if chest.rect.x >0:
                chest.rect.x-=5

        treasure_hit_list=pygame.sprite.spritecollide(chest, treasure_list, True)
        for treasure in treasure_hit_list:
            score +=1
            text1 = myFont.render('Score = ' + str(score),True,'black')
            
        garbage_hit_list=pygame.sprite.spritecollide(chest, garbage_list, True)
        for garbage in garbage_hit_list:
            score -=5
            text1 = myFont.render('Score = ' + str(score),True,'black')

    #screen.blit(text1 ,(20,50))
    allthings.draw(screen)
    pygame.display.update()

pygame.quit()