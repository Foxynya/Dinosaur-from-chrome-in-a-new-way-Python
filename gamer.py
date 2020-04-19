
import pygame
import random
pygame.init()

aqua = (0, 255, 255)  # морская волна
black = (0, 0, 0)  # черный
blue = (0, 0, 255)  # синий
fuchsia = (255, 0, 255)  # фуксия
gray = (128, 128, 128)  # серый
green = (0, 128, 0)  # зеленый
lime = (0, 255, 0)  # цвет лайма
maroon = (128, 0, 0)  # темно-бордовый
navy_blue = (0, 0, 128)  # темно-синий
olive = (128, 128, 0)  # оливковый
purple = (128, 0, 128)  # фиолетовый
red = (255, 0, 0)  # красный
silver = (192, 192, 192)  # серебряный
teal = (0, 128, 128)  # зелено-голубой
white = (255, 255, 255)  # белый
yellow = (255, 255, 0)  # желтый

fontObj1 = pygame.font.Font(None, 30)

FPS = 60

display_width = 1280
display_height = 720
display = pygame.display.set_mode((display_width, display_height))

class Box:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= self.width * -1:
            #pygame.draw.rect(display, (0, 200, 0), (self.x, self.y, self.width, self.height))
            display.blit((self.image), (self.x, self.y))
            self.x -= 4
            return True
        else:
            # self.x = display_width + 100 + random.randrange(-80, 60)
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit((self.image), (self.x, self.y))




usr_walk = [pygame.image.load('usr_walk-0.png'), pygame.image.load('usr_walk-1.png'), pygame.image.load('usr_walk-2.png'), pygame.image.load('usr_walk-3.png')]

usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 129

anim_count_between = 0
anim_count = 0

box_width = 20
box_height = 70
box_x = display_width - 50
box_y = display_height - box_height - 100

FPSclock = pygame.time.Clock()

is_jump = False
jump_count = 30
jump_count1 = 30

bg_image = pygame.image.load('bg1.png')

box_image = [pygame.image.load('box1.png'), pygame.image.load('box1.png'), pygame.image.load('box1.png'), pygame.image.load('box1.png')]

box_options = [54, 555, 54, 555, 54, 555, 54, 555]

pygame.display.set_caption("BOX")

def run_game():
    global is_jump
    global anim_count
    global anim_count_between
    game = True
    box_arr = []
    create_box_arr(box_arr)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            is_jump = True
        if is_jump:
            jump()
        if keys[pygame.K_ESCAPE]:
            pause()

        display.blit((bg_image), (0, 0))
        draw_array(box_arr)

        #pygame.draw.rect(display, (0, 0, 255), (usr_x, usr_y, usr_width, usr_height))
        draw_character()


        #pygame.display.set_caption(str(box_arr))
        if check_collision(box_arr):
            game = False
            #game_over()

        pygame.display.update()
        FPSclock.tick(FPS)
    return game_over()


def game_over():
    global fontObj
    global anim_count_between
    global anim_count
    global usr_y

    stopped_number_between = 0
    stopped_number_between_2 = 0
    stopped_str1_text = "GAME OVER"
    stopped_str2_text = "Press enter to restart"
    stopped_str3_text = "or escape to exit"

    stopped_str1_text1 = fontObj1.render(stopped_str1_text, True, black)
    stopped_str2_text1 = fontObj1.render(stopped_str2_text, True, black)
    stopped_str3_text1 = fontObj1.render(stopped_str3_text, True, black)
    stopped_str1_text2 = fontObj1.render(stopped_str1_text, True, (50, 50, 50))
    stopped_str2_text2 = fontObj1.render(stopped_str2_text, True, (50, 50, 50))
    stopped_str3_text2 = fontObj1.render(stopped_str3_text, True, (50, 50, 50))
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display.blit((bg_image), (0, 0))
        display.blit((usr_walk[anim_count]), (usr_x, usr_y))

        if stopped_number_between == 0:
            display.blit(stopped_str1_text1, [390, 240])
            display.blit(stopped_str2_text1, [350, 270])
            display.blit(stopped_str3_text1, [373, 300])
        if stopped_number_between == 1:
            display.blit(stopped_str1_text2, [390, 240])
            display.blit(stopped_str2_text2, [350, 270])
            display.blit(stopped_str3_text2, [373, 300])

        stopped_number_between_2 += 1

        if stopped_number_between_2 >= 15:
            stopped_number_between_2 = 0
            stopped_number_between += 1
        if stopped_number_between == 2:
            stopped_number_between = 0
            stopped_number_between_2 = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            stopped = False
            run_game()
        else:
            stopped = True
        if keys[pygame.K_ESCAPE]:
            stopped = False
            quit()
        pygame.display.update()
        FPSclock.tick(15)

def jump():
    global usr_y, jump_count, is_jump
    if jump_count >= -30:
        usr_y -= jump_count / 2.40
        jump_count -= 1
    else:
        jump_count = 30
        is_jump = False

def create_box_arr(array):
    choice = random.randrange(0, 1)
    image = box_image[choice]
    width = box_options[choice * 2]
    height = box_options[choice * 2 + 1]
    array.append(Box(display_width + 20, height, width, image, 4))

    choice = random.randrange(0, 1)
    image = box_image[choice]
    width = box_options[choice * 2]
    height = box_options[choice * 2 + 1]
    array.append(Box(display_width + 20, height, width, image, 4))

    choice = random.randrange(0, 1)
    image = box_image[choice]
    width = box_options[choice * 2]
    height = box_options[choice * 2 + 1]
    array.append(Box(display_width + 20, height, width, image, 4))
    #array.append(Box(display_width + 300, display_height - 45 - 120, 54, 45, 4))
    #array.append(Box(display_width + 600, display_height - 45 - 120, 54, 45, 4))
    return array

def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)
    return radius

def draw_array(array):
    for box in array:
        check = box.move()
        if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 1)
            image = box_image[choice]
            width = box_options[choice * 2]
            height = box_options[choice * 2 + 1]

            box.return_self(radius, height, width, image)

def draw_character():
    global anim_count_between
    global anim_count
    global usr_y
    display.blit((usr_walk[anim_count]), (usr_x, usr_y))

    anim_count_between += 1

    if anim_count_between == 8 and usr_y == display_height - usr_height - 129:
        anim_count_between = 0
        anim_count += 1
    if usr_y > display_height - usr_height - 129 or usr_y < display_height - usr_height - 129:
        anim_count = 0
        anim_count_between = 0
    if anim_count == len(usr_walk):
        anim_count = int(0)

def pause():
    global fontObj
    global anim_count_between
    global anim_count
    global usr_y

    paused = True
    pause_number_between = 0
    pause_number_between_2 = 0
    pause_str1_text = "Pause"
    pause_str2_text = "Press enter to continue"

    pause_str1_text1 = fontObj1.render(pause_str1_text, True, black)
    pause_str2_text1 = fontObj1.render(pause_str2_text, True, black)
    pause_str1_text2 = fontObj1.render(pause_str1_text, True, (50, 50, 50))
    pause_str2_text2 = fontObj1.render(pause_str2_text, True, (50, 50, 50))

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit((bg_image), (0, 0))
        display.blit((usr_walk[anim_count]), (usr_x, usr_y))

        if pause_number_between == 0:
            display.blit(pause_str1_text1, [330, 240])
            display.blit(pause_str2_text1, [250, 270])
        if pause_number_between == 1:
            display.blit(pause_str1_text2, [330, 240])
            display.blit(pause_str2_text2, [250, 270])

        pause_number_between_2 += 1

        if pause_number_between_2 >= 15:
            pause_number_between_2 = 0
            pause_number_between += 1
        if pause_number_between == 2:
            pause_number_between = 0
            pause_number_between_2 = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        else:
            paused = True
        pygame.display.update()
        FPSclock.tick(15)

def check_collision(barriers):
    for barrier in barriers:
        if usr_y + usr_height >= barrier.y:
            if barrier.x <= usr_x <= barrier.x + barrier.width:
                return True
            elif barrier.x <= usr_x + usr_width <= barrier.x + barrier.width:
                return True
    return False
while run_game():
    pass
pagame.quit()
quit()
