from pygame import*
time=time.Clock()
FPS=60
finish=False
window=display.set_mode((700,500))
display.set_caption('Пинг-понг')
bg=transform.scale(image.load('faild.jpg'),(700,500))
speed_x=1
speed_y=1
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Player1(Gamesprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<490:
            self.rect.y+=self.speed


class Player2(Gamesprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<490:
            self.rect.y+=self.speed


class Winner(Gamesprite):
    direction='left'
    def update(self):
        if self.rect.x<=470:
            self.direction='right'

        if self.rect.x>=700-85:
            self.direction='left'
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed              


player1=Player1('8278.png_860.jpg',0,250,10)
player2=Player2('8278.png_860.jpg',600,250,10)
ball=Gamesprite('ball.png',80,250,0)
font.init()
font=font.SysFont('Arial', 70)
win=font.render('PLAYER 1 WIN', True, (151, 69, 129))
lose=font.render('PLAYER 2 WIN', True, (35, 40, 157))



'''mixer.init()
mixer.music.load('89a80930c240b92.mp3')
mixer.music.play()'''



ii=0
li=0

game=True
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False


    if finish != True:
        window.blit(bg,(0,0))
        player1.update()
        player2.update()

        player1.reset()
        player2.reset()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        i=font.render(str(ii), True,(0,0,0))
        window.blit(i,(10,0))
        l=font.render(str(li), True,(0,0,0))
        window.blit(l,(650,0))

        if ball.rect.y>500 or ball.rect.y<0:
            speed_y *= -1    
 


        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1   



        if ball.rect.x>700:
            ball.rect.x= player2.rect.x - 100
            ball.rect.y=player2.rect.y
            
            speed_x *= -1  
            ii=ii+1
            

        if ball.rect.x<0:
            ball.rect.x= player1.rect.x + 100
            ball.rect.y=player1.rect.y
            li=li+1


        if ii==11:
            window.blit(lose,(100,200))      
            finish=True
        if li==11:
            window.blit(win,(100,200)) 
            finish=True
        

        display.update()