from pygame import *
from random import *
from time import *
font.init()
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)
screen = display.set_mode((600,400))

# clock = time.Clock()

screen.fill(LIGHT_BLUE)
style = font.Font(None, 40)


# TIMER NOT COUNTING
# FIRST CARD NOT WORKING


class Area():
    def __init__(self, x = 0, y = 0, width = 0, height = 0, color = None):
        self.rect = Rect(x,y,width,height)
        self.color = color
    def set_color(self, fill):
        self.color = fill
    def rectangle(self):
        draw.rect(screen, self.color, self.rect)
    def border_rectangle(self, color, thickness):
        draw.rect(screen, color, self.rect, thickness)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)

class Label(Area):
    def set_text(self, text, fsize, text_color):
        self.text = font.Font(None, fsize).render(text, True, text_color)
    def draw(self, padding_x, padding_y):
        self.rectangle()
        screen.blit(self.text,(self.rect.x + padding_x, self.rect.y + padding_y))

cards = []
x = 20

for i in range(5):
    card = Label(x,150, 70, 90, YELLOW)
    card.border_rectangle(DARK_BLUE, 10)
    card.set_text("Click", 30, (0,0,0))
    cards.append(card)
    x += 100

time_text = Label(40, 10, 80,80, LIGHT_BLUE)
time_text.set_text("Time",40, BLACK)
time_text.draw(0,0)

point_text = Label(390, 10, 80,80, LIGHT_BLUE)
point_text.set_text("Point", 40, BLACK)
point_text.draw(0,0)


time_counter = Label(60, 40, 80,80, LIGHT_BLUE)
time_counter.set_text("",40, BLACK)
time_counter.draw(0,0)

point_counter = Label(410, 40, 80,80, LIGHT_BLUE)
point_counter.set_text("0", 40, BLACK)
point_counter.draw(0,0)

start_time = time()
current_time = start_time

points = 0
wait = 0
run = True
while run:
    if wait == 0:
        wait = 50
        click = randint(1, 5)
        for i in range(5):
            cards[i].set_color(YELLOW)
            if (i+1) == click:
                cards[i].draw(10, 40)
            else:
                    cards[i].rectangle()
    else:
        wait -= 1
    
    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x,y = e.pos

            for i in range(1,5):
                if cards[i].collidepoint(x,y):
                    if (i + 1) == click:
                        cards[i].set_color(GREEN)
                        points += 1
                    else:
                        cards[i].set_color(RED)
                        points -= 1

                    cards[i].rectangle()
                    point_counter.set_text(str(points), 40,BLACK)
                    point_counter.draw(0,0)

    new_time = time()

    if int(new_time) - int(current_time) >= 1:
        time_counter.set_text(str(int(new_time - current_time)), 40, BLACK)
        time_counter.draw(0,0)
        current_time = new_time

# Game condition
    if points >= 2:
        win_text = Label(0, 0, 500,1000, GREEN)
        win_text.set_text("YOU WIN!!!", 80, BLACK)
        win_text.draw(0,0)
        win_time = Label(200, 200, 200,100, GREEN)
        win_time.set_text("It took you " + str(int(new_time - current_time)), 50, BLACK)
        win_time.draw(0,0)
    
    if int(new_time - current_time) >= 15:
        lose_text = Label(0, 0, 500, 1000, RED)
        lose_text.set_text("YOU LOSE", 80, BLACK)
        lose_text.draw(100,200)
        




    display.update()
    # time.delay(50)
