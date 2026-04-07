import pygame
import math

# 1. Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 2. Set Starting Positions
player_pos = [400, 300]
cat_pos = [100, 100]

running = True
while running:
    # 3. Handle Keyboard Inputs (WASD)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_pos[1] -= 5
    if keys[pygame.K_s]: player_pos[1] += 5
    if keys[pygame.K_a]: player_pos[0] -= 5
    if keys[pygame.K_d]: player_pos[0] += 5

    # 4. Realistic Cat AI: Calculate distance to player
    dx, dy = player_pos[0] - cat_pos[0], player_pos[1] - cat_pos[1]
    dist = math.hypot(dx, dy)
    
    if dist < 200: # If player is close, cat chases
        cat_pos[0] += (dx/dist) * 2
        cat_pos[1] += (dy/dist) * 2
        
        if dist < 50: # If very close, it "hisses" (logic for sound goes here)
            print("Hiss!") 

    # 5. Draw everything to the screen
    screen.fill((50, 50, 50)) # Grey background
    pygame.draw.circle(screen, (0, 255, 0), player_pos, 15) # Green circle (Player)
    pygame.draw.rect(screen, (150, 150, 150), (cat_pos[0], cat_pos[1], 30, 30)) # Grey box (Cat)
    
    pygame.display.flip()
    clock.tick(60) # Run at 60 frames per second

pygame.quit()
