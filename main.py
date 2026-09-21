import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Lab 2: Cupcake Collector")
clock = pygame.time.Clock()

score = 0
font = pygame.font.Font(None, 40)

player_image = pygame.image.load("assets/player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (120, 120))

player_x = 50
player_y = 300
player_dy = 0

player_width = 120
player_height = 120

gravity = 0.5
jump_speed = -10
on_ground = True

platforms = [
    pygame.Rect(0, 350, 600, 50),
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20)
]

cupcake_image = pygame.image.load("assets/cupcake.png").convert_alpha()
cupcake_image = pygame.transform.scale(cupcake_image, (70, 70))

cupcakes = [
    pygame.Rect(150, 230, 70, 70),
    pygame.Rect(400, 180, 70, 70),
    pygame.Rect(520, 310, 70, 70)
]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 5

    if keys[pygame.K_RIGHT]:
        player_x += 5

    if keys[pygame.K_UP] and on_ground:
        player_dy = jump_speed
        on_ground = False

    player_dy += gravity
    player_y += player_dy

    # keep player on the ground
    if player_y >= 300:
        player_y = 300
        player_dy = 0
        on_ground = True

    # keep player inside screen
    player_x = max(0, min(player_x, 1200 - player_width))

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # cupcake collision detection
    for cupcake in cupcakes[:]:
        if player_rect.colliderect(cupcake):
            cupcakes.remove(cupcake)
            score += 1

    screen.fill((255, 249, 166))

    for platform in platforms:
        pygame.draw.rect(screen, (83, 145, 117), platform)

    for cupcake in cupcakes:
        screen.blit(cupcake_image, (cupcake.x, cupcake.y))

    screen.blit(player_image, (player_x, player_y))

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()