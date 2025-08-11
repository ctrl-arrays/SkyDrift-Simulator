import pygame
import math

# Initialize Pygame
pygame.init()
 
# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Airplane Simulator")

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

# Load airplane image and scale it
plane_img = pygame.image.load("airplane.png") # You need an airplane image here in the same folder
plane_img = pygame.transform.scale(plane_img, (60, 60))

# Airplane properties
x, y = WIDTH // 2, HEIGHT // 2
velocity_x, velocity_y = 0, 0
angle = 0 # In degrees
speed = 0
acceleration = 0.1
max_speed = 5
friction = 0.02

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    screen.fill(SKY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Controls
    if keys[pygame.K_UP]:
        speed += acceleration
    elif keys[pygame.K_DOWN]:
        speed -= acceleration
    else:
        # Apply friction to speed when no input 
        if speed > 0:
            speed -= friction
        elif speed < 0:
            speed += friction

    # Clamp speed
    speed = max(-max_speed, min(speed, max_speed))

    if keys[pygame.K_LEFT]:
        angle +=3 # Rotate counterclockwise
    if keys[pygame.K_RIGHT]:
        angle -= 3 # Rotate clockwise

    # Convert angle to radians for movement calculation
    rad = math.radians(angle)

    # Update velocity based on speed and angle
    velocity_x = -math.sin(rad) * speed
    velocity_y = -math.cos(rad) * speed

    # Update position
    x += velocity_x
    y += velocity_y

    # Screen wrap around
    if x > WIDTH:
        x = 0
    elif x < 0:
        x = WIDTH
    if y > HEIGHT:
        y = 0
    elif y < 0:
        y = HEIGHT

    # Rotate the plane image
    rotated_plane = pygame.transform.rotate(plane_img, angle)

    # Get the rect of the rotated image to center it properly
    rect = rotated_plane.get_rect(center=(x, y))

    # Draw the plane
    screen.blit(rotated_plane, rect.topleft)

    # Display speed info
    font = pygame.font.SysFont(None, 24)
    speed_text = font.render(f"Speed: {speed:.2f}", True, (0, 0, 0))
    screen.blit(speed_text, (10, 10))

    pygame.display.flip()

pygame.quit()
