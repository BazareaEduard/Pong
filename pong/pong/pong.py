import pygame
import random

class Player:
    _speed = 0
    _score = 0
    _x = 0
    _y = 0
    _width = 0
    _height = 0
    def set(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    #methods
    def X(self):
        return self._x
    def Y(self):
        return self._y
    def width(self):
        return self._width
    def height(self):
        return self._height
    def draw(self, x, y):
        pygame.draw.rect(screen, (255, 255, 255), [x, y, self._width, self._height])
        self.set(x, y, self._width, self._height)

class Ball:
    _dx = 0
    _dy = -0
    _x = 0
    _y = 0
    _width = 0
    _height = 0
    def set(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
    
    #methods
    def X(self):
        return self._x
    def Y(self):
        return self._y
    def width(self):
        return self._width
    def height(self):
        return self._height
    def draw(self, x, y):
        pygame.draw.rect(screen, (255, 255, 255), [x, y, self._width, self._height])
        self.set(x, y, self._width, self._height)
    def hitsbounderies(self):
        if self.Y() < 0:
            return True
        if self.Y() + self.width() > 600:
            return True
        return False
    def playerwin(self, p1, p2):
        if self.X() > p2.X() + p2.width() + 10:
            return 1
        if self.X() < p1.X() - p1.width() - 10:
            return 2
        return 0
    def hitsplayer(self, p1, p2):
        if self.X() >= p2.X() - ball.width() and self.Y() > p2.Y() and self.Y() < p2.Y() + p2.height():
            self._x = p2.X() - self._width
            return True
        if self.X() <= p1.X() + ball.width() and self.Y() > p1.Y() and self.Y() < p1.Y() + p1.height():
            self._x = p1.X() + p1.width() + self._width
            return True
        return False

def ai():
    global difficulty, ball, p1, p2, offset, aispeed
    x, y, dx, dy = ball.X(), ball.Y(), ball._dx, ball._dy
    x1, y1, dx1, dy1 = ball.X(), ball.Y(), ball._dx, ball._dy
    x2, y2, dx2, dy2 = ball.X(), ball.Y(), ball._dx, ball._dy
    check = 0
    if selection == 'demo':
        if dy1 < 0:
            dy1 = -15
        else:
            dy1 = 15
        dx1 = 15
        if dy2 < 0:
            dy2 = -15
        else:
            dy2 = 15
        dx2 = 15
        check = [900, 0]
        if start is True:
            if x1 <= check[0]:
                while(x1 > p1.X() + ball.width()):
                    x1 -= dx1
                    if ball.hitsbounderies() is True:
                        dy1 = dy1 * -1
                    y1 -= dy1 - offset
            if x2 >= check[1]:
                while(x2 < p2.X() - ball.width()):
                    x2 += dx2
                    if ball.hitsbounderies() is True:
                        dy2 = dy2 * -1
                    y2 += dy2 + offset
                print(y1, y2)
                return y1, y2
        return 260, 260
    if difficulty == 'easy':
        if dy < 0:
            dy = -2
        else:
            dy = 2
        dx = 2
        check = 600
    if difficulty == 'medium':
        if dy < 0:
            dy = -2
        else:
            dy = 2
        dx = 2
        check = 550
    if difficulty == 'hard':
        if dy < 0:
            dy = -15
        else:
            dy = 15
        dx = 15
        check = 300
    if start is True:
        if x >= check:
            while(x < p2.X() - ball.width()):
                x += dx
                if ball.hitsbounderies() is True:
                    dy = dy * -1
            return y
    if difficulty == 'easy':
        return random.randrange(100, 400)
    if difficulty == 'medium':
        return random.randrange(200, 300)
    if difficulty == 'hard':
        return 260

def draw_text(text, color, surface, x, y):
    myfont = pygame.font.SysFont('Arial', 40)
    textsurface = myfont.render(text, False, color)
    surface.blit(textsurface, (x, y))

def select_gametype():
    global GameRunning, screen
    menu = True
    click = False
    selection = ''
    
    while menu is True:
        screen.fill((0, 0, 0))
        draw_text('Select game type', (255, 255, 255), screen, 275, 200)
        mx, my = pygame.mouse.get_pos()
        #print(mx, my)

        pvp = pygame.Rect(275, 260, 250, 50)
        pve = pygame.Rect(275, 340, 250, 50)
        demo = pygame.Rect(275, 420, 250, 50)
        pygame.draw.rect(screen, (255, 255, 255), pvp)
        pygame.draw.rect(screen, (255, 255, 255), pve)
        pygame.draw.rect(screen, (255, 255, 255), demo)

        draw_text('pvp', (0, 0, 0), screen, 375, 260)
        draw_text('pve', (0, 0, 0), screen, 375, 340)
        draw_text('demo', (0, 0, 0), screen, 359, 420)

        if pvp.collidepoint(mx, my):
            if click is True:
                print("miau")
                return 'pvp'
        if pve.collidepoint(mx, my):
            if click is True:
                print("ham")
                return 'pve'
        if demo.collidepoint(mx, my):
            if click is True:            
                print("quack")
                return 'demo'

        
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                GameRunning = False
            if event.type is pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

def select_difficulty():
    global GameRunning, screen, selection
    menu = True
    click = False
    
    while menu is True:
        if selection == 'demo':
            return 'not set'
        screen.fill((0, 0, 0))
        draw_text('Select game difficulty', (255, 255, 255), screen, 250, 200)
        mx, my = pygame.mouse.get_pos()
        print(mx, my)

        easy = pygame.Rect(275, 260, 250, 50)
        medium = pygame.Rect(275, 340, 250, 50)
        hard = pygame.Rect(275, 420, 250, 50)
        pygame.draw.rect(screen, (255, 255, 255), easy)
        pygame.draw.rect(screen, (255, 255, 255), medium)
        pygame.draw.rect(screen, (255, 255, 255), hard)

        draw_text('easy', (0, 0, 0), screen, 375, 260)
        draw_text('medium', (0, 0, 0), screen, 345, 340)
        draw_text('hard', (0, 0, 0), screen, 375, 420)

        if easy.collidepoint(mx, my):
            if click is True:
                return 'easy'
        if medium.collidepoint(mx, my):
            if click is True:
                return 'medium'
        if hard.collidepoint(mx, my):
            if click is True:
                return 'hard'

        click = False
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                GameRunning = False
            if event.type is pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

pygame.init()
pygame.font.init()

sound = pygame.mixer.Sound('bounce.wav')

GameRunning = True
screen = pygame.display.set_mode((1000, 600))

offset = 0
player2 = False
AI = False
start = False
aispeed = 0
minoffset = -0.05
maxoffset = 0.05
winner = 0

selection = 'not set'
difficulty = 'not set'

p1 = Player()
p2 = Player()
ball = Ball()

selection = select_gametype()
difficulty = select_difficulty()

if selection == 'pvp':
    player2 = True
if selection == 'pve':
    AI = True

if difficulty == 'easy' and player2 is True:
    p1.set(50, 210, 30, 180)
    p2.set(920, 210, 30, 180)
elif difficulty == 'medium' and player2 is True:
    p1.set(50, 240, 30, 120)
    p2.set(920, 240, 30, 120)
elif difficulty == 'hard' and player2 is True:
    p1.set(50, 260, 30, 80)
    p2.set(920, 260, 30, 80)
elif difficulty == 'easy' and AI is True:
    p1.set(50, 210, 30, 180)
    p2.set(920, 260, 30, 80)
    aispeed = 0.3
elif difficulty == 'medium' and AI is True:
    p1.set(50, 240, 30, 120)
    p2.set(920, 260, 30, 80)
    aispeed = 0.6
elif difficulty == 'hard' and AI is True:
    p1.set(50, 260, 30, 80)
    p2.set(920, 260, 30, 80)
    aispeed = 1
elif selection == 'demo':
    p1.set(50, 260, 30, 80)
    p2.set(920, 260, 30, 80)
    aispeed = 1

ball.set(465, 265, 25, 25)

myfont = pygame.font.SysFont('Arial', 20)
textsurface = myfont.render('Player 1: ' + str(p1._score) + '    Player 2: ' + str(p2._score), False, (255, 255, 255))
clock = pygame.time.Clock();
FPS = 2000
#GameLoop
while GameRunning is True:
    screen.fill((0, 0, 0))
    screen.blit(textsurface, (300, 10))

    speed = 1

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            GameRunning = False
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_SPACE:
                ball._dx = 0.3
                ball._dy = -0.3
                start = True
            if event.key is pygame.K_w and p1.Y() > 0:
                p1._speed = -speed
            if event.key is pygame.K_s and p1.Y() + p1.height() <= 600:
                p1._speed = speed
            if player2 == True:
                if event.key is pygame.K_o and p2.Y() > 0:
                    p2._speed = -speed
                if event.key is pygame.K_l and p2.Y() + p2.height() <= 600:
                    p2._speed = speed
        if event.type is pygame.KEYUP:
            if event.key is pygame.K_w or event.key is pygame.K_s:
                p1._speed = 0
            if player2 is True:
                if event.key is pygame.K_o or event.key is pygame.K_l:
                    p2._speed = 0

    if AI is True:
        y = ai()
        if(p2.Y() + p2.height() / 2 < y and p2.Y() + p2.height() < 600):
            p2._speed = aispeed
        if(p2.Y() + p2.height() / 2 > y and p2.Y() > 0):
            p2._speed = -aispeed

    if selection == 'demo':
        y1, y2 = ai()
        if(p1.Y() + p1.height() / 2 < y1 and p1.Y() + p1.height() < 600):
            p1._speed = aispeed
        if(p1.Y() + p1.height() / 2 > y1 and p1.Y() > 0):
            p1._speed = -aispeed
        if(p2.Y() + p2.height() / 2 < y2 and p2.Y() + p2.height() < 600):
            p2._speed = aispeed
        if(p2.Y() + p2.height() / 2 > y2 and p2.Y() > 0):
            p2._speed = -aispeed

    p1.draw(p1.X(), p1.Y() + p1._speed)
    p2.draw(p2.X(), p2.Y() + p2._speed)
    ball.draw(ball.X() + ball._dx + offset, ball.Y() + ball._dy)

    if p1.Y() < 0 or p1.Y() + p1.height() > 600:
        p1._speed = 0
    if p2.Y() < 0 or p2.Y() + p2.height() > 600:
        p2._speed = 0
    if ball.hitsbounderies() is True:
        ball._dy *= -1

    won = ball.playerwin(p1, p2)
    if won == 1 or won == 2:
        ball._dx = 0.3
        ball._dy = -0.3
        ball._x, ball._y, ball._dx, ball._dy = 370, 270, ball._dx * -1, -0.3
        aispeed = 1 
        if won is 1:
            p1._score += 1
        elif won is 2:
            p2._score += 1
        textsurface = myfont.render('Player 1: ' + str(p1._score) + '    Player 2: ' + str(p2._score), False, (255, 255, 255))

    if ball.hitsplayer(p1, p2) is True:
        pygame.mixer.Sound.play(sound)
        ball._dx *= -1
        if ball._dx < 0:
            ball._dx -= 0.05
        if ball._dx > 0:
            ball._dx += 0.05
        if ball._dy < 0:
            ball._dy -= 0.05
        if ball._dy > 0:
            ball._dy += 0.05
        if AI is True and difficulty == 'hard':
            speed += 0.1
            aispeed += 0.2
        offset = random.uniform(minoffset, maxoffset)
        if selection == 'demo':
            aispeed += 0.3

    if p1._score == 10:
        winner = 1
        GameRunning = False
    if p2._score == 10:
        winner = 2
        GameRunning = False
    pygame.display.update()
    clock.tick(FPS)

myfont = pygame.font.SysFont('Arial', 40)
textsurface = myfont.render('Player ' + str(winner) + 'has won the game!', False, (255, 255, 255))

display_winner = True

while display_winner is True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            display_winner = False
    textsurface = myfont.render('Player ' + str(winner) + 'has won the game!', False, (255, 255, 255))
    screen.blit(textsurface, (200, 270))
    pygame.display.update()