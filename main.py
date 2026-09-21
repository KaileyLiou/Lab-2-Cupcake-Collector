import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Lab 2: Cupcake Collector")
clock = pygame.time.Clock()

score = 0
font = pygame.font.Font(None, 40)

player_image = pygame.image.load("assets/player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (120, 120))

player_x = 20
player_y = 640
player_dy = 0

player_width = 120
player_height = 120

gravity = 0.5
jump_speed = -10
on_ground = True

platforms = [
    pygame.Rect(0, 765, 1200, 35), # ground
    pygame.Rect(150, 660, 180, 30),
    pygame.Rect(480, 590, 150, 30),
    pygame.Rect(250, 480, 160, 30),
    pygame.Rect(600, 400, 140, 30),
    pygame.Rect(900, 470, 170, 30),
    pygame.Rect(750, 300, 130, 30),
    pygame.Rect(400, 230, 150, 30),
    pygame.Rect(150, 150, 160, 30),
    pygame.Rect(550, 110, 200, 30),
]

cupcake_image = pygame.image.load("assets/cupcake.png").convert_alpha()
cupcake_image = pygame.transform.scale(cupcake_image, (70, 70))

cupcake2_image = pygame.image.load("assets/cupcake2.png").convert_alpha()
cupcake2_image = pygame.transform.scale(cupcake2_image, (70, 70))

cupcakes = [
    pygame.Rect(850, 700, 70, 70),
    pygame.Rect(200, 595, 70, 70),
    pygame.Rect(520, 525, 70, 70),
    pygame.Rect(650, 335, 70, 70),
    pygame.Rect(790, 235, 70, 70),
    pygame.Rect(450, 165, 70, 70),
    pygame.Rect(190, 85, 70, 70),
]

cupcakes2 = [
    pygame.Rect(300, 415, 70, 70),
    pygame.Rect(950, 405, 70, 70),
    pygame.Rect(620, 45, 70, 70),
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

    player_x = max(0, min(player_x, 1200 - player_width))

    if keys[pygame.K_UP] and on_ground:
        player_dy = jump_speed
        on_ground = False

    player_dy += gravity
    player_y += player_dy

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    on_ground = False

    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_dy >= 0 and player_rect.top < platform.top:
                # falling onto the platform from above
                player_y = platform.top - player_height
                player_dy = 0
                on_ground = True
            elif player_dy < 0 and player_rect.bottom > platform.bottom:
                # bumping from below
                player_y = platform.bottom
                player_dy = 0

            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # cupcake collision detection
    for cupcake in cupcakes[:]:
        if player_rect.colliderect(cupcake):
            cupcakes.remove(cupcake)
            score += 1

    for cupcake in cupcakes2[:]:
        if player_rect.colliderect(cupcake):
            cupcakes2.remove(cupcake)
            score += 2

    screen.fill((255, 249, 166))

    for platform in platforms:
        pygame.draw.rect(screen, (83, 145, 117), platform)

    for cupcake in cupcakes:
        screen.blit(cupcake_image, (cupcake.x, cupcake.y))

    for cupcake in cupcakes2:
        screen.blit(cupcake2_image, (cupcake.x, cupcake.y))

    screen.blit(player_image, (player_x, player_y))

    score_text = font.render(f"Score: {score}", True, (184, 37, 110))
    screen.blit(score_text, (30, 30)) 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()