import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Pong")

class Ball:
    def __init__(self, x, y, r, sx, sy):
        self.x, self.y, self.r, self.sx, self.sy = x, y, r, sx, sy
    def move(self):
        self.x += self.sx; self.y += self.sy
    def draw(self, s):
        pygame.draw.circle(s, WHITE, (self.x, self.y), self.r)
    def bounce(self, d):
        if d == 'x': self.sx = -self.sx
        elif d == 'y': self.sy = -self.sy

class Paddle:
    def __init__(self, x, y, w, h, s):
        self.x, self.y, self.w, self.h, self.s = x, y, w, h, s
    def move(self, d):
        if d == 'up' and self.y > 0: self.y -= self.s
        elif d == 'down' and self.y < SCREEN_HEIGHT - self.h: self.y += self.s
    def draw(self, s):
        pygame.draw.rect(s, WHITE, (self.x, self.y, self.w, self.h))

def main():
    clock = pygame.time.Clock()
    ball = Ball(400, 300, 10, 5, 5)
    lp = Paddle(30, 250, 10, 100, 10)
    rp = Paddle(760, 250, 10, 100, 10)
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: lp.move('up')
        if keys[pygame.K_s]: lp.move('down')
        if keys[pygame.K_UP]: rp.move('up')
        if keys[pygame.K_DOWN]: rp.move('down')
        ball.move()
        if ball.y <= 0 or ball.y >= SCREEN_HEIGHT: ball.bounce('y')
        if ball.x <= 0 or ball.x >= SCREEN_WIDTH: ball.x = 400
        if ball.x - ball.r <= lp.x + lp.w and lp.y <= ball.y <= lp.y + lp.h: ball.bounce('x')
        if ball.x + ball.r >= rp.x and rp.y <= ball.y <= rp.y + rp.h: ball.bounce('x')
        ball.draw(screen); lp.draw(screen); rp.draw(screen)
        pygame.display.flip(); clock.tick(60)
    pygame.quit(); sys.exit()

if __name__ == "__main__": main()
