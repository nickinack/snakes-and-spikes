
import pygame
import random
import time
from config import *

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Spikes!")
clock = pygame.time.Clock()

# Sprite 1


class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30, 20))
		self.rect = self.image.get_rect()
		self.image = pygame.image.load("rabbit.png")
		self.image = pygame.transform.rotate(self.image, 90)
		self.image1 = pygame.transform.smoothscale(self.image, (40, 80))
		screen.blit(self.image1, self.rect)
		self.rect.centerx = WIDTH/2
		self.rect.bottom = HEIGHT-20
		self.speedx = 0

	def update(self):
		self.speedx = 0
		self.speedy = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -5
		if keystate[pygame.K_RIGHT]:
			self.speedx = 5
		if keystate[pygame.K_UP]:
			self.speedy = -5
		if keystate[pygame.K_DOWN]:
			self.speedy = 5
		if self.rect.right > WIDTH :
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0 :
			self.rect.top = 0
		if self.rect.bottom > HEIGHT :
			self.rect.bottom = HEIGHT
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		self.score = 0



#Sprite set 1
class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 20))
		self.rect = self.image.get_rect()
		self.image = pygame.image.load("Snake.png")
		screen.blit(self.image,self.rect)

		self.rect.x = random.randrange(0, 10)
		self.rect.y = 500

		self.speedx = random.randrange(2, 4)

	def update(self):
		self.rect.x += self.speedx


#Sprite set 2
class Mob1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 20))
		self.rect = self.image.get_rect()
		self.rect = self.image.get_rect()
		self.image = pygame.image.load("Snake.png")
		self.rect.x = (random.randrange(0, 10))
		self.rect.y = 300

		self.speedx = random.randrange(2, 4)

	def update(self):
		self.rect.x += self.speedx
#Static Sprite



#Sprite set 3
class Mob2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 20))
		self.rect = self.image.get_rect()
		self.rect = self.image.get_rect()
		self.image = pygame.image.load("Snake.png")
		self.rect.x = random.randrange(0, 10)
		self.rect.y = 100

		self.speedx = random.randrange(2, 4)
	def update(self):
		self.rect.x +=self.speedx

#Static Sprites
class Mob_static(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((20, 30))
		self.rect = self.image.get_rect()
		self.image = pygame.image.load("Spike.png")
		self.image1 = pygame.transform.smoothscale(self.image , (40, 80))
		screen.blit(self.image1,self.rect)
		self.rect.x = random.randrange(1, WIDTH-self.rect.right)
		self.rect.y = 400

class Mob_static1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((20, 30))
		self.rect = self.image.get_rect()
		self.image = pygame.image.load("Spike.png")
		self.image1 = pygame.transform.smoothscale(self.image , (40, 80))
		screen.blit(self.image1,self.rect)
		self.rect.x = random.randrange(1, WIDTH-self.rect.right)
		self.rect.y = 200
font_name = pygame.font.match_font('comicsans')
def draw_text(surf,text,size,x,y):
	font = pygame.font.Font(font_name,size)
	text_surface = font.render(text,True,WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surf.blit(text_surface , text_rect)


class Tile1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((WIDTH, 30))
		self.rect  = self.image.get_rect()
		self.image.fill(GREEN)
		self.rect.y = 100

class Tile2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((WIDTH, 30))
		self.rect  = self.image.get_rect()
		self.image.fill(GREEN)
		self.rect.y = HEIGHT-100

class Tile3(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((WIDTH, 30))
		self.rect  = self.image.get_rect()
		self.image.fill(GREEN)
		self.rect.top = WIDTH/2 + 60

class Tile4(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((WIDTH, 30))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.top = WIDTH/2 + 166

class Tile5(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((WIDTH, 30))
		self.rect  = self.image.get_rect()
		self.image.fill(BROWN)
		self.rect.top = WIDTH/2 - 35


#Sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
mobs_static = pygame.sprite.Group()


list = []
player = Player()
list.append(player)
tile = Tile1()
tile1 = Tile2()
tile2 = Tile3()
tile3 = Tile4()
tile4 = Tile5()


all_sprites.add(tile)
all_sprites.add(tile1)
all_sprites.add(tile2)
all_sprites.add(tile3)
all_sprites.add(tile4)
all_sprites.add(player)

for x in range(6):
	m = Mob_static()
	all_sprites.add(m)
	mobs_static.add(m)
for x in range(6):
	m = Mob_static1()
	all_sprites.add(m)
	mobs_static.add(m)
running = True

pygame.time.set_timer(create_mobs, 550)
pygame.time.set_timer(score_down, 1000)
grass = pygame.image.load("grass.png")
flag = 0
flag1 = 0
score1 = 500
score = 500
counter = 0
kill = 0
kill_1 = 0
kill1 = 0
kill1_1 = 0





while running:



	clock.tick(FPS)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type ==  create_mobs:

			m = Mob2()
			all_sprites.add(m)
			mobs.add(m)


			m = Mob1()
			all_sprites.add(m)
			mobs.add(m)

			m = Mob()
			all_sprites.add(m)
			mobs.add(m)


		if event.type == score_down:
			if (flag == 0 and flag1 == 0) or (flag == 1 and flag1 == 1) or (flag == 2 and flag1 == 2):
				score1 = score1 -1

			if (flag == 1 and flag1 == 0) or (flag ==1 and flag1 == 0) or (flag == 2 and flag1 == 1) or (flag == 3 and flag1 == 2):
				score = score - 1





	print(str(flag) + " " + str(flag1))





	if flag == 0:
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				if player.rect.top <= 0 and counter >=0 :
					player.image = pygame.transform.rotate(player.image,180)

					counter = counter + 1
					flag = 1
					score1 += 30


	if flag1 == 0 and flag == 1:
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				if player.rect.bottom >=HEIGHT  :
					player.image = pygame.transform.rotate(player.image,180)
					flag1 = 1
					score += 30



	if flag == 1 and flag1 == 1:
		for i in mobs:
			i.speedx = random.randrange(3,6)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				if player.rect.top <= 0 and counter >=0 :
					player.image = pygame.transform.rotate(player.image,180)
					counter = counter + 1
					flag = 2
					score1 += 30


	if flag == 2 and flag1 == 1:
		for i in mobs:
			i.speedx = random.randrange(3,6)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				if player.rect.bottom >=HEIGHT :
					player.image = pygame.transform.rotate(player.image,180)
					flag1 = 2
					score += 30


	if flag == 2 and flag1 == 2:
		for i in mobs:
			i.speedx = random.randrange(7,10)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				if player.rect.top <= 0 and counter >=0 :
					player.image = pygame.transform.rotate(player.image,180)
					counter = counter + 1
					flag = 3
					score1 += 30


	if flag == 3 and flag1 ==2 :
		for i in mobs:
			i.speedx = random.randrange(7,10)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				if player.rect.bottom >=HEIGHT :
					player.image = pygame.transform.rotate(player.image,180)
					flag1 = 3
					score += 30


	if flag == 3 and flag1 == 3:
		running = False

	hits = pygame.sprite.spritecollide(player,mobs,False)
	hits1 = pygame.sprite.spritecollide(player,mobs_static,False)





	if hits or hits1:


		if flag == 0 and flag1 == 0 :

			print("Hey")
			player.kill()
			player = Player()
			player.image = pygame.transform.rotate(player.image,180)
			all_sprites.add(player)

			player.rect.top = 0
			flag = 1
			score1 = score1 - 100
			kill=1



		elif flag == 1 and flag1 == 0 :
			kill1=1
			player.kill()
			player = Player()
			all_sprites.add(player)

			player.rect.bottom = HEIGHT-10
			flag1 = 1
			score = score - 100


		elif flag == 1 and flag1 == 1:

			player.kill()
			player = Player()
			all_sprites.add(player)
			player.image = pygame.transform.rotate(player.image,180)

			player.rect.top = 0
			flag= 2
			score1 = score1 - 100

			kill_1 = 1


		elif flag == 2 and flag1 == 1:

			player.kill()
			player = Player()
			all_sprites.add(player)

			flag1 = 2


			player.rect.bottom = HEIGHT-10
			score = score - 100
			kill1_1 = 2


		elif flag == 2 and flag1 == 2:
			player.kill()
			player = Player()
			all_sprites.add(player)
			player.image = pygame.transform.rotate(player.image,180)

			player.rect.top = 0
			score1 = score1 - 100
			flag= 3



		elif flag == 3 and flag1 ==2:
			player.kill()
			player = Player()
			all_sprites.add(player)


			player.rect.bottom = HEIGHT-10
			score = score - 100
			flag1 = 3





	all_sprites.update()


	for x in range(int(HEIGHT/grass.get_width()+2)):
	        for y in range(int(WIDTH/grass.get_height()+2)):
	            screen.blit(grass,(x*100,y*100))


	all_sprites.draw(screen)
	draw_text(screen,"Player1: " + str(score1),18,WIDTH/2,10)
	draw_text(screen,"Player2: " + str(score),18,WIDTH/2,HEIGHT-20)
	if (flag == 0 and flag1 == 0) or (flag == 1 and flag1 == 1) or (flag == 2 and flag1 == 2):
		screen.blit(textsurface_1,(0,0))
	if (flag == 1 and flag1 == 0) or (flag ==1 and flag1 == 0) or (flag == 2 and flag1 == 1) or (flag == 3 and flag1 == 2):
		screen.blit(textsurface_2,(0,0))
	pygame.display.flip()

	for all in mobs:
		if all.rect.left > WIDTH:
			all.kill()

time.sleep(1)


myfont = pygame.font.SysFont('comicsans', 30)
if score>score1:
	textsurface = myfont.render('Player2 Won with score:', False, (255, 255, 255))
	textsurface1 = myfont.render(str(score), False, (255, 255, 255))

if score1>score:
	textsurface = myfont.render('Player1 Won with score:', False, (255, 255, 255))
	textsurface1 = myfont.render(str(score1), False, (255, 255, 255))
else:
	textsurface = myfont.render('Tied with score:', False, (255, 255, 255))
	textsurface1 = myfont.render(str(score1), False, (255, 255, 255))

t_end = time.time()+2
while time.time() < t_end:
	screen.fill((255,182,193))
	screen.blit(textsurface,(HEIGHT/2-170,WIDTH/2))
	screen.blit(textsurface1,(HEIGHT/2-70 , WIDTH/2+20))

	pygame.display.flip()

pygame.quit()
