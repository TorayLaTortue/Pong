import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

score = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
balle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
balle_force = pygame.Vector2(200, 200)
multiplicateurForce = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    police = pygame.font.SysFont("monospace", 15)
    image_texte = police.render("texte uwu", 1 ,(255,0,0))
    screen.blit(image_texte, (320,240))
    pygame.display.flip()
    
    rect1 = pygame.draw.rect(screen, "black", pygame.Rect(10, player_pos.y, 20, 80))
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_z] and player_pos.y > 0:
        player_pos.y -= 600 * dt
            
    if keys[pygame.K_s]and player_pos.y < 660:
        player_pos.y += 600 * dt
        
    rect2 = pygame.draw.rect(screen, "black", pygame.Rect(1250, player_pos2.y, 20, 80))
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and player_pos2.y > 0:
        player_pos2.y -= 600 * dt
    
    if keys[pygame.K_DOWN] and player_pos2.y < 660:
        player_pos2.y += 600 * dt
        
    circle = pygame.draw.circle(screen, "red", balle_pos, 10)
    
    balle_pos.x += balle_force.x * dt
    balle_pos.y += balle_force.y * dt
    
    
    
    #rebond sur le pong (Gauche et droite)
    if circle.colliderect(rect1):
        balle_force.x = 200 * multiplicateurForce
        multiplicateurForce += 0.01
        score += 1
    if circle.colliderect(rect2):
        balle_force.x = -200 * multiplicateurForce
        multiplicateurForce += 0.01
        score += 1
    
    #Rebond plafond et bas
    if balle_pos.y > 700:
        balle_force.y = -200
    if balle_pos.y < 0:
        balle_force.y = 200
        
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    if keys[pygame.K_ESCAPE]:
        running = False