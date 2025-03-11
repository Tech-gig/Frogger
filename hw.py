from pygame import *

init() #Initialize Pygame 
width, height = 600, 400
screen = display.set_mode((width, height))
display.set_caption("Frogger-Game")

# Load images
PictureFrog = image.load("frog.png")
PictureFrog = transform.scale(PictureFrog, (40, 40))  # Frog size
RectFrog = Rect(280, 350, 40, 40)  # Frog's starting position

PictureCar = image.load("car.png")
PictureCar = transform.scale(PictureCar, (60, 40))  # Car size

# Create a list of moving cars
cars = [
    Rect(100, 200, 60, 40),
    Rect(300, 150, 60, 40),
    Rect(500, 250, 60, 40)
]

endGame = False
car_speed = 9  # Speed of cars

while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True
        elif e.type == KEYDOWN:
            if e.key == K_s:
                RectFrog.move_ip(0, 5)
            elif e.key == K_w:
                RectFrog.move_ip(0, -5)
            elif e.key == K_d:
                RectFrog.move_ip(5, 0)
            elif e.key == K_a:
                RectFrog.move_ip(-5, 0)

    # Move cars to the right
    for c in cars:
        c.move_ip(car_speed, 0)
        if c.left > width:  # Reset car when it leaves the screen
            c.right = 0

    # Check collision
    for c in cars:
        if c.colliderect(RectFrog):
            print("Game Over!")  # Debugging message
            endGame = True  # End game on collision

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(PictureFrog, RectFrog)  # Draw frog

    for c in cars:
        screen.blit(PictureCar, c)  # Draw moving cars

    display.update()  # Refresh screen
    time.delay(30)  # Small delay for smooth movement

quit()  # Quit pygame


