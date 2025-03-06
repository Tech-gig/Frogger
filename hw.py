from pygame import *

init() #Sets the window 
width = 600 
height = 400
screen = display.set_mode((width, height)) #Initialize a window for screen display 
display.set_caption('Frogger-Game ') #Set title of window 
endGame = False
PictureFrog = image.load("frog.png")
PictureFrog = transform.scale(PictureFrog,(40,40))#Sets the measurement for picture 
RectFrog = Rect(100,0,40,40)

while endGame == False:
	for e in event.get(): # It is the gameloop 
		if e.type == QUIT:
			endGame = True
		elif e.type == KEYDOWN:
			if e.key == K_s:
				RectFrog.move_ip(0,5)
			elif e.key == K_w:
				RectFrog.move.ip(0,-5)
			elif e.key == K_d:
				RectFrog.move_ip(5,0)
			elif e.key == K_a:
				RectFrog.move_ip(-5,0)
				
				
				
				
	screen.fill((0,0,0))
	draw.rect(screen, (255,255,255), (0,0,width,20))
	screen.blit(PictureFrog, RectFrog)
	display.update()#Updates portions of screen for software updates 
	time.delay(30)
    
    

