import pygame
import sys
import math
import random

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_walk_images = [pygame.image.load("sprite_0.png"), pygame.image.load("sprite_1.png"),
                      pygame.image.load("sprite_2.png"), pygame.image.load("sprite_3.png"),
                      pygame.image.load("sprite_4.png"), pygame.image.load("sprite_5.png"),
                      pygame.image.load("sprite_6.png"), pygame.image.load("sprite_7.png"),
                      pygame.image.load("sprite_8.png")]




player_weapon = pygame.image.load("enemyAnimations/karrotgun.png")
arrow_1 = pygame.image.load("enemyAnimations/arrow2.png")
#player_weapon.set_colorkey((0, 0, 0))



class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
    def handle_weapons(self, display): #rotating gun
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)
        arrow = pygame.transform.rotate(arrow_1, angle)

        display.blit(player_weapon_copy, (self.x+26-int(player_weapon.get_width()/2), self.y+46-int(player_weapon_copy.get_height()/2)))
        display.blit(arrow, (self.x + 26 - int(arrow.get_width() / 2), self.y + 46 - int(arrow.get_height() / 2)))


    def main(self, display):

        if self.animation_count + 1 >= 81:
            self.animation_count = 0


        self.animation_count += 1

        if self.moving_right:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count // 9], (64, 64)),
                         (self.x, self.y))
        elif self.moving_left:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count // 9], True, False), (64, 64)),
                         (self.x, self.y))

        else:
            display.blit(pygame.transform.scale(player_walk_images[0], (64, 64)), (self.x, self.y))


        self.handle_weapons(display) # rotate weapon



        self.moving_right = False
        self.moving_left = False

        #pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height)) #character's properties

class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.xVel = math.cos(self.angle) * self.speed
        self.yVel = math.sin(self.angle) * self.speed
        self.image = pygame.image.load("enemyAnimations/carot.png")#stuff
    def main(self, display):
        self.x -= int(self.xVel)
        self.y -= int(self.yVel)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        player_weapon_copy = pygame.transform.rotate(self.image, angle)

        display.blit(player_weapon_copy, (
        self.x + 26 - int(player_weapon.get_width() / 2), self.y + 46 - int(player_weapon_copy.get_height() / 2)))

        #display.blit(pygame.transform.scale(self.image, (32, 32)), (self.x+26, self.y+26)) #stuff

        #pygame.draw.circle(display, (0,0,0), (self.x+26, self.y+26), 5)

class SlimeEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation_images = [pygame.image.load("enemyAnimations/sprite_00.png"), pygame.image.load("enemyAnimations/sprite_01.png"),
                                 pygame.image.load("enemyAnimations/sprite_02.png"), pygame.image.load("enemyAnimations/sprite_03.png"),
                                 pygame.image.load("enemyAnimations/sprite_04.png"), pygame.image.load("enemyAnimations/sprite_05.png"),
                                 pygame.image.load("enemyAnimations/sprite_06.png"), pygame.image.load("enemyAnimations/sprite_07.png"),
                                 pygame.image.load("enemyAnimations/sprite_08.png"), pygame.image.load("enemyAnimations/sprite_09.png")]

        self.deathAnimation = [pygame.image.load("enemyAnimations/deathAnimation/deathAnim0.png"), pygame.image.load("enemyAnimations/deathAnimation/deathAnim1.png"),
                               pygame.image.load("enemyAnimations/deathAnimation/deathAnim2.png"), pygame.image.load("enemyAnimations/deathAnimation/deathAnim3.png"), ]
        self.animation_count = 0

        self.deathAnimation_count = 0
        self.resetOffset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150)
        self.zombieHealth = 100

        self.val = 10
        self.hundred = 100

        self.facingright = False
        self.facingLeft = False

        self.deadValue = 100

    def main(self, display):



        if self.animation_count + 1 == self.hundred: #edit
            self.animation_count = 0 #edit
        self.animation_count += 1

        if self.deathAnimation_count + 1 == 16: #edit
            self.deathAnimation_count = 0 #edit
        self.deathAnimation_count += 1

        if self.resetOffset == 0:
            self.offset_x = random.randrange(-150, 150)
            self.offset_y = random.randrange(-150, 150)
            self.resetOffset = random.randrange(120, 150)
        else:
            self.resetOffset -= 1

        if player.x + self.offset_x > self.x-display_scroll[0]:
            self.x += 1
        elif player.x + self.offset_x < self.x-display_scroll[0]:
            self.x -= 1

        if player.y + self.offset_y > self.y-display_scroll[1]:
            self.y += 1
        elif player.y + self.offset_y < self.y-display_scroll[1]:
            self.y -= 1

        pygame.draw.rect(display,(0, 0, 0), (self.x-display_scroll[0] - 20, self.y-display_scroll[1], self.deadValue, 5))
        pygame.draw.rect(display, (255, 0, 0), (self.x - display_scroll[0] - 20, self.y - display_scroll[1], self.zombieHealth, 5))



        s = display.blit(pygame.transform.scale(self.animation_images[self.animation_count // self.val], (64, 64)),
                         (self.x - display_scroll[0], self.y - display_scroll[1]))





        #s = display.blit(pygame.transform.scale(self.animation_images[self.animation_count // 10], (64, 64)),
                         #(self.x - display_scroll[0], self.y - display_scroll[1]))


        #damage
        for bullet in player_bullets:
            if s.collidepoint(bullet.x, bullet.y):
                self.zombieHealth -= 1




        if self.zombieHealth <= 100 and self.zombieHealth >= 1:
            s

        else:


            self.animation_images = self.deathAnimation
            self.animation_count = self.deathAnimation_count
            self.val = 4
            self.hundred = 16

        if s.x <= player.x:
            self.facingright = True
            self.facingLeft = False
            if self.facingright == True:
                s
        elif s.x >= player.x:
            self.facingright = False
            self.facingLeft = True
            if self.facingLeft == True:
                f = display.blit(
                    pygame.transform.scale(pygame.transform.flip(self.animation_images[self.animation_count // self.val], True, False), (64, 64)),
                    (self.x - display_scroll[0], self.y - display_scroll[1]))


        if self.zombieHealth <= 0:
            self.deadValue = 0

        self.facingright = False
        self.facingLeft = False


        #display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count // 9], True, False), (64, 64)),(self.x, self.y))


enemies = [SlimeEnemy(100, 100)]



player = Player(375, 300, 32, 32)

display_scroll = [0,0]


player_bullets = []



while True:
    display.fill((24, 164, 86))

    mouse_x, mouse_y = pygame.mouse.get_pos()





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))



    keys = pygame.key.get_pressed()

    box = pygame.draw.rect(display, (255, 255, 255), (100-display_scroll[0], 100-display_scroll[1], 16, 16)) # square


    if keys[pygame.K_a]:
        display_scroll[0] -= 5

        player.moving_left = True

        for bullet in player_bullets:
            bullet.x += 5
    if keys[pygame.K_d]:
        display_scroll[0] += 5

        player.moving_right = True

        for bullet in player_bullets:
            bullet.x -= 5
    if keys[pygame.K_w]:
        display_scroll[1] -= 5

        for bullet in player_bullets:
            bullet.y += 5
    if keys[pygame.K_s]:
        display_scroll[1] += 5

        for bullet in player_bullets:
            bullet.y -= 5

    player.main(display)





    for bullet in player_bullets:
        bullet.main(display)




    for enemy in enemies:
        enemy.main(display)






    '''for bullet in player_bullets:
        for enemy in enemies:
            if display.get_at((bullet.x, bullet.y)) == (58, 188, 59):
                zombieHealth -= 5'''
    clock.tick(60)
    pygame.display.update()
