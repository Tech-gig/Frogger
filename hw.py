from pygame import *

init() #Sets the window 
width = 600 
height = 400
screen = display.set_mode((width, height)) #Initialize a window for screen display 
display.set_caption('Frogger-Game ') #Set title of window 
endGame = False
PictureFrog = image.load("frog.png")
PictureFrog = transform.scale(PictureFrog,(40,40))#Sets the measurement for picture 
RectFrog = Rect(100,0,40,40)#Draws a rectangle to the screen 
PictureCar = image.load("car.png")
PictureCar = transform.scale(PictureCar, (50,50))
cars = []
cars.append(Rect(200,200,40,40))


while endGame == False:
	for e in event.get(): # It is the gameloop 
		if e.type == QUIT:
			endGame = True #This quits the game 
		elif e.type == KEYDOWN:
			if e.key == K_s:
				RectFrog.move_ip(0,5)
			elif e.key == K_w:
				RectFrog.move_ip(0,-5)
			elif e.key == K_d:
				RectFrog.move_ip(5,0)
			elif e.key == K_a:
				RectFrog.move_ip(-5,0)
	for c in cars:
		if c.colliderect(RectFrog):
			endGame=True 
				
				
				
				
	screen.fill((0,0,0))
	for c in cars:
		draw.rect(screen, (255,255,255), c)
	screen.blit(PictureFrog, RectFrog)
	display.update()#Updates portions of screen for software updates 
	time.delay(30)
    
    

